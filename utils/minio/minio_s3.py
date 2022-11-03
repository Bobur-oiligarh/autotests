import base64
import io
import json
from typing import Any

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

    def get(self, object_name: str, **kwargs):
        try:
            object_buffer = io.BytesIO()
            self.client.get_object(self.bucket_name, object_name, **kwargs)
            print("Data of an object downloaded successfully")
        except Exception as err:
            print(err)

    def upload(self, data_name: str, data: Any, **kwargs):
        data_as_bytes = bytes(data)
        encoded = base64.b64encode(data_as_bytes)
        decoded = base64.b64decode(encoded)
        data_as_a_stream = io.BytesIO(decoded)
        self.client.put_object(self.bucket_name, data_name, data_as_a_stream, length=len(data_as_bytes), **kwargs)


class MinioParent(MinioS3, metaclass=Singleton):
    pass


if __name__ == '__main__':
    m = MinioS3()
    m.upload('test6', data={1: 'klklkm'})

    d = {1: "kjkl"}
    asd = bytes(d)
    encode = base64.b64encode(asd)
    print(encode)
    kas = io.BytesIO(encode)
    print(kas.read())


    print(asd)
    mas = io.BytesIO(asd)
    print(mas.read())

    # m.upload('check', '/home/bobur/Test/testfile')
    #
    # path = Path(__file__).joinpath('credentials.yaml')
    # print(path)
    # value = "Some text I want to upload"
    # value_as_bytes = value.encode('utf-8')
    # value_as_a_stream = io.BytesIO(value_as_bytes)
    # m.put_object('mydata', value_as_a_stream, length=len(value_as_bytes))

    # data = 'test string'
    # m.put_object('next_data', data)

    # datas = {1: 'dmlkl'}
    # # data_as_bytes = data.encode('utf-8')
    # # print(data_as_bytes)
    # # data_as_a_stream = io.BytesIO(data_as_bytes)
    # # print(data_as_a_stream.read())
    # #
    # # data_2_as_a_stream = base64.b64encode(data_as_bytes)
    # # decoded = base64.b64decode(data_2_as_a_stream)
    # # print(data_2_as_a_stream)
    # # print(data_2_as_a_stream)
    # # print(decoded)
    #
    # encoded_data = json.dumps(data).encode('utf-8')
    # data_as_aa_stream = io.BytesIO(encoded_data)
    #
    # # encoded = base64.b64encode(data)
    # print(encoded_data)
    # print(data_as_aa_stream.read())
    # # decoded = base64.b64decode(encoded)
    # # print(decoded)
