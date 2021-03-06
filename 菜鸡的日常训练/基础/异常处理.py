from diskcache import Cache

cache = Cache()
with Cache(cache.directory) as reference:
    reference.set('key','value12')
    print(reference.get('key'))