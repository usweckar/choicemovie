import csv
import json

import settings


class Converter:

    def __init__(
        self,
        csv_path=settings.RESOURCE_CSV_PATH,
        json_path=settings.RESOURCE_JSON_PATH,
    ):

        self._csv_path = csv_path
        self._json_path = json_path

    def save(self):
        dict_data = self._make_dict()
        json_data = self._csv_to_json(dict_data)
        self._update_json(json_data)
        return

    def _make_dict(self):
        lines = []
        with open(self._csv_path, 'r') as f:
            for line in csv.DictReader(f):
                lines.append(line)

        data = {'movies': lines}
        return data

    def _csv_to_json(self, data):
        result = json.dumps(data, indent=2, ensure_ascii=False)
        return result

    def _update_json(self, data):
        with open(self._json_path, 'w') as f:
            f.write(data)
        return


if __name__ == '__main__':
    cls = Converter()
    cls.save()
