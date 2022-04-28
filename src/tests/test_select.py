import pytest


class TestSelector:

    @pytest.fixture
    def target(self):
        from selector import Selector
        return Selector()

    def test_save(self, target):
        target._json_path = './src/tests/resources/movies.json'

        # act
        actual = target.select()

        expected_1 = (
            '\n'
            '===============================================\n'
            '動画みてっ！スーパーサンクスしよっ！！\n'
            '-----------------------------------------------\n'
            '動画1 (2021/01/01)\n'
            'https://www.youtube.com/watch?v=aaa\n'
            '===============================================\n'
        )
        expected_2 = (
            '\n'
            '===============================================\n'
            '動画みてっ！スーパーサンクスしよっ！！\n'
            '-----------------------------------------------\n'
            '動画2 (2021/12/31)\n'
            'https://www.youtube.com/watch?v=bbb\n'
            '===============================================\n'
        )

        # assert
        assert actual in [expected_1, expected_2]
