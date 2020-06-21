
from distutils.core import setup
setup(
  name = 'dfin',         
  packages = ['dfin'],  
  version = '0.1',      
  license='MIT',       
  description = 'A simple Package to get Stock Details',   
  author = 'Davis Raimon',                   
  author_email = 'davisraimon@gmail.com',      
  url = 'https://github.com/davisraimon/dfin',   
  download_url = 'https://github.com/davisraimon/dfin/blob/master/dist/dfin-0.1.tar.gz',    
  keywords = ['Finance', 'stock', 'share'],   
  install_requires=[            
          'yfinance',
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
