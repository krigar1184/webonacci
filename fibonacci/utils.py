def local_cache(f):
    cache = {}

    def inner(*args, **kwargs):
        key = hash(tuple([f.__name__] + list(args) + list(kwargs.items())))

        if not key in cache:
            result = f(*args, **kwargs)
            cache[key] = result

        return cache[key]

    return inner
