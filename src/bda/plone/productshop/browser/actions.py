from zope.i18nmessageid import MessageFactory
from Products.Five.browser import BrowserView
from collective.instancebehavior import (
    instance_behaviors_of,
    enable_behaviors,
    disable_behaviors,
)
from ..behaviors import (
    IColorBehavior,
    IWeightBehavior,
    ISizeBehavior,
    IDemandBehavior,
    ILengthBehavior,
    IWidthBehavior,
    IHeightBehavior,
)
from ..interfaces import IVariant


_ = MessageFactory('bda.plone.productshop')


class VariantAspectAction(BrowserView):
    aspect_title = None
    aspect_behavior = None
    aspect_schema = None

    def enable_aspect(self):
        enable_behaviors(self.context,
                         (self.aspect_behavior,),
                         (self.aspect_schema,))
        self.context.plone_utils.addPortalMessage(
            _(u'enabled_aspect',
              default=u'Added ${aspect} to object.',
              mapping={'aspect': self.aspect_title}))
        self.request.response.redirect(self.context.absolute_url())

    def disable_aspect(self):
        disable_behaviors(self.context,
                          (self.aspect_behavior,),
                          (self.aspect_schema,))
        self.context.plone_utils.addPortalMessage(
            _(u'disabled_aspect',
              default=u'Removed ${aspect} from object.',
              mapping={'aspect': self.aspect_title}))
        self.request.response.redirect(self.context.absolute_url())

    def can_enable(self):
        return not self.aspect_schema.providedBy(self.context) \
            and IVariant.providedBy(self.context)

    def can_disable(self):
        return self.aspect_schema.providedBy(self.context)


class ColorAction(VariantAspectAction):
    aspect_title = _(u'aspect_color', default=u'Color')
    aspect_behavior = 'bda.plone.productshop.behaviors.IColorBehavior'
    aspect_schema = IColorBehavior


class WeightAction(VariantAspectAction):
    aspect_title = _(u'aspect_weight', default=u'Weight')
    aspect_behavior = 'bda.plone.productshop.behaviors.IWeightBehavior'
    aspect_schema = IWeightBehavior


class SizeAction(VariantAspectAction):
    aspect_title = _(u'aspect_size', default=u'Size')
    aspect_behavior = 'bda.plone.productshop.behaviors.ISizeBehavior'
    aspect_schema = ISizeBehavior


class DemandAction(VariantAspectAction):
    aspect_title = _(u'aspect_demand', default=u'Demand')
    aspect_behavior = 'bda.plone.productshop.behaviors.IDemandBehavior'
    aspect_schema = IDemandBehavior


class LengthAction(VariantAspectAction):
    aspect_title = _(u'aspect_length', default=u'Length')
    aspect_behavior = 'bda.plone.productshop.behaviors.ILengthBehavior'
    aspect_schema = ILengthBehavior


class WidthAction(VariantAspectAction):
    aspect_title = _(u'aspect_width', default=u'Width')
    aspect_behavior = 'bda.plone.productshop.behaviors.IWidthBehavior'
    aspect_schema = IWidthBehavior


class HeightAction(VariantAspectAction):
    aspect_title = _(u'aspect_height', default=u'Height')
    aspect_behavior = 'bda.plone.productshop.behaviors.IHeightBehavior'
    aspect_schema = IHeightBehavior
