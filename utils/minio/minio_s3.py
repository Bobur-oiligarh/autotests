import base64
import io
import PIL.Image as Image
from minio.api import Minio
from utils.patterns.singleton import Singleton
from utils.yaml_reader import YAMLReader


class MinioS3:
    IMAGE_FORMATS = ['jpg', 'png', 'jpeg', 'svg', 'jfif', 'pjpeg', 'pjp']

    def __init__(self):
        self.client = Minio(
            endpoint=YAMLReader().minio_data.get('server'),
            access_key=YAMLReader().minio_data.get('access_key'),
            secret_key=YAMLReader().minio_data.get('secret_key'),
            secure=YAMLReader().minio_data.get('secure')
        )

    def put_object(self, object_name, data_in_bytes):
        data_as_a_stream = io.BytesIO(data_in_bytes)
        length = len(data_in_bytes)
        extension = object_name.split('.')[1]
        self.client.put_object(bucket_name="images" if extension in self.IMAGE_FORMATS else "files",
                               object_name=object_name,
                               data=data_as_a_stream,
                               length=length)

    def get_object(self, object_name: str):
        extension = object_name.split('.')[1]
        bucket_name = 'images' if extension in self.IMAGE_FORMATS else 'files'
        obj = self.client.get_object(
                     bucket_name=bucket_name,
                     object_name=object_name
                 )
        if bucket_name == 'files':
            return obj.read().decode()

        return Image.open(io.BytesIO(obj.read()))


    def to_base64(self, object_name: str):
        data = self.get_object(object_name)

        extension = object_name.split(".")[1]
        if extension in self.IMAGE_FORMATS:
            return self._foto_to_b64(data, extension)

        return self._str_to_b64(data)

    def _str_to_b64(self, data):
        data_bytes = data.encode('utf-8')
        base64_bytes = base64.b64encode(data_bytes)
        return base64_bytes.decode('utf-8')

    def _foto_to_b64(self, data, extension):
        buffered = io.BytesIO()
        data.save(buffered, format=extension)
        buffered.seek(0)
        img_byte = buffered.getvalue()
        return f"data:image/{extension};base64,{base64.b64encode(img_byte).decode()}"


class MinioParent(MinioS3, metaclass=Singleton):
    pass


if __name__ == '__main__':
    m = MinioParent()
    string = "Hello World"
    str_bytes = string.encode('utf-8')
    print(str_bytes)
    m.put_object("text.txt", str_bytes)

