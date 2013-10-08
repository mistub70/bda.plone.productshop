from plone.indexer import indexer
from .behaviors import (
    IColorBehavior,
    IWeightBehavior,
    ISizeBehavior,
    IDemandBehavior,
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
