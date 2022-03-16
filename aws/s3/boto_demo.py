## 访问s3
import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('my_bucket_name')

for object_summary in my_bucket.objects.filter(Prefix="dir_name/"):
    print(object_summary.key)