import zope.interface
import zope.schema


class ISourceTextNote(zope.interface.Interface):
    """\
    Presents a syntax highlighted view of source text.
    """

    langtype = zope.schema.Choice(
        title=u'Language Type',
        description=u'The language of this file.',
        #vocabulary='shjs',
        values=[u'c', u'cpp', u'xml', u'html'],
        default=u'xml',
    )
