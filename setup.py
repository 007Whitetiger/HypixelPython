
from distutils.core import setup
setup(
  name = 'PyHy',
  packages = ['PyHy'],
  version = '0.1',
  license='MIT',
  description = f'Hypixel Api wrapper! For more info go to https://github.com/007Whitetiger/PyHy',
  author = 'Stijn Te Baerts',
  author_email = 'developer.whitetiger@gmail.com',
  url = 'https://github.com/007Whitetiger/PyHy',
  download_url = 'https://github.com/007Whitetiger/PyHy/archive/v0.1.1.tar.gz',
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