from zope import schema
from zope.interface import alsoProvides
from zope.component import provideAdapter
from zope.i18nmessageid import MessageFactory
from z3c.form.widget import ComputedWidgetAttribute
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from plone.app.textfield import RichText
from .interfaces import (
    IProduct,
    IProductGroup,
    IVariant,
    IVariantAspect,
)


_ = MessageFactory('bda.plone.productshop')


class IProductExcludeFromNavigation(IExcludeFromNavigation):
    """Exclude from navigation behavior for products.

    Could not find a sane way of providing default values for general behavior
    attributes based on content interface which the behavior is bound to.
    Registering ComputedWidgetAttribute to context does not help because
    context is the container in case of add form instead of a content instance.
    """


alsoProvides(IProductExcludeFromNavigation, IFormFieldProvider)


provideAdapter(ComputedWidgetAttribute(
    lambda data: True,
    field=IProductExcludeFromNavigation['exclude_from_nav']),
    name='default')


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


class IColor(IVariantAspect):
    """Color variant behavior.
    """
    color = schema.TextLine(
        title=_(u'color_title', default=u'Product Color'),
        description=_(u'color_description',
                      default=u'Product Color as hex string i.e. #000000'),
        required=False)


alsoProvides(IColor, IFormFieldProvider)


class IWeight(IVariantAspect):
    """Weight variant behavior.
    """
    weight = schema.Float(
        title=_(u'weight_title', default=u'Product Weight'),
        description=_(u'weight_description',
                      default=u'Weight of the Product in Kilo'),
        required=False)


alsoProvides(IWeight, IFormFieldProvider)
