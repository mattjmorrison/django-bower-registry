from setuptools import setup, find_packages


setup(
    name='bower-registry',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': {
            "bower-server = registry.main:run",
        }
    },
    install_requires=file('requirements.txt').read().split("\n"),
)
