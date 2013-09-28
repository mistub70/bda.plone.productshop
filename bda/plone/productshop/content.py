from zope.interface import implementer
from plone.dexterity.content import (
    Item,
    Container,
)
from .interfaces import (
    IProduct,
    IProductGroup,
    IVariant,
)


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
