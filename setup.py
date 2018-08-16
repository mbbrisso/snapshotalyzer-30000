from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='1.0',
    author="Robin Norwood",
    author_email="robin@acloud.guru",
    description="Snapshotalyzer 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    package=['shotty'],
    url="https://github.com/mbbrisso/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
