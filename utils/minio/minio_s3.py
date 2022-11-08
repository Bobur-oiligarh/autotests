import base64
import io
import json
import pickle
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

    def upload_unstructured_data(self, data_name: str, uploaded_data: Any, **kwargs):
        pass

    def upload_structured_data(self, data_name: str, uploaded_data: Any, **kwargs):
        if isinstance(uploaded_data, str):
            data_as_bytes = uploaded_data.encode('utf-8')
        elif isinstance(uploaded_data, dict):
            data_as_bytes = json.dumps(uploaded_data).encode('utf-8')
        elif isinstance(uploaded_data, list):
            data_as_bytes = bytes(uploaded_data)
        else:
            data_as_bytes = bytearray(uploaded_data)
        print(data_as_bytes)
        encoded_data = base64.b64encode(data_as_bytes)
        print(encoded_data)
        decoded_data = base64.b64decode(encoded_data)
        data_as_a_stream = io.BytesIO(decoded_data)
        print(data_as_a_stream)
        self.client.put_object(self.bucket_name, data_name, data_as_a_stream, length=len(data_as_bytes), **kwargs)

    def get(self, object_name: str, **kwargs):
        try:
            response = self.client.get_object(bucket_name=self.bucket_name, object_name=object_name)
            data = response.data
            decoded_data = data.decode()
            return decoded_data
        except Exception as err:
            print(err)


class MinioParent(MinioS3, metaclass=Singleton):
    pass


if __name__ == '__main__':
    m = MinioS3()

    m.upload_structured_data('test25', uploaded_data=[1, 2, 3])
    resp = m.client.get_object('test', 'test25')
    print(type(resp))
    data = resp.data
    print(data)
    print(data.decode())
    print(type(data.decode()))
