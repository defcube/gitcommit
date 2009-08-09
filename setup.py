from distutils.core import setup
import gitcommitlib

setup(name='GitCommit',
      version=gitcommitlib.get_version(),
      author_email='gattster@gmail.com',
      author='Philip Gatt',
      py_modules=['gitcommitlib'],
      scripts=['scripts/gitcommit'])
