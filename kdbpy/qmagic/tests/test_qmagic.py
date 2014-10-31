import os
import inspect
from contextlib import contextmanager
from kdbpy import qmagic
from runipy.notebook_runner import NotebookRunner
from IPython.nbformat.current import read


@contextmanager
def cd(path):
    curdir = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(curdir)


def test_qmagic_notebook():
    path = os.path.dirname(inspect.getfile(qmagic))
    with cd(path):
        with open('qmagic.ipynb') as f:
            notebook = read(f, 'json')
        r = NotebookRunner(notebook)
        assert os.getcwd() == path
        r.run_notebook()
