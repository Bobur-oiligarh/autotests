from utils.api_utils.url_provider import URLProvider


class Credentials:
    DB_USER = "postgres"
    DB_PASSWORD = "XqDKJj5KuUkB"
    DB_PATH = URLProvider().db_url()
    DB_CREDS_BASE = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_PATH}/%s"



