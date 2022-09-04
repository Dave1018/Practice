import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.set('name','Dave')
print(r.get('name'))

r.append('name',' and Hope')
print(r.get('name'))

print(r.strlen('name'))

print(r.getrange('name', 3, 10))



