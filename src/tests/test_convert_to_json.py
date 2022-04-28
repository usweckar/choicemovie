import pytest


class TestConvertToJson:

    @pytest.fixture
    def target(self):
        from convert_to_json import ConvertToJson
        return ConvertToJson()

    def test_save(self, target):
        import tempfile

        target._csv_path = './src/tests/resources/movies.csv'

        with tempfile.NamedTemporaryFile() as temp_f:
            target._json_path = temp_f.name

            # act
            target.save()

            with open(temp_f.name, 'r') as temp_read:
                actual = temp_read.read()

        expected = ''.join([
            '{\n',
            '  "movies": [\n',
            '    {\n',
            '      "url": "https://www.youtube.com/watch?v=aaa",\n',
            '      "title": "動画 \\"の\\", \\"タイトル\\" です",\n',
            '      "yyyymmdd": "2022/12/31"\n',
            '    },\n',
            '    {\n',
            '      "url": "https://www.youtube.com/watch?v=bbb",\n',
            '      "title": "どうがのタイトル",\n',
            '      "yyyymmdd": "2010/1/1"\n',
            '    }\n',
            '  ]\n',
            '}',
        ])

        # assert
        assert actual == expected

    def test__make_dict(self, target):
        from collections import OrderedDict

        target._csv_path = './src/tests/resources/movies.csv'

        # act
        actual = target._make_dict()

        expected = {
            'movies': [
                OrderedDict([
                    ('url', 'https://www.youtube.com/watch?v=aaa'),
                    ('title', '動画 "の", "タイトル" です'),
                    ('yyyymmdd', '2022/12/31'),
                ]),
                OrderedDict([
                    ('url', 'https://www.youtube.com/watch?v=bbb'),
                    ('title', 'どうがのタイトル'),
                    ('yyyymmdd', '2010/1/1'),
                ]),
            ],
        }

        # assert
        assert actual == expected

    def test__csv_to_json(self, target):
        from collections import OrderedDict

        data = {
            'movies': [
                OrderedDict([
                    ('url', 'https://www.youtube.com/watch?v=aaa'),
                    ('title', '動画 "の", "タイトル" です'),
                    ('yyyymmdd', '2022/12/31')
                ]),
                OrderedDict([
                    ('url', 'https://www.youtube.com/watch?v=bbb'),
                    ('title', 'どうがのタイトル'),
                    ('yyyymmdd', '2010/1/1')
                ]),
            ],
        }

        # act
        actual = target._csv_to_json(data)

        expected = ''.join([
            '{\n',
            '  "movies": [\n',
            '    {\n',
            '      "url": "https://www.youtube.com/watch?v=aaa",\n',
            '      "title": "動画 \\"の\\", \\"タイトル\\" です",\n',
            '      "yyyymmdd": "2022/12/31"\n',
            '    },\n',
            '    {\n',
            '      "url": "https://www.youtube.com/watch?v=bbb",\n',
            '      "title": "どうがのタイトル",\n',
            '      "yyyymmdd": "2010/1/1"\n',
            '    }\n',
            '  ]\n',
            '}',
        ])

        # assert
        assert actual == expected

    def test__update_json(self, target):
        import tempfile

        data = 'aaa\nbbb\n   ccc'

        with tempfile.NamedTemporaryFile() as temp_f:
            target._json_path = temp_f.name

            # act
            target._update_json(data)

            with open(temp_f.name, 'r') as temp_read:
                actual = temp_read.read()

        # assert
        assert actual == data
