from setuptools import setup

requirements = []

with open('requirements.txt') as req_file:
    for req in req_file.readlines():
        requirements.append(req.strip())

setup(
    version='0.1',
    name='api_exercise_sergioperez',
    author='Sergio Perez',
    author_email='sergio@codefin.me',
    packages=["apiclient", "tests", "tests.apiclient", "tests.util", "util"],
    include_package_data=True,
    url="www.codefin.me",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run = run:main' 
        ],
    },
    description='Client library and runner to integrate with a fictitious API',
    long_description=open('README.md').read(),
)
