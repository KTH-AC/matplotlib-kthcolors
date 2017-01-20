
from setuptools import setup
setup(
  name = 'kthcolors',
  packages = ['kthcolors'], # this must be the same as the name above
  version = '0.0.2',
  classifiers=[
          "License :: OSI Approved :: MIT",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Geometry",
      ],
  description = 'Collection of KTH colors for matplotlib',
  author = 'Antonio Adaldo',
  author_email = 'anntonio.adaldo.89@gmail.com',
  url = 'https://github.com/adaldo/matplotlib-kthcolors', # use the URL to the github repo
  download_url = 'https://github.com/adaldo/matplotlib-kthcolors/tarball/0.0.1', # I'll explain this in a second
  keywords = ['plot', 'matplotlib', 'colors', 'kth'], # arbitrary keywords
)
