from utils import aws_utils as aws
from utils import cloud_constants as cc


s3_obj = aws.S3_OBJ
bucket_name = cc.S3_BUCKET_NAME
s3_bucket = s3_obj.Bucket(bucket_name)


if __name__ == '__main__':
    print('Uploading Saved Model Assets to S3 Bucket')
    aws.s3_upload_folder(folder_path='./models/model_assets/gokube-phase1-jun19',
                         s3_bucket_obj=s3_bucket, prefix='model_assets')
