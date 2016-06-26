import newspaper
import logging

logging.basicConfig(level=logging.DEBUG,

                    format='level:%(levelname)s file: %(filename)s '

                           'line: [%(lineno)d]  output msg:  %(message)s'

                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]',)
url = 'https://segmentfault.com/a/1190000000349555'
a=newspaper.Article(url)
a.download()
a.parse()
print(a.text)