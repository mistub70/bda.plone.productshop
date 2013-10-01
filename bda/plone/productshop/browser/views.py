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


class ProductListing(BrowserView):
    image_scale = 'thumb'

    @property
    def products(self):
        ret = list()
        for brain in query_children(self.context):
            item = self.create_listing_item(brain)
            if not item:
                continue
            ret.append(item)
        return ret

    def create_listing_item(self, brain):
        obj = brain.getObject()
        if not IProduct.providedBy(obj):
            return None
        item = dict()
        item['obj'] = obj
        item['preview'] = img_tag(
            obj, self.image_scale, 'product_listing_image')
        item['buyable_controls'] = True
        if IProductGroup.providedBy(obj):
            item['buyable_controls'] = False
        return item


class AspectsExtraction(object):

    @property
    def aspects_criteria(self):
        criteria = dict()
        for definition in available_variant_aspects():
            key = definition.attribute
            value = self.request.get(key)
            if value and value != 'UNSET':
                criteria['%s_aspect' % key] = value
        return criteria


class ProductGroupListing(ProductListing, AspectsExtraction):

    @property
    def products(self):
        ret = list()
        criteria = self.aspects_criteria
        for brain in query_children(self.context, criteria=criteria):
            item = self.create_listing_item(brain)
            if not item:
                continue
            ret.append(item)
        return ret


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


class Aspects(BrowserView):
    scope = None

    @property
    def variants(self):
        raise NotImplementedError(u'Abstract ``Aspects`` does not '
                                  u'implement ``variants``.')

    @property
    def aspects(self):
        raise NotImplementedError(u'Abstract ``Aspects`` does not '
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

    def create_aspect(self, title, name):
        aspect = dict()
        aspect['title'] = title
        aspect['name'] = name
        aspect['options'] = list()
        return aspect

    def create_option(self, title, value, selected):
        option = dict()
        option['title'] = title
        option['value'] = value
        option['selected'] = selected
        return option


class ProductGroupAspects(Aspects):
    scope = 'productgroup'

    @request_property
    def variants(self):
        return [_.getObject() for _ in query_children(self.context)]

    @property
    def aspects(self):
        aspects = list()
        for definition in available_variant_aspects():
            aspect = self.create_aspect(definition.title, definition.attribute)
            options = aspect['options']
            for value in self.variant_values(definition):
                options.append(self.create_option(value, value, False))
            if options:
                options.insert(0, self.create_option('all', 'UNSET', True))
                aspects.append(aspect)
        return aspects


class VariantBase(BrowserView):

    @property
    def product_group(self):
        return aq_parent(aq_inner(self.context))


class VariantAspects(VariantBase, Aspects):
    scope = 'variant'

    @request_property
    def variants(self):
        return [_.getObject() for _ in query_children(self.product_group)]

    @property
    def aspects(self):
        aspects = list()
        for definition in available_variant_aspects():
            aspect = self.create_aspect(definition.title, definition.attribute)
            options = aspect['options']
            selected_value = self.variant_value(definition)
            for value in self.variant_values(definition):
                selected = value == selected_value
                options.append(self.create_option(value, value, selected))
            if options:
                if not selected_value:
                    options.insert(0, self.create_option('-', 'UNSET', True))
                aspects.append(aspect)
        return aspects


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


class VariantLookup(BrowserView, AspectsExtraction):

    @property
    def product_group(self):
        uid = self.request.get('uid')
        if not uid:
            raise ValueError(u'No execution context UID')
        obj = get_object_by_uid(self.context, uid)
        if not obj:
            raise ValueError(u'Execution context object not found by UID')
        if IProductGroup.providedBy(obj):
            return obj
        if IVariant.providedBy(obj):
            return aq_parent(obj)
        raise ValueError(u'Object not implements IProductGroup or IVariant')

    def variant_uid_by_criteria(self):
        """Return UID of first variant found by aspect criteria.

        Base assumption is that each variant has a unique set of aspects. It
        makes not much sence to have 2 Variants with color red and weight 10
        if this 2 aspects are enabled.
        """
        found = False
        oid = uid = url = None
        criteria = self.aspects_criteria
        try:
            product_group = self.product_group
        except ValueError, e:
            return json.dumps({
                'found': False,
                'error': str(e),
            })
        for brain in query_children(product_group, criteria=criteria):
            found = True
            oid = brain.id
            uid = brain.UID
            url = brain.getURL()
            break
        return json.dumps({
            'found': found,
            'oid': oid,
            'uid': uid,
            'url': url,
        })
