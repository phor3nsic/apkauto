from os import path
from setuptools import setup, find_packages

main_dir = path.abspath(path.dirname(__file__))
install_requires = open(path.join(main_dir, "requirements.txt"), "r").readlines()

setup(
    name='apkauto',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    dependency_links=[
        "git+https://github.com/phor3nsic/resecrets",
        "git+https://github.com/kiber-io/apkd"
    ],
    entry_points={
        'console_scripts': [
            'apkauto=apkauto.main:main',
        ],
    },
    author='phor3nsic',
    author_email='phorensic@pm.me',
    description='Check secrets to all apk\'s version',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phor3nsic/apkauto',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
