import redis
r = redis.StrictRedis()
r.set('foo', 'bar')
print r.get('foo')
