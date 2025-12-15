#!/bin/bash
# syntax_error_example.sh

# 1. コマンドのタイプミス → コマンドが存在しない
eccho "Hello, world!"  # 正しくは echo

# 2. 未定義変数を使う（set -u を有効にするとエラーになる）
echo "Value is $UNDEFINED_VAR"

# 3. if 文の構文ミス
if [ 1 -eq 1 ] ; then  # then がない → syntax error
  echo "Numbers are equal"
fi

# 4. 閉じないクォート
echo "This string is not closed"

# 5. 関数の定義ミス
myfunc() {        # 関数は } で閉じる必要がある
  echo "Hello"
}
# 閉じてない