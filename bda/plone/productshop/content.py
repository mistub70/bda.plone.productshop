from plone.dexterity.content import (
    Item,
    Container,
)


class Product(Item):
    """Product Content.
    """


class ProductGroup(Container):
    """Product Group content.
    """


class Variant(Item):
    """Variant content.
    """
