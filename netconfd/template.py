from lxml import etree
from lxml.etree import XSLT
import os.path

class TemplateEngine(object):
    def __init__(self, *paths):
        '''
        Translator cache with prioritized overrides.
        '''
        self.paths = [os.path.abspath(x) for x in paths]
        self.reload_template()

    def translate(self, page):
        relpath = 'pages/%s.xml' % page
        return self.translator.transform(self.get_file(relpath))

    def get_file(self, relpath):
        return retrieve(relpath, *self.paths)

    def reload_template(self):
        '''
        Compiles a big composite XSLT template from multiple sources
        '''
        self.translator = Template()
        for relpath in ('./global.xslt',):
            self.translator.include(self.get_file(relpath))
        self.translator.compile()


STYLESHEET_SKELETON = '''
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
</xsl:stylesheet>
'''

class Template(object):
    def __init__(self):
        self.root = etree.XML(STYLESHEET_SKELETON)
        self.xslt = None

    def include(self, filehandle):
        subtemplate = etree.parse(filehandle).getroot()
        self.root.append(subtemplate)

    def compile(self):
        if not self.xslt:
            self.recompile()

    def recompile(self):
        self.xslt = XSLT(self.root)

    def transform(self, source):
        self.compile()
        source_root = etree.parse(source).getroot()
        return self.xslt(source_root)

def walk(*paths):
    '''
    Get a list of all relative paths available from any of the paths
    in a set of paths (only has to be available in one).
    '''
    results = set()
    def append_results(root, dirname, fnames, results):
        reldir = os.path.relpath(dirname, root)
        for fname in fnames:
            results.add(os.path.join(reldir, fname))
    append_dir = lambda arg, dirname, fnames: append_results(arg, dirname, fnames, results)
    for path in paths:
        path = os.path.abspath(path)
        os.path.walk(path, append_dir, path)
    return results

def retrieve(relpath, *paths):
    '''
    Find the first openable file for a relpath in a set of root paths.
    '''
    for path in paths:
        try:
            fullpath = os.path.join(path, relpath)
            print "Trying to open", fullpath
            return open(fullpath)
        except:
            pass
    raise ValueError("File not found")
