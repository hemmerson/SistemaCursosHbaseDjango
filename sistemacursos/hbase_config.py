import happybase
from django.conf import settings

def get_hbase_connection():
    connection = happybase.Connection(
        host=settings.HBASE_HOST,
        port=settings.HBASE_PORT
    )