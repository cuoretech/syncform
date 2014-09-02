import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
<<<<<<< HEAD
with open(os.path.join(here, 'README.md')) as f:
=======
with open(os.path.join(here, 'README.txt')) as f:
>>>>>>> 8f36627a1649aa4c0d660076b91943d33052eb73
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
<<<<<<< HEAD
    'transaction',
    'pyramid_tm',
    'py2neo',
    'pyramid_mailer'
=======
>>>>>>> 8f36627a1649aa4c0d660076b91943d33052eb73
    ]

setup(name='SyncForm',
      version='0.0',
      description='SyncForm',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
<<<<<<< HEAD
      author='Leo Schultz and Kevin Aloysius',
      author_email='leo@cuore.io',
      url='http://www.cuore.io',
      keywords='Cuore SyncForm Coordination Efficiency Platform',
=======
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
>>>>>>> 8f36627a1649aa4c0d660076b91943d33052eb73
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="syncform",
      entry_points="""\
      [paste.app_factory]
      main = syncform:main
      """,
      )
