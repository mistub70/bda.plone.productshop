from plone.dexterity.content import Item
from plone.dexterity.content import Container


class Product(Item):
    """Product Content.
    """


class ProductGroup(Container):
    """Product Group content.
    """


class Variant(Item):
    """Variant content.
    """
