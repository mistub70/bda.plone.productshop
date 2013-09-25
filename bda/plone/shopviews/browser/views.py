from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from ..interfaces import IProduct


_ = MessageFactory('bda.plone.shopviews')


class Listing(BrowserView):
    """Product Listing.
    """
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
            image = None
            if obj.image:
                scales = obj.restrictedTraverse('@@images')
                scale = scales.scale('image', self.image_scale)
                if scale:
                    image = scale.tag(css_class='product_listing_image')
            ret.append({
               'obj': obj,
               'preview': image,
            })
        return ret


class Product(BrowserView):
    """Product view.
    """
    image_scale = 'mini'

    @property
    def image(self):
        if not self.context.image:
            return None
        scales = self.context.restrictedTraverse('@@images')
        scale = scales.scale('image', self.image_scale)
        if not scale:
            return None
        return scale.tag(css_class='product_image')
