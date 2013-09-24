from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from ..interfaces import IProduct


_ = MessageFactory('bda.plone.shopviews')


class Listing(BrowserView):
    """Product Listing.
    """

    @property
    def products(self):
        cat = getToolByName(self.context, 'portal_catalog')
        ret = list()
        query = {
            'object_provides': IProduct,
            'path': {
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1,
            },
        }
        for brain in cat.query(**query):
            ret.append(brain)
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
