import json
from redis import Redis
from .settings import REDIS_HOST, REDIS_PORT


redis_store = Redis(host=REDIS_HOST, port=REDIS_PORT)

caches = {
    'local': {},
    'redis': redis_store,
}


def local_cache(f, key_prefix=None):
    cache = caches['local']

    def inner(*args, **kwargs):
        nonlocal key_prefix

        key_prefix = key_prefix or f.__name__
        key = '{}_{}'.format(
            key_prefix,
            hash(tuple([f.__name__] + list(args) + list(kwargs.items()))))

        if key not in cache:
            result = f(*args, **kwargs)
            cache[key] = result

        return cache[key]

    return inner


def redis_cache(f, key_prefix=None, ttl=24 * 60 * 60):
    def inner(*args, **kwargs):
        nonlocal key_prefix

        cache = caches['redis']
        key_prefix = key_prefix or f.__name__

        key = hash(args + tuple(kwargs.items()))
        prefixed_key = f'{key_prefix}_{key}'

        cached_result = cache.get(prefixed_key)

        if cached_result is not None:
            return json.loads(cached_result)

        result = f(*args, **kwargs)
        cache.set(prefixed_key, json.dumps(result), ttl)

        return result

    return inner
