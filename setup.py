# -*- coding: utf-8 -*-

import setuptools

def readme():
    with open('README.md', 'r') as fh:
        return fh.read()

setuptools.setup(
        name='xfce4_terminal_themes',
        version='0.1',
        author='Juan C. Müller',
        author_email='jcmuller@gmail.com',
        description='Manage your xfce4-terminal themes with ease!',
        long_description=readme(),
        long_description_content_type='text/markdown',
        url='https://github.com/jcmuller/xfce4-terminal-themes',
        packages=setuptools.find_packages(),
        install_requires=[],
        entry_points={
            'console_scripts': ['xfce4-terminal-themes=xfce4_terminal_themes.cli:main'],
            },
        test_suite='nose.collector',
        tests_require=['nose'],
        include_package_data=True,
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.7',
            'Topic :: Terminals',
            ],
        )
