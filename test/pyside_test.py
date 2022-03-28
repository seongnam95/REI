
from urllib import parse

val = '%BA%C0%BF%EC%C0%E7%B7%CE+154'
data = parse.unquote(val)
data = data.encode('utf-8')
data = data.decode('unicode_escape')

print(data)
