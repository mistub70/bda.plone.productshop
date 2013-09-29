from Acquisition import (
    aq_inner,
    aq_parent,
)
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from ..interfaces import (
    IProduct,
    IProductGroup,
)
from ..utils import available_variant_aspects


_ = MessageFactory('bda.plone.productshop')


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
        cat = getToolByName(self.context, 'portal_catalog')
        ret = list()
        query = {
            'path': {
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1,
            },
        }
        for brain in cat(**query):
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


class VariantView(ProductView):

    @property
    def parent(self):
        return aq_parent(aq_inner(self.context))

    @property
    def image(self):
        context_image = img_tag(
            self.context, self.image_scale, 'product_image')
        if context_image:
            return context_image
        return img_tag(self.parent, self.image_scale, 'product_image')

    @property
    def details(self):
        if self.context.details:
            return self.context.details
        return self.parent.details

    @property
    def datasheet(self):
        if self.context.datasheet:
            return self.context.datasheet
        return self.parent.datasheet

    @property
    def related_items(self):
        context = self.context
        if hasattr(context, 'relatedItems'):
            if context.relatedItems:
                return context.relatedItems
        parent = self.parent
        if hasattr(parent, 'relatedItems'):
            if parent.relatedItems:
                return parent.relatedItems
        return None
