import pickle
from redis import Redis


class RedisShelve:
    def __init__(self, shelve_name, pickle_protocol):
        self.shelve_name = shelve_name
        self.pickle_protocol = pickle_protocol if pickle_protocol is not None else -1
        self.redis = Redis()

    def close(self):
        pass

    def __getitem__(self, key):
        return pickle.loads(self.redis.get(self._get_redis_key(key)))

    def __setitem__(self, key, value):
        pickled_value = pickle.dumps(value, protocol=self.pickle_protocol)
        self.redis.set(self._get_redis_key(key), pickled_value)

    def __delitem__(self, key):
        self.redis.delete(self._get_redis_key(key))

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def _get_redis_key(self, key):
        return 'shelve_{}_key_{}'.format(self.shelve_name, key)


def open(filename, flag='c', protocol=None, writeback=False, *args, **kwargs):
    return RedisShelve(shelve_name=filename, pickle_protocol=protocol)
