from setuptools import find_packages, setup

setup(
    name="drfdocs",
    version=__import__('rest_framework_docs').__version__,
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=find_packages(),
    include_package_data=True,
    url="http://www.drfdocs.com",
    license='BSD',
    description="Documentation for Web APIs made with Django Rest Framework.",
    long_description=open("README.md").read(),
    install_requires=['Django==1.10.1', 'djangorestframework==3.4.6',
        'coverage==4.2', 'flake8<3.0.0', 'mkdocs==0.15.3', 'docutils==0.12',
        'django-markwhat==1.5'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)
