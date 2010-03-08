import zope.interface
import zope.component

from pmr2.app.factory import named_factory
from pmr2.app.annotation.interfaces import *
from pmr2.app.annotation.annotator import ExposureFileAnnotatorBase


class SourceTextAnnotator(ExposureFileAnnotatorBase):
    zope.interface.implements(IExposureFileAnnotator)
    title = u'Source Viewer'
    label = u'Source View'

    def generate(self):
        return ()

SourceTextAnnotatorFactory = named_factory(SourceTextAnnotator)
