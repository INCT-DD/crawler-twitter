#!/usr/bin/env python

from distutils.core import setup

setup(name='crawler-twitter',
      version='0.0.1',
      description='Ferramenta de captura de dados brutos a partir da API do Twitter',
      author='Instituto Nacional de Ciência e Tecnologia em Democracia Digital',
      author_email='inctdd@ufba.br',
      url='http://inctdd.org',
      packages=['crawler-twitter'],
      install_requires=['logzero', 'flask'],
     )