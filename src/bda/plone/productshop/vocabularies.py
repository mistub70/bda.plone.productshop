from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import (
    SimpleVocabulary,
    SimpleTerm,
)
from zope.i18nmessageid import MessageFactory
from .utils import (
    dotted_name,
    available_variant_aspects,
)

#added by espen
from zope.component import getUtility
from plone.dexterity.interfaces import IDexterityFTI

_ = MessageFactory('bda.plone.productshop')


def AvailableVariantAspectsVocabulary(context):
    terms = list()
    for definition in available_variant_aspects():
        terms.append(SimpleTerm(value=dotted_name(definition.interface),
                                title=definition.title))
    return SimpleVocabulary(terms)


directlyProvides(AvailableVariantAspectsVocabulary, IVocabularyFactory)



def RtfFieldsVocabulary(context):
    try:
        fields = list(getUtility(IDexterityFTI, name='bda.plone.productshop.product').lookupSchema())
    except:
        fields = ()
    #datasheet and details are not found as they come from a behaviour
    #I think we should remove these fields as a behaviour, since
    #it is not possible to customize them TTW
    fields += ('datasheet', 'details')
    terms = [ SimpleTerm(value=pair, token=pair, title=pair) for pair in fields]
    return SimpleVocabulary(terms)

directlyProvides(RtfFieldsVocabulary, IVocabularyFactory)

