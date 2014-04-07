from zope.interface import implementer
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from bda.plone.productshop.interfaces import IProduct
from bda.plone.productshop.interfaces import IProductGroup
from bda.plone.productshop.interfaces import IVariant


@implementer(IProduct)
class Product(Item):
    """Product Content.
    """


@implementer(IProductGroup)
class ProductGroup(Container):
    """Product Group content.
    """


@implementer(IVariant)
class Variant(Item):
    """Variant content.
    """
