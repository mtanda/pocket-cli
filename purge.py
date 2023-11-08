#!/usr/bin/env python3

from pocket_comm import Pocket
import time

if __name__ == "__main__":
    pocket = Pocket()
    pocket.authenticate()
    delete_until = 1698332400

    for i in range(10000):
      param_since = 1293807600
      param_state = 'archive'
      param_sort = 'oldest'
      param_count = 2000
      try:
        _, _, _, _, it = pocket.retrieve(since=param_since, state=param_state, sort=param_sort, count=param_count)
        items = list(it.values())
        items = list(filter(lambda x: x.time_added < delete_until, items))
        items = sorted(items, reverse=False, key=lambda x: x.time_added)
        item_id_lists = list(map(lambda x: x.item_id, items))

        time.sleep(1)
        try:
          print(f'try to remove, since={param_since}, from={items[0].time_added}, to={items[-1].time_added}')
          for item_id in item_id_lists:
            pocket.request_delete_batch(item_id)
          pocket.send_batched_requests()
          print(f'success, since={param_since}, from={items[0].time_added}, to={items[-1].time_added}')
          time.sleep(10)
          param_since = items[-1].time_added
        except:
          print('error, sleep 10')
          time.sleep(10)
          #pocket.authenticate()
      except:
        print('retrieve error, sleep 10')
        time.sleep(10)
        #pocket.authenticate()
