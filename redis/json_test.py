import json


str1 = '{"name":"Dave", "age":"29", "height":180, "weight":65}'
j = json.loads(str1)
print(j)
print(type(j))


j2 = {'name':'Dave', 'age':29, 'height':180, 'weight':65}
str2 =json.dumps(j2)
print(str2)
print(type(str2))