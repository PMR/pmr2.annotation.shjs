import zope.interface
import zope.component
from zope.schema import fieldproperty

from pmr2.app.interfaces import *
from pmr2.app.annotation.note import RawTextNote
from pmr2.app.annotation.note import ExposureFileNoteBase
from pmr2.app.annotation.note import ExposureFileEditableNoteBase

from interfaces import *

class SourceTextNote(ExposureFileEditableNoteBase):
    """\
    Points to the OpenCell session attached to this file.
    """

    zope.interface.implements(ISourceTextNote)
    langtype = fieldproperty.FieldProperty(ISourceTextNote['langtype'])
