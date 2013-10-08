from plone.indexer import indexer
from .behaviors import (
    IColorBehavior,
    IWeightBehavior,
    ISizeBehavior,
    IDemandBehavior,
    ILengthBehavior,
    IWidthBehavior,
    IHeightBehavior,
)


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
