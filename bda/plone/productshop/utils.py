from zope.component import getUtilitiesFor
from plone.behavior.interfaces import IBehavior
from z3c.form.field import Fields
from .interfaces import IVariantAspect


class VariantAspectDefinition(object):

    def __init__(self, interface):
        fields = Fields(interface)
        if len(fields) != 1:
            raise ValueError(u'Variant aspect schema must provide exactly 1 '
                             u'field')
        for key in fields:
            break
        self.attribute = key
        self.title = fields[self.attribute].field.title
        self.interface = interface


def available_variant_aspects():
    aspects = list()
    for behavior in getUtilitiesFor(IBehavior):
        interface = behavior[1].interface
        if interface.isOrExtends(IVariantAspect):
            aspects.append(VariantAspectDefinition(interface))
    return aspects
