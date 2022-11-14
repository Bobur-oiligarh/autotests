import base64
import io
import PIL.Image as Image
from minio.api import Minio
from utils.patterns.singleton import Singleton
from utils.yaml_reader import YAMLReader


class MinioS3:
    _IMAGE_EXTENSIONS = YAMLReader().read()['image_extensions']

    def __init__(self):
        self._file_bucket = YAMLReader().minio_data.get('file_bucket')
        self._img_bucket = YAMLReader().minio_data.get('image_bucket')

        self._client = Minio(
            endpoint=YAMLReader().minio_data.get('server'),
            access_key=YAMLReader().minio_data.get('access_key'),
            secret_key=YAMLReader().minio_data.get('secret_key'),
            secure=YAMLReader().minio_data.get('secure')
        )

    def put(self, object_name, data_in_bytes):
        data_as_a_stream = io.BytesIO(data_in_bytes)
        length = len(data_in_bytes)
        extension = object_name.split('.')[1]
        self._client.put_object(
            bucket_name=self._img_bucket if extension in self._IMAGE_EXTENSIONS else self._file_bucket,
            object_name=object_name,
            data=data_as_a_stream,
            length=length
        )

    def get(self, object_name: str):
        extension = object_name.split('.')[1]
        bucket_name = self._img_bucket if extension in self._IMAGE_EXTENSIONS else self._file_bucket
        obj = self._client.get_object(
            bucket_name=bucket_name,
            object_name=object_name
        )
        if bucket_name == self._file_bucket:
            return obj.read().decode()

        return Image.open(io.BytesIO(obj.read()))

    def get_b64(self, object_name: str):
        data = self.get(object_name)

        extension = object_name.split(".")[1]
        if extension in self._IMAGE_EXTENSIONS:
            return self._foto_to_b64(data, extension)

        return self._str_to_b64(data)

    @staticmethod
    def _str_to_b64(data):
        data_bytes = data.encode('utf-8')
        base64_bytes = base64.b64encode(data_bytes)
        return base64_bytes.decode('utf-8')

    @staticmethod
    def _foto_to_b64(data, extension):
        buffered = io.BytesIO()
        data.save(buffered, format=extension)
        buffered.seek(0)
        img_byte = buffered.getvalue()
        return f"data:image/{extension};base64,{base64.b64encode(img_byte).decode()}"


class MinioParent(MinioS3, metaclass=Singleton):
    pass
