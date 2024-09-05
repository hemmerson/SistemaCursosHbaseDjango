import happybase
from django.conf import settings

_hbase_connection = None  # Variável global para armazenar a conexão

def get_hbase_connection():
    global _hbase_connection
    if _hbase_connection is None:
        _hbase_connection = happybase.Connection(
            host=settings.HBASE_HOST,
            port=settings.HBASE_PORT
        )
    return _hbase_connection

def close_hbase_connection():
    global _hbase_connection
    if _hbase_connection is not None:
        _hbase_connection.close()
        _hbase_connection = None