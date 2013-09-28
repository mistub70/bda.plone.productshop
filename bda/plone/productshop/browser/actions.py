from zope.i18nmessageid import MessageFactory
from Products.Five.browser import BrowserView
from collective.instancebehavior import (
    instance_behaviors_of,
    enable_behaviors,
    disable_behaviors,
)


_ = MessageFactory('bda.plone.productshop')


class VariantAspectAction(BrowserView):
    aspect_title = None
    aspect_behavior = None

    def enable_aspect(self):
        enable_behaviors(self.context, [self.aspect_behavior], [])
        self.context.plone_utils.addPortalMessage(
            _(u'enabled_aspect',
              default=u'Added ${aspect} to object.',
              mapping={'aspect': self.aspect_title}))
        self.request.response.redirect(self.context.absolute_url())

    def disable_aspect(self):
        disable_behaviors(self.context, [self.aspect_behavior], [])
        self.context.plone_utils.addPortalMessage(
            _(u'disabled_aspect',
              default=u'Removed ${aspect} from object.',
              mapping={'aspect': self.aspect_title}))
        self.request.response.redirect(self.context.absolute_url())

    def can_enable(self):
        return not self.aspect_behavior in instance_behaviors_of(self.context)

    def can_disable(self):
        return self.aspect_behavior in instance_behaviors_of(self.context)


class ColorAction(VariantAspectAction):
    aspect_title = _(u'aspect_color', default=u'Color')
    aspect_behavior = 'bda.plone.productshop.behaviors.IColorBehavior'


class WeightAction(VariantAspectAction):
    aspect_title = _(u'aspect_weight', default=u'Weight')
    aspect_behavior = 'bda.plone.productshop.behaviors.IWeightBehavior'


class SizeAction(VariantAspectAction):
    aspect_title = _(u'aspect_size', default=u'Size')
    aspect_behavior = 'bda.plone.productshop.behaviors.ISizeBehavior'


class DemandAction(VariantAspectAction):
    aspect_title = _(u'aspect_demand', default=u'Demand')
    aspect_behavior = 'bda.plone.productshop.behaviors.IDemandBehavior'
