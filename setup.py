from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='spindata',
      version='1.13',
      description='Gyromagnetic ratios, spin, and quadrupole moments (where applicable) of all elements and the electron.',
      classifiers=['License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Physics'],
      keywords='NMR spin nuclear magnetic resonance gyromagnetic ratio',
      url='http://github.com/bennomeier/spindata',
      author='Benno Meier',
      author_email='meier.benno@gmail.com',
      license='MIT',
      packages=['spindata'],
      include_package_data=True,
            install_requires = [
          'numpy',
          'scipy',
          ],
      zip_safe=False)

