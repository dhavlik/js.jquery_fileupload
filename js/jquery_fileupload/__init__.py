from fanstatic import Library, Resource

from js.jquery import jquery

library = Library('jquery_fileupload', 'resources')

jquery_fileupload = Resource(
    library, 'jquery.fileupload.js',
    depends=[jquery],
)
