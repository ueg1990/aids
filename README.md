aids
===

Implementation of various algorithms, data structures, interview questions and challenges in Python.  


# Tests

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run all tests using nose,

    $ nosetests -v tests

To run all tests using nose and coverage,

    $ nosetests -v --with-coverage --cover-package=mooc_aggregator_restful_api --cover-inclusive --cover-erase tests

# PEP 8 Test

Whole project:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 * 

A specific file:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 <path_to_file> 

# Author

Usman Ehtesham Gul - <uehtesham90@gmail.com>
