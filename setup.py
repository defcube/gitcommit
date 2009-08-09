from distutils.core import setup
import __init__

setup(name='GitCommit',
      version=__init__.get_version(),
      author_email='gattster@gmail.com',
      author='Philip Gatt',
      py_modules=['gitcommitlib'],
      scripts=['scripts/gitcommit'])
