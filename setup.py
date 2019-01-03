import os
from setuptools import setup
from crypt4gh import __version__, __author__, __title__, __doc__ as lega_doc, __license__, PROG

here = os.path.dirname(__file__)
with open(os.path.join(here, 'requirements.txt')) as f:
    packages = f.readlines()

setup(name='crypt4gh',
      version=__version__,
      url='https://www.github.com/EGA-archive/crypt4gh',
      license=__license__,
      author=__author__,
      #author_email='frederic.haziza@crg.eu',
      description=__title__,
      long_description=lega_doc,
      packages=['crypt4gh'],
      include_package_data=False,
      package_data={ 'crypt4gh': ['completion.bash'] },
      zip_safe=False,
      entry_points={
          'console_scripts': [
              f'{PROG} = crypt4gh.__main__:main' ,
          ]
      },
      platforms = 'any',
      install_requires=packages,
)
