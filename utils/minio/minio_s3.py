import base64
import io
import PIL.Image as Image
from minio.api import Minio
from utils.patterns.singleton import Singleton
from utils.yaml_reader import YAMLReader


class MinioS3:
    IMAGE_FORMATS = ['jpg', 'png', 'jpeg', 'svg', 'jfif', 'pjpeg', 'pjp']

    def __init__(self):
        self.bucket_name = None
        self.format = None
        self.client = Minio(
            endpoint=YAMLReader().minio_data.get('server'),
            access_key=YAMLReader().minio_data.get('access_key'),
            secret_key=YAMLReader().minio_data.get('secret_key'),
            secure=YAMLReader().minio_data.get('secure')
        )

    def put_object(self, object_name, data_in_bytes):
        data_as_a_stream = io.BytesIO(data_in_bytes)
        length = len(data_in_bytes)
        self.format = object_name.split('.')[1]
        self.bucket_name = "images" if self.format in self.IMAGE_FORMATS else "files"
        self.client.put_object(bucket_name=self.bucket_name,
                               object_name=object_name,
                               data=data_as_a_stream,
                               length=length)

    def get_object(self, object_name: str):
        self.format = object_name.split('.')[1]
        self.bucket_name = 'images' if self.format in self.IMAGE_FORMATS else 'files'
        obj = self.client.get_object(
                     bucket_name=self.bucket_name,
                     object_name=object_name
                 )
        if self.bucket_name == 'files':
            decoded_object = obj.read().decode()
        elif self.bucket_name == 'images':
            decoded_object = Image.open(io.BytesIO(obj.read()))
        return decoded_object

    def to_base64(self, object_name: str):
        data = self.get_object(object_name)
        if self.format not in self.IMAGE_FORMATS:
            data_bytes = data.encode('utf-8')
            base64_bytes = base64.b64encode(data_bytes)
            result_b64_str = base64_bytes.decode('utf-8')

        elif self.format in self.IMAGE_FORMATS:
            buffered = io.BytesIO()
            data.save(buffered, format=self.format)
            buffered.seek(0)
            img_byte = buffered.getvalue()
            result_b64_str = f"data:image/{self.format};base64,{base64.b64encode(img_byte).decode()}"
        return result_b64_str


class MinioParent(MinioS3, metaclass=Singleton):
    pass


if __name__ == '__main__':
    m = MinioParent()
    string = "Hello World"
    str_bytes = string.encode('utf-8')
    print(str_bytes)
    m.put_object("text.txt", str_bytes)

