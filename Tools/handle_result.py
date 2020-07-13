# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/13 15:21
"""

from deepdiff import DeepDiff


def handle_result_json(dict1, dict2):
    '''
    校验格式
    '''
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == "__main__":
    dict2 = {'code': 200, 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTRlZTUxZjEwOTVhZDUzODAxMjAzODg0MTFkNzU3ZTk3MjFiNDExNGZlYjUxZDA3NzlkYWZiZjQyNjZlNGQwNjQxOTY4MzI4MWQ2MGMyMmIiLCJpYXQiOjE1OTQ2MjE4NzksIm5iZiI6MTU5NDYyMTg3OSwiZXhwIjoxNTk0NjIxOTM5LCJzdWIiOiI2MDgwMDExMjAiLCJpc3MiOiJzYW5qaWVrZS1wcmUiLCJzaWQiOiJlNGVlNTFmMTA5NWFkNTM4MDEyMDM4ODQxMWQ3NTdlOTcyMWI0MTE0ZmViNTFkMDc3OWRhZmJmNDI2NmU0ZDA2NDE5NjgzMjgxZDYwYzIyYiIsInNjb3BlcyI6W119.Q5v7FFHq2DiVFr7xrbfWHdfpVvfZ35edYJxkUJ_hn7l1Rtv79JUPk6ZZSC17JyVjqiF1wbdDp3hfWP6QJgtHjg'}, 'msg': 'ok'}
    dict1 = {'code': 201, 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZTRlZTUxZjEwOTVhZDUzODAxMjAzODg0MTFkNzU3ZTk3MjFiNDExNGZlYjUxZDA3NzlkYWZiZjQyNjZlNGQwNjQxOTY4MzI4MWQ2MGMyMmIiLCJpYXQiOjE1OTQ2MjE4NzksIm5iZiI6MTU5NDYyMTg3OSwiZXhwIjoxNTk0NjIxOTM5LCJzdWIiOiI2MDgwMDExMjAiLCJpc3MiOiJzYW5qaWVrZS1wcmUiLCJzaWQiOiJlNGVlNTFmMTA5NWFkNTM4MDEyMDM4ODQxMWQ3NTdlOTcyMWI0MTE0ZmViNTFkMDc3OWRhZmJmNDI2NmU0ZDA2NDE5NjgzMjgxZDYwYzIyYiIsInNjb3BlcyI6W119.'}, 'msg': 'true'}
    print(handle_result_json(dict1,dict2))
