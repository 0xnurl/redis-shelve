# Redis Shelve
### Alternative to Python shelve that uses Redis as a backend

* Writes to Redis instead of local file
* Faster than disk-bound shelve
* Works better for multiprocessing use cases 


#### Usage

Same as in `https://docs.python.org/3/library/shelve.html`

```

import redis_shelve as shelve
 
d = shelve.open(table_name)
 
d[key] = data
 
data = d[key]
 
del d[key]

```

#### TODO
* Support `__len__` and `__iter__`