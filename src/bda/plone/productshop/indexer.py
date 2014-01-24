from plone.indexer import indexer
from .behaviors import IColorBehavior
from .behaviors import IWeightBehavior
from .behaviors import ISizeBehavior
from .behaviors import IDemandBehavior
from .behaviors import ILengthBehavior
from .behaviors import IWidthBehavior
from .behaviors import IHeightBehavior
from .behaviors import IIPCodeBehavior
from .behaviors import IAngleBehavior


@indexer(IColorBehavior)
def color_aspect(obj):
    return obj.color


@indexer(IWeightBehavior)
def weight_aspect(obj):
    return obj.weight


@indexer(ISizeBehavior)
def size_aspect(obj):
    return obj.size


@indexer(IDemandBehavior)
def demand_aspect(obj):
    return obj.demand


@indexer(ILengthBehavior)
def length_aspect(obj):
    return obj.length


@indexer(IWidthBehavior)
def width_aspect(obj):
    return obj.width


@indexer(IHeightBehavior)
def height_aspect(obj):
    return obj.height


@indexer(IIPCodeBehavior)
def ip_code_aspect(obj):
    return obj.ip_code


@indexer(IAngleBehavior)
def angle_aspect(obj):
    return obj.angle
