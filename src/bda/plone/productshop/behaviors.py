from zope import schema
from zope.interface import alsoProvides
from zope.component import provideAdapter
from zope.i18nmessageid import MessageFactory
from z3c.form.widget import ComputedWidgetAttribute
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.supermodel import model
from plone.directives import form
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
    item_number = schema.TextLine(
        title=_(u'item_number_title', default=u'Item number'),
        description=_(u'item_number_description',
                      default=u'Item number of the product'),
        required=False)

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
    form.fieldset(
        'settings',
        fields=['default_variant_aspects'])

    form.widget(default_variant_aspects=CheckBoxFieldWidget)
    default_variant_aspects = schema.List(
        title=_(u'default_variant_aspects_title',
                default=u'Default variant aspects'),
        description=_(u'default_variant_aspects_description',
                      default=u'Variant aspects enabled by default when '
                              u'adding new variants'),
        required=False,
        missing_value=set(),
        value_type=schema.Choice(
            vocabulary=
                'bda.plone.productshop.AvailableVariantAspectsVocabulary'))


alsoProvides(IProductGroupBehavior, IFormFieldProvider)


class IVariantBehavior(IProductBehavior, IVariant):
    """Variant base behavior.
    """


alsoProvides(IVariantBehavior, IFormFieldProvider)


class IColorBehavior(IVariantAspect):
    """Color variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['color'])

    color = schema.TextLine(
        title=_(u'color_title', default=u'Color'),
        description=_(u'color_description',
                      default=u'Color of the product'),
        required=False)


alsoProvides(IColorBehavior, IFormFieldProvider)


class IWeightBehavior(IVariantAspect):
    """Weight variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['weight'])

    weight = schema.TextLine(
        title=_(u'weight_title', default=u'Weight'),
        description=_(u'weight_description',
                      default=u'Weight of the product'),
        required=False)


alsoProvides(IWeightBehavior, IFormFieldProvider)


class ISizeBehavior(IVariantAspect):
    """Size variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['size'])

    size = schema.TextLine(
        title=_(u'size_title', default=u'Size'),
        description=_(u'size_description',
                      default=u'Size of the product'),
        required=False)


alsoProvides(ISizeBehavior, IFormFieldProvider)


class IDemandBehavior(IVariantAspect):
    """Demand variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['demand'])

    demand = schema.TextLine(
        title=_(u'demand_title', default=u'Demand'),
        description=_(u'demand_description',
                      default=u'Demand of the product'),
        required=False)


alsoProvides(IDemandBehavior, IFormFieldProvider)


class ILengthBehavior(IVariantAspect):
    """Length variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['length'])

    length = schema.TextLine(
        title=_(u'length_title', default=u'Length'),
        description=_(u'length_description',
                      default=u'Length of the product'),
        required=False)


alsoProvides(ILengthBehavior, IFormFieldProvider)


class IWidthBehavior(IVariantAspect):
    """Width variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['width'])

    width = schema.TextLine(
        title=_(u'width_title', default=u'Width'),
        description=_(u'width_description',
                      default=u'Width of the product'),
        required=False)


alsoProvides(IWidthBehavior, IFormFieldProvider)


class IHeightBehavior(IVariantAspect):
    """Height variant behavior.
    """
    form.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['height'])

    height = schema.TextLine(
        title=_(u'height_title', default=u'Height'),
        description=_(u'height_description',
                      default=u'Height of the product'),
        required=False)


alsoProvides(IHeightBehavior, IFormFieldProvider)
