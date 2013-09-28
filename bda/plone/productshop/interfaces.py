from zope.interface import Interface
from plone.namedfile.interfaces import IImageScaleTraversable
from collective.instancebehavior import IInstanceBehaviorAssignableContent


class IProductShopExtensionLayer(Interface):
    """Product shop specific browser layer.
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


class IVariant(IProduct, IInstanceBehaviorAssignableContent):
    """Marker interface for variant content.
    """


class IVariantAspect(Interface):
    """Aspect of a variant.
    """
