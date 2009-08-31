from distutils.core import setup
import gitcommitlib

setup(name='GitCommit',
      version=gitcommitlib.get_version(),
      author_email='gattster@gmail.com',
      author='Philip Gatt',
      py_modules=['gitcommitlib'],
      scripts=['scripts/gitcommit'],
      description='Does a few checks before running "git commit -av". Checks include running django unit tests and checking for #TODO statements',
      )
