import json
import random

import settings


class Selector:

    def __init__(
        self,
        json_path=settings.RESOURCE_JSON_PATH,
    ):

        self._json_path = json_path

    def select(self):
        with open(self._json_path, 'r') as f:
            raw_data = f.read()

        data = json.loads(raw_data)
        picked = random.choice(data['movies'])

        url = picked['url']
        title = picked['title']
        yyyymmdd = picked['yyyymmdd']

        s = (
            '\n'
            '===============================================\n'
            'スーパーサンクスできるよ！コメントしよっ！！\n'
            '-----------------------------------------------\n'
            f'{title}'
            f' ({yyyymmdd})\n'
            f'{url}\n'
            '===============================================\n'
        )
        return s


if __name__ == '__main__':
    cls = Selector()
    result = cls.select()
    print(result)
