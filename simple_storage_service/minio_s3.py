from minio.api import Minio

S3_SERVER = 'prep-os.hamkorbank.uz'
S3_ACCESS_KEY = '1WPRrvZCyWs3pzEo'
S3_SECRET_KEY = '2rqGCbmrJ80gfBlI3OhXVP1WzePBhPyA'


class MinioS3:

    def __init__(self, minio_server: str,
                 access_key: str = None,
                 secret_key: str = None,
                 secure: bool = False,
                 region=None,
                 http_client=None,
                 credentials=None
                 ):
        self.client = Minio(
            endpoint=minio_server,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
            region=region,
            http_client=http_client,
            credentials=credentials
        )

    def upload_object_to_bucket(self, bucket_name: str, object_name: str, file_path: str, **kwargs):
        found = self.client.bucket_exists(bucket_name)
        if not found:
            self.client.make_bucket(bucket_name)
        else:
            print(f"Bucket: \'{bucket_name}\' is already exists")
        try:
            self.client.fput_object(bucket_name, object_name, file_path, **kwargs)
            print("Object successfully uploaded")
        except Exception as err:
            print(err)

    def download_object_from_bucket(self, bucket_name: str, object_name: str, file_path):
        try:
            self.client.fget_object(bucket_name, object_name, file_path)
            print("Data of an object downloaded successfully")
        except Exception as err:
            print(err)

