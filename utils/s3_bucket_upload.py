from minio import Minio
from minio.error import S3Error
import base64
from minio.error import S3Error

S3_SERVER = 'prep-console-os.hamkorbank.uz/buckets'
S3_ACCESS_KEY = 'MIdO271L6wdhFj8U'
S3_SECRET_KEY = 'W5vHv4gksQD77rVLnQB1T3SeyuHXlxQd'


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        S3_SERVER,
        access_key=S3_ACCESS_KEY,
        secret_key=S3_SECRET_KEY,

    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)