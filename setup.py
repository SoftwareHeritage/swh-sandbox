from setuptools import setup, find_packages

setup(
    name='swh-sandbox',
    description='Sandbox project',
    version='0.0.1',
    author='Software Heritage developers',
    author_email='swh-devel@inria.fr',
    url='https://forge.softwareheritage.org/source/sandbox',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # noqa
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    project_urls={
        'Bug Reports': 'https://forge.softwareheritage.org/maniphest',
        'Funding': 'https://www.softwareheritage.org/donate',
        'Source': 'https://forge.softwareheritage.org/source/sandbox',
    },
)
