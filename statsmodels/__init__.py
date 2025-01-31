
from statsmodels._version import get_versions

debug_warnings = False

print( "Here we go this is a local version for statsmodels..2." )
if debug_warnings:
    import warnings

    warnings.simplefilter("default")
    # use the following to raise an exception for debugging specific warnings
    # warnings.filterwarnings("error", message=".*integer.*")



def test(extra_args=None, exit=False):
    """
    Run the test suite

    Parameters
    ----------
    extra_args : list[str]
        List of argument to pass to pytest when running the test suite. The
        default is ['--tb=short', '--disable-pytest-warnings'].
    exit : bool
        Flag indicating whether the test runner should exist when finished.

    Returns
    -------
    int
        The status code from the test run if exit is False.
    """
    from .tools._testing import PytestTester
    tst = PytestTester(package_path=__file__)
    return tst(extra_args=extra_args, exit=exit)


__version__ = get_versions()['version']
del get_versions
