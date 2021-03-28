import memcache

db = memcache.Client(['memcached:11211'])
print(db.get("D0"))
print(db.get("D1"))
print(db.get("D2"))
print(db.get("D3"))
print(db.get("D4"))
print(db.get("D5"))
