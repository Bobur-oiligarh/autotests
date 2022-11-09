from minio.api import Minio
from utils.patterns.singleton import Singleton
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
        self.file_folder = YAMLReader().minio_data.get('file_folder')
        self.image_folder = YAMLReader().minio_data.get('image_folder')

    def upload_file(self, file_name: str, file_path: str, content_type: str = "application/txt", **kwargs):
        """Для загрузки файла в желаемом формате - передайти file_name с нужным расширением.(.txt, .yaml)"""
        self.client.fput_object(self.bucket_name,
                                object_name=f"{self.file_folder}/{file_name}",
                                file_path=f"{file_path}/{file_name}",
                                content_type=content_type, **kwargs
                                )

    def upload_image(self, image_name: str, path_to_image: str, content_type: str = "application/png", **kwargs):
        """Для загрузки файла в желаемом формате - передайти file_name с нужным расширением.(.txt, .yaml)"""
        self.client.fput_object(self.bucket_name,
                                object_name=f"{self.image_folder}/{image_name}",
                                file_path=f"{path_to_image}/{image_name}",
                                content_type=content_type, **kwargs
                                )

    def download_file(self, object_name: str, path_where_file_to_download: str, **kwargs):
        try:
            self.client.fget_object(bucket_name=self.bucket_name,
                                    object_name=f"{self.file_folder}/{object_name}",
                                    file_path=f"{path_where_file_to_download}/{object_name}", **kwargs
                                    )
        except Exception as err:
            print(err)

    def download_image(self, object_name: str, path_where_image_to_download: str, **kwargs):
        try:
            self.client.fget_object(bucket_name=self.bucket_name,
                                    object_name=f"{self.image_folder}/{object_name}",
                                    file_path=f"{path_where_image_to_download}/{object_name}", **kwargs
                                    )
        except Exception as err:
            print(err)


class MinioParent(MinioS3, metaclass=Singleton):
    pass


if __name__ == '__main__':
    pass
    # m = MinioS3()
    #
    # print(os.path.abspath('hamkorautotests/requirements.txt'))
    # m.upload_image('image.png', '/home/bobur/Pictures/Screenshot from 2022-09-14 14-09-45.png')
    # m.download_image('image.png', '/home/bobur/Pictures/')
    # m.upload_file('runner.py', '/home/bobur/PycharmProjects/hamkorautotests/')
    # m.download_file('runner.py', '/home/bobur/')
