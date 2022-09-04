import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=1)

p1 = {'name':'Dave', 'city':'taipei', 'age':29}
p2 = {'name':'Leo', 'city' : 'yilan', 'age' :25}
plist = [p1, p2]

for p in plist:
    r.lpush('list1',json.dumps(p))

print('list1 length = ' + str(r.llen('list1')))

while(r.llen('list1') != 0):
    s2 = r.rpop('list1')
    j2= json.loads(s2)
    print(j2)
    print('list1 length = ' + str(r.llen('list1')))





