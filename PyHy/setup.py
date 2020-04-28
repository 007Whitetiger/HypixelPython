
from distutils.core import setup
setup(
  name = 'HyPython',
  packages = ['YOURPACKAGENAME'],
  version = '0.1',
  license='MIT',
  description = 'TYPE YOUR DESCRIPTION HERE',
  author = 'Stijn Te Baerts',
  author_email = 'developer.whitetiger@gmail.com',
  url = 'https://github.com/007Whitetiger/HyPy',
  download_url = 'https://github.com/007Whitetiger/HyPy/archive/v_0.1.tar.gz',
  keywords = ['Hypixel', 'Api', 'ApiWrapper'],
  install_requires=[
          'requests',
          ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)