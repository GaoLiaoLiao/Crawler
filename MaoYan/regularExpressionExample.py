import re

content = 'oooooowww.google.com'
result = re.search('www\.google\.com', content)
print(result)


content2 = '<li data-view="2">lol</li>'
results = re.findall('<li.*?>(.*?)</li>', content2, re.S)
print(results)

