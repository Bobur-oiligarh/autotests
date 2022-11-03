from minio.api import Minio
from pathlib import Path
from utils.yaml_reader import YAMLReader


class MinioS3:

    def __init__(self):
        self.bucket_name = YAMLReader().minio_data.get('bucket_name')
        self.client = Minio(
            endpoint=YAMLReader().minio_data.get('server'),
            access_key=YAMLReader().minio_data.get('access_key'),
            secret_key=YAMLReader().minio_data.get('secret_key'),
            secure=YAMLReader().minio_data.get('secure')
        )

    def upload(self, object_name: str, file_path: str, **kwargs):
        try:
            self.client.fput_object(self.bucket_name, object_name, file_path, **kwargs)
            print("Object successfully uploaded")
        except Exception as err:
            print(err)

    def download(self, bucket_name: str, object_name: str, file_path, **kwargs):
        try:
            self.client.fget_object(bucket_name, object_name, file_path, **kwargs)
            print("Data of an object downloaded successfully")
        except Exception as err:
            print(err)


if __name__ == '__main__':
    m = MinioS3()
    m.upload('check', '/home/bobur/Test/testfile')

    path = Path(__file__).joinpath('credentials.yaml')
    print(path)

    print(m.client.get_object('test', 'TESTFILE'))

