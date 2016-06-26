from setuptools import setup, find_packages

name = 'helloworld-backend'
version = '0.0.1b1'


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A Techie Blog!",
    long_description=open('README.rst').read(),
    url="https://helloworld.co.ke",
    author="@yoda-yoda, @ikosenn",
    author_email="dee.caranja@gmail.com, ikosenn@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status ::',
        'Intended Audience :: Techies and Techies wannabe',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'ansible==2.0.2',
        'gunicorn==19.5.0',
        'django==1.9.6',
        'psycopg2==2.6.1',
        'djangorestframework==3.3.3',
        'Pillow==3.2.0',
        'sarge==0.1.4',
        'Click==6.6',
        'dj_database_url==0.4.1',
        'django-oauth-toolkit==0.10.0',
        # 'django-rest-auth==0.7.0',
        'django-cors-headers==1.1.0',
        'ipython'
    ],
    scripts=[
        'bin/helloworld_manage',
        'bin/run'
    ],
    include_package_data=True
)
