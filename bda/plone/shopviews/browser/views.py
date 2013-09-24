from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


_ = MessageFactory('bda.plone.shopviews')


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


class ColorsView(BrowserView):
    """Browser view that does the following.
    - redirects to parent folder of product.
    - sets color to context's color
    - uses this in the folder view
    """

    def __call__(self):
        request = self.request
        color = self.context.color
        redirect_url = self.context.aq_parent.absolute_url() + \
                       '/productlist_view?color=' + \
                       color
        return redirect_url


class ProductsView(BrowserView):
    """Products browser view.
    """

    def find_objects(self):
        #not working at the moment
        #so the same code is 3 times below
        catalog = getToolByName(self, 'portal_catalog')
        if context.is_folderish:
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
        catalog = getToolByName(self, 'portal_catalog')
        #if IFolderish.isProvidedBy(context.aq_base): 
        folder_path = '/'.join(context.getPhysicalPath())
        #else:
        #    folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})

        tags = set()
        for item in results:
            tags.update(item.Subject)
        return sorted(tags)

    @property
    def variations(self):
        #results = self.find_objects
        context = self.context
        catalog = getToolByName(self, 'portal_catalog')
        #if IFolderish.isProvidedBy(context.aq_base):
        folder_path = '/'.join(context.getPhysicalPath())
        #else:
        #    folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})

        tags = []
        for item in results:
            tags.append(item.variation)
        return sorted(tags)

    @property
    def colors(self):
        #results = self.find_objects
        context = self.context
        parent = context.aq_parent.aq_inner
        catalog = getToolByName(self, 'portal_catalog')
        folder_path = '/'.join(parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})

        colors = []
        for item in results:
            if item.color:
                colors.append(item.color)
        return sorted(colors)

    @property
    def get_groups(self):
        current = api.user.get_current()
        groups_tool = getToolByName(self, 'portal_groups')
        return groups_tool.getGroupsByUserId(current)

    @property
    def get_user(self):
        return  api.user.get_current()
