import json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

print(json.loads(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])))

content = json.dumps({'errorcode': '0', 'msg': 'OK'})

errorcode = json.loads(content)

for key, value in errorcode.items():
    if key == 'errorcode':
        print(value)
# print(repr(errorcode))

print('end')
