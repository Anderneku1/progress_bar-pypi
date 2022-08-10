from setuptools import setup, find_packages


setup(
    name='progress_bar',
    version='1.0',
    license='MIT',
    author="Chukuneku Nwanwene",
    author_email='chukunekunwanwene@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Anderneku1/progress_bar-pypi',
    keywords='progress bar',
    install_requires=[
          'time',
      ],

)
