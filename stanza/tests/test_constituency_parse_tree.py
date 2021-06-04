import pytest

from stanza.models.constituency.parse_tree import Tree

from stanza.tests import *

pytestmark = [pytest.mark.pipeline, pytest.mark.travis]

def test_leaf_preterminal():
    foo = Tree(label="foo")
    assert foo.is_leaf()
    assert not foo.is_preterminal()
    assert len(foo.children) == 0

    bar = Tree(label="bar", children=foo)
    assert not bar.is_leaf()
    assert bar.is_preterminal()
    assert len(bar.children) == 1

    baz = Tree(label="baz", children=[bar])
    assert not baz.is_leaf()
    assert not baz.is_preterminal()
    assert len(baz.children) == 1
