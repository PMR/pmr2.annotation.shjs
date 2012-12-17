import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from pmr2.app.exposure.interfaces import IExposureSourceAdapter
from pmr2.app.exposure.browser.browser import ExposureFileViewBase


class SourceTextNote(ExposureFileViewBase):
    """\
    The source text viewer class.
    """

    template = ViewPageTemplateFile('source_text.pt')
    title = ViewPageTemplateFile('source_title.pt')
    index = ViewPageTemplateFile('shjs_layout.pt')

    def portal_url(self):
        portal = getToolByName(self.context, 'portal_url').getPortalObject()
        return portal.absolute_url()
    
    @property
    def langtype(self):
        return self.note.langtype

    def content(self):
        a = zope.component.queryAdapter(self.context, IExposureSourceAdapter)
        if a:
            return a.file()
