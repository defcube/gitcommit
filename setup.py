from distutils.core import setup
import gitcommitlib

setup(name='GitCommit',
      version=gitcommitlib.get_version(),
      author_email='gattster@gmail.com',
      author='Philip Gatt',
      py_modules=['gitcommitlib'],
      scripts=['scripts/gitcommit', 'scripts/safe_git'],
      description='GitCommit is a free Python based script that does a few checks before running "git commit -av". Checks include running django unit tests and checking for TODO statements. To contribute, visit http://github.com/defcube/gitcommit/',
      )
