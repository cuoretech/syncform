import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'transaction',
    'pyramid_tm',
    'py2neo',
    'pyramid_mailer'
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
      author='Leo Schultz and Kevin Aloysius',
      author_email='leo@cuore.io',
      url='http://www.cuore.io',
      keywords='Cuore SyncForm Coordination Efficiency Platform',
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
