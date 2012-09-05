import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from pmr2.app.exposure.interfaces import IExposureSourceAdapter
from pmr2.app.exposure.browser.browser import ExposureFileViewBase


class SourceTextNote(ExposureFileViewBase):
    """\
    The source text viewer class.
    """

    template = ViewPageTemplateFile('source_text.pt')
    title = ViewPageTemplateFile('source_title.pt')
    index = ViewPageTemplateFile('shjs_layout.pt')
    
    @property
    def langtype(self):
        return self.note.langtype

    def content(self):
        a = zope.component.queryAdapter(self.context, IExposureSourceAdapter)
        if a:
            return a.file()
