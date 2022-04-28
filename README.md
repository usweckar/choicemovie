# choicemovie

推し活の一環です。

## env

```console
$ python3 -V
Python 3.7.3
$ cd choicemovie
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

## run

csvファイルを元にjsonファイルを作成

```console
$ python3 src/converter.py
```

jsonファイルを元にランダムで動画を1つ選択

```console
$ python3 src/selector.py
```

## test

```console
$ . venv/bin/activate
(venv) $ pytest src
```
