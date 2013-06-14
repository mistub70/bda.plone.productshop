from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from bda.plone.shopviews import shopviewMessageFactory as _

class IProductsView(Interface):
    """
    Products  view interface
    """

    def test():
        """ test method"""


class IProductsView(BrowserView):
    """
    Products browser view
    """
    implements(IProductsView)


    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
