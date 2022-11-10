import base64

from minio.api import Minio
from utils.patterns.singleton import Singleton
from utils.yaml_reader import YAMLReader


class MinioS3:

    def __init__(self):
        self.file_bucket = YAMLReader().minio_data.get('file_bucket')
        self.image_bucket = YAMLReader().minio_data.get('image_bucket')
        self.local_files_directory = YAMLReader().minio_data.get('file_folder_in_local')
        self.local_images_directory = YAMLReader().minio_data.get('image_folder_in_local')
        self.client = Minio(
            endpoint=YAMLReader().minio_data.get('server'),
            access_key=YAMLReader().minio_data.get('access_key'),
            secret_key=YAMLReader().minio_data.get('secret_key'),
            secure=YAMLReader().minio_data.get('secure')
        )

    def upload_file(self, file_name: str, **kwargs):
        """
        Для загрузки файла в желаемом формате - передайти file_name с нужным расширением.(.txt, .yaml)
        @param file_name: the files will be named in bucket (with extension)
        @param kwargs:
        @return:
        """
        self.client.fput_object(
            bucket_name=self.file_bucket,
            object_name=file_name,
            file_path=f"{self.local_files_directory}/{file_name}",
            **kwargs
        )

    def upload_image(self, image_name: str, **kwargs):
        """Для загрузки файла в желаемом формате - передайти file_name с нужным расширением.(.txt, .yaml)"""
        self.client.fput_object(
            bucket_name=self.image_bucket,
            object_name=image_name,
            file_path=f"{self.local_images_directory}/{image_name}",
            **kwargs
        )

    def download_file(self, object_name: str, **kwargs):
        """
        @param object_name: name of the unloaded object
        @param kwargs:
        @return:
        """
        try:
            self.client.fget_object(
                bucket_name=self.file_bucket,
                object_name=object_name,
                file_path=f"{self.local_files_directory}/{object_name}",
                **kwargs
            )
        except Exception as err:
            print(err)

    def download_image(self, object_name: str, **kwargs):
        try:
            self.client.fget_object(
                bucket_name=self.image_bucket,
                object_name=object_name,
                file_path=f"{self.local_images_directory}/{object_name}",
                **kwargs
            )
        except Exception as err:
            print(err)

    def data_to_base64(self, file_name):
        image_formats = ['jpg', 'png', 'jpeg', 'svg', 'jfif', 'pjpeg', 'pjp']
        file_format = file_name.split('.')[1]
        if file_format in image_formats:
            self.download_image(file_name)
            file_path = f"{self.local_images_directory}/{file_name}"
        else:
            self.download_file(file_name)
            file_path = f"{self.local_files_directory}/{file_name}"
        with open(file_path, 'rb') as file:
            encoded_string = base64.b64encode(file.read())
            file.close()
        return encoded_string.decode('utf-8')


class MinioParent(MinioS3, metaclass=Singleton):
    pass
