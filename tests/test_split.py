"""Tests for split"""

from textwrap import dedent

from abctools.split import _split, TuneData


def test__split():
    text = dedent("""
        %Some garbage
        x: 43
        T: foo
        adfa old other content

        X: 99
        t: Title2
        And another thing
    """)
    assert _split(text) == [
        TuneData(
            title='foo',
            tune='x: 43\n'
                 'T: foo\n'
                'adfa old other content\n'
                '\n',
            header=[
                    '\n'
                    '%Some garbage\n',
                ],
        ),
        TuneData(
            title='Title2',
            tune='X: 99\n'
                't: Title2\n'
                'And another thing\n',
            header=[
                    '\n'
                    '%Some garbage\n',
                ],
        ),
    ]

