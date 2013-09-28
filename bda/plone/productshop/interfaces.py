from zope.interface import Interface
from plone.namedfile.interfaces import IImageScaleTraversable


class IShopViews(Interface):
    """Shop views specific browser layer.
    """


##############################################################################
# content markers
##############################################################################

class IProduct(Interface, IImageScaleTraversable):
    """Marker interface for product content.
    """


class IProductGroup(IProduct):
    """Marker interface for product group content.
    """


class IVariant(IProduct):
    """Marker interface for variant content.
    """


class IColorVariant(IVariant):
    """Marker interface for color variants content.
    """


class IWeightVariant(IVariant):
    """Marker interface for weight variant content.
    """
