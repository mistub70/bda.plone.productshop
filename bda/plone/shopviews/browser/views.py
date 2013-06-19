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

	#this is just for quicksand, probably
	def all_keywords(self):
		#finding unique keywords
		#must be a faster way to do this
		object = ["a", "b", "c"]
		#objects = ???
		uniques = ""
		for item in objects:
			uniques += " "
			uniques += (item['keywords'])
		tags = uniques.split()
		tags = set(tags)
		return sorted(tags)
		#Need to fix this for keywords containing spaces
