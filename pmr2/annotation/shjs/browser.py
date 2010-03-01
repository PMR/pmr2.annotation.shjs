import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from plone.z3cform import layout

from pmr2.app.interfaces import IExposureSourceAdapter
from pmr2.app.browser.exposure import ExposureFileViewBase

from pmr2.annotation.shjs.layout import ShjsLayoutWrapper


class SourceTextNote(ExposureFileViewBase):
    """\
    The source text viewer class.
    """

    template = ViewPageTemplateFile('source_text.pt')

    def source(self):
        a = zope.component.queryAdapter(self.context, IExposureSourceAdapter)
        if a:
            return a.file()

SourceTextNoteView = layout.wrap_form(SourceTextNote, 
    __wrapper_class=ShjsLayoutWrapper)
