# CentOS7.0でPyenvでのPython3.6.1環境構築
## 環境まとめ
* OS:CentOS7.0(vagrant)

## 手順
1. VirtualBoxのインストール
1. Vagrantのインストール
1. Vagrantの起動
1. SSHクライアントで仮想マシンにログインする
1. ホストマシンと仮想マシンでフォルダを共有する
1. gitのインストール
1. pythonのコンパイル時に必要なパッケージのインストール
1. Pyenvのインストール
1. Pyenv-virtualenvのインストール
1. Pythonのインストール
1. pipのインストール

## VirtualBoxのインストール
[VirtualBox_DL](https://www.virtualbox.org/wiki/Downloads)
## Vagrantのインストール
[Vagrant_DL](https://www.vagrantup.com/downloads.html)
## Vagrantを追加
仮想マシンを作りたいディレクトリで以下のコマンドをコマンドプロンプトに入力

```shell
$ vagrant box add 【仮想マシン名】 【URL】
$ vagrant init 【仮想マシン名】
```
URL:http://www.vagrantbox.es/

vagrantfileが作成される

## Vagrantの起動
以下のコマンドをコマンドプロンプトに入力

```shell
$ vagrant up
```

## SSHクライアントで仮想マシンにログインする
以下のコマンドをコマンドプロンプトに入力

```shell
$ vagrant ssh
```

するとssh接続に必要な情報が出る

```
Host: 127.0.0.1
Port: 2222
Username: vagrant
Private key: C:/Users/【対象のディレクトリ】/.vagrant/machines/default/virtualbox/private_key
```

適当なSSHクラインアント([RLogin](http://nanno.dip.jp/softlib/man/rlogin/))で接続

## ホストマシンと仮想マシンでフォルダを共有する

ディレクトリ

```
/vagrant
```
で共有

-------------------ここからは、SSHクライアントでのコマンド-------------------------

## gitのインストール(入っている場合は大丈夫)

```shell
sudo yum install git
```

## Pyenvのインストール

```shell
$ sudo git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```

## bash_profileに環境変数を記述します。

```shell
$ vim .bash_profile
```
下記を追記


```shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## インストールできるバージョンを一覧表示

```shell
$ pyenv install --list
```

## Pythonのインストール
使用したいPythonのバージョンを指定(`.pyenv`でpermissionエラーが出たので、一時的に権限を変更)

```shell
$ pyenv install 3.6.1
$ pyenv global 3.6.1
$ pyenv rehash
$ python --version
$ pyenv versions
```

## pipのインストール

```shell
$ sudo yum install epel-release
$ sudo yum install python-pip
```

## 参考記事
* [Vagrant + VirtualBoxでWindows上に開発環境をサクッと構築する](http://qiita.com/ozawan/items/160728f7c6b10c73b97e)
* [PyenvによるPython3.x環境構築(CentOS, Ubuntu)](http://qiita.com/akito1986/items/be5dcd1a502aaf22010b)
* [自然言語処理を行う開発環境を設定する](http://qiita.com/woody-kawagoe/items/09c0f89a55701bcf72eb)
* [How to install pip on CentOS / RHEL / Ubuntu / Debian](http://sharadchhetri.com/2014/05/30/install-pip-centos-rhel-ubuntu-debian/)
