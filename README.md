# これは何?

バイナリのバイト列をC言語の配列に変換するやつ。

CA証明書をC言語の配列に変換したいときに便利。


# 動作環境

Python 3.x


# 使い方

1. `SCRoot2ca.cer`のようなCA証明書を`input.txt`にリネームする
1. `python main.py`を実行する
1. `output.txt`に、C言語の配列になったやつが生成される

## 例
`input.txt`の中身を見てほしい。これが`output.txt`に変換される。