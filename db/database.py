import databases
from dynaconf import settings

from db.models import create_database_url


DATABASE_URL = create_database_url()
database = databases.Database(
    DATABASE_URL,
    min_size=settings.DB_CONN_MIN_SIZE,
    max_size=settings.DB_CONN_MAX_SIZE,
    max_inactive_connection_lifetime=settings.DB_CONN_MAX_LIFETIME,
)