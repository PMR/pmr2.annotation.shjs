import zope.interface
import zope.schema


class ISourceTextNote(zope.interface.Interface):
    """\
    Presents a syntax highlighted view of source text.
    """

    langtype = zope.schema.Choice(
        title=u'Session File',
        description=u'The session file that is made for this file.',
        #vocabulary='shjs',
        values=[u'c', u'cpp', u'xml', u'html'],
        default=u'xml',
    )
