import json
from Acquisition import (
    aq_inner,
    aq_parent,
)
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from bda.plone.cart import get_object_by_uid
from ..interfaces import (
    IProduct,
    IProductGroup,
    IVariant,
)
from ..utils import (
    request_property,
    available_variant_aspects,
)


_ = MessageFactory('bda.plone.productshop')


def query_children(context, criteria=dict()):
    cat = getToolByName(context, 'portal_catalog')
    query = {
        'path': {
            'query': '/'.join(context.getPhysicalPath()),
            'depth': 1,
        },
        'order_by': 'objPositionInParent',
    }
    query.update(criteria)
    return cat(**query)


def img_tag(context, scale, css_class):
    if not context.image:
        return None
    scales = context.restrictedTraverse('@@images')
    scale = scales.scale('image', scale)
    if not scale:
        return None
    return scale.tag(css_class=css_class)


class ProductListing(BrowserView):
    image_scale = 'thumb'

    @property
    def products(self):
        ret = list()
        for brain in query_children(self.context):
            obj = brain.getObject()
            if not IProduct.providedBy(obj):
                continue
            item = dict()
            item['obj'] = obj
            item['preview'] = img_tag(
                obj, self.image_scale, 'product_listing_image')
            item['buyable_controls'] = True
            if IProductGroup.providedBy(obj):
                item['buyable_controls'] = False
            ret.append(item)
        return ret


class ProductView(BrowserView):
    image_scale = 'mini'

    @property
    def image(self):
        return img_tag(self.context, self.image_scale, 'product_image')

    @property
    def details(self):
        return self.context.details

    @property
    def datasheet(self):
        return self.context.datasheet

    @property
    def related_items(self):
        if hasattr(self.context, 'relatedItems'):
            return self.context.relatedItems
        return None


class ProductGroupView(BrowserView):

    @request_property
    def variant(self):
        obj = None
        for brain in query_children(self.context):
            obj = brain.getObject()
            break
        return obj

    @property
    def rendered_variant(self):
        obj = self.variant
        if obj:
            return obj.restrictedTraverse('@@bda.plone.productshop.variant')
        return None


class AspectsBase(BrowserView):

    @property
    def variants(self):
        raise NotImplementedError(u'Abstract ``AspectsBase`` does not '
                                  u'implement ``variants``.')

    @property
    def aspects(self):
        raise NotImplementedError(u'Abstract ``AspectsBase`` does not '
                                  u'implement ``aspects``.')

    def variant_value(self, definition, context=None):
        if not context:
            context = self.context
        if not definition.interface.providedBy(context):
            return None
        return getattr(context, definition.attribute, None)

    def variant_values(self, definition):
        ret = list()
        for variant in self.variants:
            value = self.variant_value(definition, variant)
            if value:
                ret.append(value)
        return ret


class ProductGroupAspects(AspectsBase):

    @request_property
    def variants(self):
        return [_.getObject() for _ in query_children(self.context)]

    @property
    def aspects(self):
        aspects = list()
        for definition in available_variant_aspects():
            aspect = dict()
            aspect['title'] = definition.title
            aspect['name'] = definition.attribute
            aspect['options'] = options = list()
            #selected_value = self.variant_value(definition)
            #if not selected_value:
            #    continue
            for value in self.variant_values(definition):
                option = dict()
                option['title'] = value
                option['value'] = value
                #option['selected'] = value == selected_value
                option['selected'] = False
                options.append(option)
            if options:
                aspects.append(aspect)
        return aspects


class VariantBase(BrowserView):

    @property
    def product_group(self):
        return aq_parent(aq_inner(self.context))


class VariantAspects(VariantBase, AspectsBase):

    @request_property
    def variants(self):
        return [_.getObject() for _ in query_children(self.product_group)]

    @property
    def aspects(self):
        aspects = list()
        for definition in available_variant_aspects():
            aspect = dict()
            aspect['title'] = definition.title
            aspect['name'] = definition.attribute
            aspect['options'] = options = list()
            selected_value = self.variant_value(definition)
            if not selected_value:
                continue
            for value in self.variant_values(definition):
                option = dict()
                option['title'] = value
                option['value'] = value
                option['selected'] = value == selected_value
                options.append(option)
            if options:
                aspects.append(aspect)
        return aspects


class VariantLookup(BrowserView):

    @property
    def product_group(self):
        self.scope = None
        uid = self.request.get('variant_aspects_uid')
        if not uid:
            raise ValueError(u'No execution context UID')
        obj = get_object_by_uid(self.context, uid)
        if not obj:
            raise ValueError(u'Execution context object not found by UID')
        if IProductGroup.providedBy(obj):
            self.scope = 'productgroup'
            return obj
        if IVariant.providedBy(obj):
            self.scope = 'variant'
            return aq_parent(obj)
        raise ValueError(u'Object not implements IProductGroup or IVariant')

    @property
    def filtered_variants(self):
        criteria = dict()
        for definition in available_variant_aspects():
            key = definition.attribute
            value = self.request.get(key)
            if value:
                criteria['%s_aspect' % key] = value
        return query_children(self.product_group, criteria=criteria)

    def variant_uid_by_criteria(self):
        """Return UID of first variant found by aspect criteria.

        Base assumption is that each variant has a unique set of aspects. It
        makes not much sence to have 2 Variants with color red and weight 10
        if this 2 aspects are enabled.
        """
        found = False
        oid = None
        uid = None
        url = None
        for brain in self.filtered_variants:
            found = True
            oid = brain.id
            uid = brain.UID
            url = brain.getURL()
            break
        return json.dumps({
            'scope': self.scope,
            'found': found,
            'oid': oid,
            'uid': uid,
            'url': url,
        })


class VariantView(ProductView, VariantBase):

    @property
    def image(self):
        context_image = img_tag(
            self.context, self.image_scale, 'product_image')
        if context_image:
            return context_image
        return img_tag(self.product_group, self.image_scale, 'product_image')

    @property
    def details(self):
        if self.context.details:
            return self.context.details
        return self.product_group.details

    @property
    def datasheet(self):
        if self.context.datasheet:
            return self.context.datasheet
        return self.product_group.datasheet

    @property
    def related_items(self):
        context = self.context
        if hasattr(context, 'relatedItems'):
            if context.relatedItems:
                return context.relatedItems
        product_group = self.product_group
        if hasattr(product_group, 'relatedItems'):
            if product_group.relatedItems:
                return product_group.relatedItems
        return None
