#!/bin/bash
# 読み込むファイル定義
FILENAME="./file/hightemp.txt"
# 配列定義
declare -a array=()
# ファイルの行数のcount
row_count=0;
# 一行づつ読み込む
while read LINE;
do
	# 整数演算を行う
	row_count=`expr $row_count + 1`
	# 一行の加工

	array+=($LINE)
done < $FILENAME
# 結果をコマンドラインに表示
echo $row_count
