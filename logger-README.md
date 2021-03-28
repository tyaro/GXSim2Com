# logger.py

Docker上のmemcachedにD0からD9600までの値を書き込みます。
memcache 上には "D0":D0の値 形式で書き込まれます。

Docker上のclientの中にあるmemcahe-client.pyで
Docker上からmemcached にアクセスして値をとることができます。