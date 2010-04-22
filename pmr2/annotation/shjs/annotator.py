import zope.interface
import zope.component

from pmr2.app.factory import named_factory
from pmr2.app.annotation.interfaces import *
from pmr2.app.annotation.annotator import ExposureFileAnnotatorBase

from pmr2.annotation.shjs.interfaces import ISourceTextNote


class SourceTextAnnotator(ExposureFileAnnotatorBase):
    zope.interface.implements(IExposureFileAnnotator, 
                              IExposureFileEditAnnotator)
    title = u'Source Viewer'
    label = u'Source View'
    for_interface = ISourceTextNote

    def generate(self):
        return ()

SourceTextAnnotatorFactory = named_factory(SourceTextAnnotator)
