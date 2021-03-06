import json
import zlib

import diskcache
from diskcache import Cache, UNKNOWN


class JSONDisk(diskcache.Disk):
    def __init__(self, directory, compress_level=1, **kwargs):
        self.compress_level = compress_level
        super(JSONDisk, self).__init__(directory, **kwargs)

    def put(self, key):
        json_bytes = json.dumps(key).encode('utf-8')
        data = zlib.compress(json_bytes, self.compress_level)
        return super(JSONDisk, self).put(data)

    def get(self, key, raw):
        data = super(JSONDisk, self).get(key, raw)
        return json.loads(zlib.decompress(data).decode('utf-8'))

    def store(self, value, read, key=UNKNOWN):
        if not read:
            json_bytes = json.dumps(value).encode('utf-8')
            value = zlib.compress(json_bytes, self.compress_level)
        return super(JSONDisk, self).store(value, read)

    def fetch(self, mode, filename, value, read):
        data = super(JSONDisk, self).fetch(mode, filename, value, read)
        if not read:
            data = json.loads(zlib.decompress(data).decode('utf-8'))
        return data


if __name__ == '__main__':
    jd=JSONDisk(directory='./leaf')
    jd.put({1:2})