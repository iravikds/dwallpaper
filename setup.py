from setuptools import setup, find_packages

setup(
    name='dwallpaper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'dwallpaper=dwallpaper.main:main',
        ],
    },
)
