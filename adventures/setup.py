from setuptools import setup

setup(
    name='Adventure_Game',
    version='1.3',
    packages=['adventures files', 'lilypod_dodge/resources'],

    license='MIT',
    long_description='adventure game',
    install_requires=[
                    'pygame',
                     ],
    include_package_data = True,
    author = 'Hakim Hamaili',
    author_email = 'hakimboum406@gmail.com',
    url='https://github.com/hakimm77/Adventure-Game'
)
