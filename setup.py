from setuptools import setup, find_packages


setup(
    name='gym_d2d',
    version='0.1.0',
    description='Device-to-Device (D2D) communication OpenAI Gym environment',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['gym>=0.9.6', 'numpy'],
    extras_require={
        'dev': ['pytest', 'pytest-cov', 'pytest-sugar']
    },
    clasifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
