"""
Tree datastructure
"""

from stanza.models.common.doc import StanzaObject

class Tree(StanzaObject):
    """
    A data structure to represent a parse tree
    """
    def __init__(self, label=None, children=None):
        if children is None:
            self.children = []
        elif isinstance(children, Tree):
            self.children = (children,)
        else:
            self.children = children

        self.label = label

    def is_leaf(self):
        return len(self.children) == 0

    def is_preterminal(self):
        return len(self.children) == 1 and len(self.children[0].children) == 0

    def yield_preterminals(self):
        if self.is_leaf():
            pass
        elif self.is_preterminal():
            yield self
        else:
            for child in self.children:
                for preterminal in child.yield_preterminals():
                    yield preterminal

    def __repr__(self):
        if not self.children:
            return str(self.label)
        else:
            pieces = [str(self.label)] + [str(x) for x in self.children]
            return "(" + " ".join(pieces) + ")"

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Tree):
            return False
        if self.label != other.label:
            return False
        if self.children != other.children:
            return False
        return True
