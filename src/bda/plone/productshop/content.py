from zope.interface import implementer
from plone.dexterity.content import Item
from plone.dexterity.content import Container
from .interfaces import IProduct
from .interfaces import IProductGroup
from .interfaces import IVariant


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
