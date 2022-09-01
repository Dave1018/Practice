import redis 

#r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.Redis.__new__
r.set('key1', "value1")
print(r['key1'])
print(r.get('key1'))
print(type(r.get('key1')))
