from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.utils import Condition

class PdbSection(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.condition = Condition(options.get('condition', 'python:False'),
                                   transmogrifier, name, options)
        self.previous = previous
        self.transmogrifier = transmogrifier
        self.context = transmogrifier.context

    def __iter__(self):
        for item in self.previous:
            if self.condition(item):
                import pdb; pdb.set_trace()
            yield item
