#!/usr/bin/env python3

from pocket_comm import Pocket
import json

if __name__ == "__main__":
    pocket = Pocket()
    pocket.authenticate()
    param_since = 1293807600
    param_state='archive'
    param_sort='oldest'
    param_count=20000
    print(json.dumps({
      "since": param_since,
      "state": param_state,
      "sort": param_sort,
      "count": param_count
    }))
    pocket.retrieve(since=param_since, state=param_state, sort=param_sort, count=param_count)
