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
        #not working at the moment
        #so the same code is 3 times below
        context = self.context
        content_type = context.portal_type
        is_folderish = ['Folder', 'ATFolder', 'Productgruppe', 'Group', 'Topic', 'Collection']
        catalog = getToolByName(self, 'portal_catalog')
        if type in is_folderish: 
            folder_path = '/'.join(context.getPhysicalPath())
        else:
            folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        return results
                
    @property    
    def all_keywords(self):
        #results = self.find_objects
        context = self.context
        content_type = context.portal_type
        is_folderish = ['Folder', 'ATFolder', 'Productgruppe', 'Group', 'Topic', 'Collection']
        catalog = getToolByName(self, 'portal_catalog')
        
        if content_type in is_folderish: 
            folder_path = '/'.join(context.getPhysicalPath())
        else:
            folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
        uniques = ""
        tags = set()
        for item in results:
            tags.update(item.Subject)
        return sorted(tags)
        
    @property    
    def variations(self):
        #results = self.find_objects
        context = self.context
        content_type = context.portal_type
        is_folderish = ['Folder', 'ATFolder', 'Productgruppe', 'Group', 'Topic', 'Collection']
        catalog = getToolByName(self, 'portal_catalog')
        
        if content_type in is_folderish: 
            folder_path = '/'.join(context.getPhysicalPath())
        else:
            folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
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
        #results = self.find_objects
        context = self.context
        content_type = context.portal_type
        is_folderish = ['Folder', 'ATFolder', 'Productgruppe', 'Group', 'Topic', 'Collection']
        catalog = getToolByName(self, 'portal_catalog')
        pdb; pdb.set_trace()
        if content_type in is_folderish: 
            folder_path = '/'.join(context.getPhysicalPath())
        else:
            folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
        uniques = ""
        tags = set()
        for item in results:
            try:
                tags.update(item.color)
            except:
                pass
        return sorted(tags)