"""Tests for common utility functions."""

import pytest

from abctools.utils import get_target_file, title_parser


param = pytest.param


@pytest.mark.parametrize(
    'target, expect',
    (
        param(
            'folder/foo.abc',
            ['folder/foo.abc'],
            id='it-ids-single-file'
        ),
        param(
            'folder',
            [
                'folder/foo.abc',
                'folder/bar.abc',
                'folder/sub/baz.abc',
                'folder/quix.dsfa'
            ],
            id='it-ids-a-folderful'
        ),
    )
)
def test_list_target_files(tmp_path, target, expect):
    (tmp_path / 'folder/sub').mkdir(parents=True)
    for _file in expect:
        (tmp_path / _file).touch()
    result = list(get_target_file(tmp_path / target))
    assert result == [tmp_path / e for e in expect if e.endswith('.abc')]


@pytest.mark.parametrize(
    'text, expect',
    (
        ('fenwick o\' bywell', 'Fenwick o\' Bywell'),
    )
)
def test_title_parser(text, expect):
    