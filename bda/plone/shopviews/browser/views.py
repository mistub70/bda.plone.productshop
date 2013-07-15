from zope.interface import implements, Interface, Attribute
from Products.Five import BrowserView

#from bda.plone.cart.interfaces.ICartDataProvider import  get_data_provider
from bda.plone.shopviews import shopviewsMessageFactory  as _

from Products.CMFCore.utils import getToolByName



class IColorsView(Interface):
    """
    Redirect  view interface
    """
    
class IProductsView(Interface):
    """
    Products  view interface
    """
    
    #def currency(self):
    #    """Get the currency"""
        
    def test():
        """ test method"""
        
    def all_keywords():
        """ get all keywords in folder so we can sort on them """

    def colors():
        """ get (all) color (field) in your content type for folder """

    def variations():
        """ get (all) variation (field) in your content type for folder """

class ColorsView(BrowserView):
    """
    Browser view that does the following.
    - redirects to parent folder of product.
    - sets color to context's color
    - uses this in the folder view
    """
    implements(IColorsView)
    
    
    def __call__(self):
        request = self.request
        color = self.context.color
        redirect_url = self.context.aq_parent.absolute_url() + '/productlist_view?color=' + color
        #return self.context.redirect(redirect_url)
        return redirect_url

class ProductsView(BrowserView):
    """
    Products browser view
    """
    implements(IProductsView)
    
    #property
    #def currency(self):
    #    return self.data_provider.currency

    def test(self):
        """
        test method
        """
        
        dummy = _(u'a dummy string')
        return {'dummy': dummy}

    def find_objects(self):
        catalog = getToolByName(self, 'portal_catalog')
        folder_path = '/'.join(self.context.getPhysicalPath())
        results = []
        return catalog.searchResults(path={'query': folder_path})
                
    @property    
    def all_keywords(self):
        catalog = getToolByName(self, 'portal_catalog')
        folder_path = '/'.join(self.context.getPhysicalPath())
        results = []
        results =  catalog.searchResults(path={'query': folder_path})
        uniques = ""
        tags = set()
        for item in results:
            tags.update(item.Subject)
        return sorted(tags)
        
    @property    
    def variations(self):
        results = find_objects()
        uniques = ""
        tags = set()
        for item in results:
            try:
                tags.update(item.variation)
            except:
                pass
        return sorted(tags)
        
    @property    
    def colors(self):
        catalog = getToolByName(self, 'portal_catalog')
        folder_path = '/'.join(self.context.getPhysicalPath())
        results = []
        results =  catalog.searchResults(path={'query': folder_path})
        uniques = ""
        tags = set()
        for item in results:
            try:
                tags.update(item.color)
            except:
                pass
        return sorted(tags)