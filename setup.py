from setuptools import setup



setup(

    name='montecarlo',

    version='1.0.0',

    url='https://github.com/mahgan/mg4ccz_ds5100_montecarlo',

    author='Mahin Ganesan',

    author_email='mg4ccz@virginia.edu',

    description='Package contains modules Montecarlo and Montecarlo_test which creates a Die, Game, and Analyzer class that computes analytics for die rolls within games with user-specified parameters and tests it.',

    license='MIT',

    packages=['montecarlo'],    

    install_requires=['pandas','numpy', 'unittest','matplotlib']

)