from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.i18nmessageid import MessageFactory
from bda.plone.productshop.utils import dotted_name
from bda.plone.productshop.utils import available_variant_aspects


_ = MessageFactory('bda.plone.productshop')


def AvailableVariantAspectsVocabulary(context):
    terms = list()
    for definition in available_variant_aspects():
        terms.append(SimpleTerm(value=dotted_name(definition.interface),
                                title=definition.title))
    return SimpleVocabulary(terms)


directlyProvides(AvailableVariantAspectsVocabulary, IVocabularyFactory)
