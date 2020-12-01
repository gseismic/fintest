import os
from setuptools import setup, find_packages


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('fintest/')
setup(
    name='fintest', 
    version='0.1.0', 
    packages=find_packages(),
    description='finanical dataset for algorithm test',
    install_requires = ['arrow'],
    scripts=[],
    python_requires = '>=3.7',
    include_package_data=True,
    package_data={
        '': extra_files
    },
    author='Liu Shengli',
    url='https://github.com/gseismic/fintest',
    zip_safe=False,
    author_email='liushengli203@163.com'
)
