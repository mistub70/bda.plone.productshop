from zope.interface import implements, Interface, Attribute
from Products.Five import BrowserView

#from bda.plone.cart.interfaces.ICartDataProvider import  get_data_provider

from bda.plone.shopviews import shopviewsMessageFactory  as _


class IProductsView(Interface):
    """
    Products  view interface
    """
    
    #def currency(self):
    #    """Get the currency"""
        
    def test():
        """ test method"""
        

    def all_keywords():
        """ get all keywords so we can sort on them """



#I am not sure if this is the right way to define the view

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
        
    
    @property
    def all_keywords(self, context):
        """
        get all keywords in current folder so we can sort on them
        """
        folder_path = '/'.join(context.getPhysicalPath())
        results = catalog(path={'query': folder_path, 'depth': 1})
        my_keys = results.uniqueValuesFor('Subject')
        return sorted(my_keys)
        