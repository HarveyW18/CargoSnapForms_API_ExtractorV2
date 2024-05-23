from setuptools import setup, find_packages

setup(
    name='CargoSnap_CSV_Extractor',
    version='1.0.0',
    description='A tool for extracting and exporting CargoSnap CSV data',
    author='Harvey W.',
    author_email='votre.email@example.com',
    url='https://github.com/harveyw18/CargoSnap_CSV_Extractor',
    packages=find_packages(where='Project'),
    package_dir={'': 'Project'},
    install_requires=[
        'tkcalendar',
        'customtkinter',
        'requests',
        'datetime',
    ],
    entry_points={
        'console_scripts': [
            'CargoSnap_CSV_Extractor=main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['Icon/*.ico'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
