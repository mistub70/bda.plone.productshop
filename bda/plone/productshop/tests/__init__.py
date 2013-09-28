from zope.interface import alsoProvides
from plone.app.testing import (
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from bda.plone.productshop.interfaces import IProductShop


def set_browserlayer(request):
    """Set the BrowserLayer for the request.

    We have to set the browserlayer manually, since importing the profile alone
    doesn't do it in tests.
    """
    alsoProvides(request, IProductShop)


class ProductShopLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import bda.plone.productshop
        self.loadZCML(package=bda.plone.productshop,
                      context=configurationContext)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'bda.plone.productshop:default')

    def tearDownZope(self, app):
        pass


ProductShop_FIXTURE = ProductShopLayer()
ProductShop_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ProductShop_FIXTURE,),
    name="ProductShop:Integration")