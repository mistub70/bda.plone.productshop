from zope import schema
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText
from .interfaces import (
    IProduct,
    IProductGroup,
    IVariant,
    IColorVariant,
    IWeightVariant,
)


_ = MessageFactory('bda.plone.shopviews')


class IProductBehavior(model.Schema, IProduct):
    """Product behavior.
    """
    image = NamedBlobImage(
        title=_(u'image_title', default=u'Product Image'),
        description=_(u'image_description',
                      default=u'Preview image of Product'),
        required=False)

    details = RichText(
        title=_(u'details_title', default=u'Details'),
        description=_(u'details_description',
                      default=u'Details about the product'),
        required=False)

    datasheet = RichText(
        title=_(u'datasheet_title', default=u'Datasheet'),
        description=_(u'datasheet_description',
                      default=u'Datasheet of the product'),
        required=False)


alsoProvides(IProductBehavior, IFormFieldProvider)


class IProductGroupBehavior(IProductBehavior, IProductGroup):
    """Product group behavior.
    """


alsoProvides(IProductGroupBehavior, IFormFieldProvider)


class IVariantBehavior(IProductBehavior, IVariant):
    """Variant base behavior.
    """


alsoProvides(IVariantBehavior, IFormFieldProvider)


class IColorVariantBehavior(IVariantBehavior, IColorVariant):
    """Color variant behavior.
    """
    color = schema.TextLine(
        title=_(u'color_title', default=u'Product Color'),
        description=_(u'color_description',
                      default=u'Product Color as hex string i.e. #000000'),
        required=False)


alsoProvides(IColorVariantBehavior, IFormFieldProvider)


class IWeightVariantBehavior(IVariantBehavior, IWeightVariant):
    """Weight variant behavior.
    """
    weight = schema.Float(
        title=_(u'weight_title', default=u'Product Weight'),
        description=_(u'weight_description',
                      default=u'Weight of the Product in Kilo'),
        required=False)


alsoProvides(IWeightVariantBehavior, IFormFieldProvider)
