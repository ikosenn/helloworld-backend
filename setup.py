from setuptools import setup, find_packages

name = 'helloworld-backend'
version = '0.0.1'


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A Techie Blog!",
    long_description=open('README.md').read(),
    author="@yoda-yoda, @ikosenn",
    author_email="dee.caranja@gmail.com, ikosenn@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status ::',
        'Intended Audience :: Techies and Techies wannabe',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'django==1.8.5',
        'psycopg2==2.6.1',
        'djangorestframework==3.2.4',
        'djangorestframework-camel-case==0.2.0'
    ],
    scripts=[
        'bin/helloworld_manage',
    ],
    include_package_data=True
)
