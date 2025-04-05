"""Generic utilities.
"""

from pathlib import Path


def get_target_file(target):
    """Check target path, return list of abc files"""
    target = Path(target)
    target.exists()
    if target.is_file():
        yield target
    else:
        for file_ in target.rglob('*.abc'):
            yield file_


def title_parser(
    func=str.capitalize,
    sep=" ",
    exceptions=['of', 'the', 'and', 'o\'', 'to'],
    replace={}
):
    """Parse a title into a given format
    
    Args:
        func: Function to apply to each word.
        sep: Word separator
        exceptions: Words not to run function on
        replace: substitutions
            (for example to avoid filenames like
            fenwick o' bywell.abc)
    """
