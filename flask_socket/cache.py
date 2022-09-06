from flask_caching import Cache

config = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": '/etc/cache/',
    "CACHE_DEFAULT_TIMEOUT": 3600,
    "CACHE_THRESHOLD": 922337203685477580
}

cache_app = Cache(config=config)


def get_cache_value(cache_key):
    return cache_app.get(cache_key)


def set_cached_item(key, value, timeout=30 * 60):
    if value is None:
        return False

    cache_app.set(key, value, timeout=timeout)
    return True


def delete_cached_item(key):
    try:
        cache_app.delete(key)
        return True
    except Exception as exp:
        print(f"Error {exp} while deleting key {key}")
        return False

