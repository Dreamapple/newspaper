import newspaper

url = 'https://segmentfault.com/a/1190000000349555'
a=newspaper.Article(url)
a.download()
a.parse()
print(a.text)