# -*- coding: utf-8 -*-
from bda.plone.productshop.utils import available_variant_aspects
from bda.plone.productshop.utils import dotted_name
from plone.app.imaging.utils import getAllowedSizes
from zope.i18nmessageid import MessageFactory
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


_ = MessageFactory('bda.plone.productshop')


@provider(IVocabularyFactory)
def AvailableVariantAspectsVocabulary(context):
    terms = list()
    for definition in available_variant_aspects():
        terms.append(SimpleTerm(value=dotted_name(definition.interface),
                                title=definition.title))
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def ImageScaleVocabulary(context):
    allowed_sizes = getAllowedSizes()
    items = [(u'{0}({1}, {2})'.format(key, value[0], value[1]), key)
             for key, value in allowed_sizes.items() if allowed_sizes]
    return SimpleVocabulary.fromItems(items)
