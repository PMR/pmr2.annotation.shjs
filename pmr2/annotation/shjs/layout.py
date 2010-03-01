import os.path
import zope.interface

from plone.z3cform.templates import ZopeTwoFormTemplateFactory
from plone.z3cform.interfaces import IFormWrapper

from pmr2.app.browser.layout import FormWrapper


class IShjsLayoutWrapper(IFormWrapper):
    """
    The interface for the SHJS layout wrapper.
    """


path = lambda p: os.path.join(os.path.dirname(__file__), p)

shjs_layout_factory = ZopeTwoFormTemplateFactory(
    path('shjs_layout.pt'), form=IShjsLayoutWrapper)


class ShjsLayoutWrapper(FormWrapper):
    """\
    This layout wrapper provides XML stylesheet declarations for the
    rendering of MathML.
    """

    zope.interface.implements(IShjsLayoutWrapper)
