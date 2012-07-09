from lxml import etree
from lxml.etree import XSLT
import os.path

class TemplateEngine(object):
    def __init__(self, *paths):
        '''
        Translator cache with prioritized overrides.
        '''
        self.paths = list(paths)
        self.cache = {}

    def translate(self, tmpl_relpath, source_relpath):
        translator = self.document(tmpl_relpath)
        source = self.document(source_relpath)
        translator = XSLT(translator)
        return translator.translate(source)

    def document(self, relpath):
        if relpath in self.cache:
            return self.cache[relpath]
        for path in self.paths.reverse():
            path = os.path.join(path, relpath)
            try:
                data = etree.parse(open(relpath))
                self.cache[relpath] = data
                return data
            except:
                pass
        raise Exception('Document not found: '+relpath)
