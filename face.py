from settings import ACCESS_KEY, SECRET_KEY, BUCKET
from PIL import Image, ImageDraw
# from camera import snapshot
import boto3


FILENAME = '22.jpg'
client = boto3.client('rekognition', 'eu-west-1',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

s3client = boto3.client('s3', 'eu-west-1',
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)


def send_image(filename):
    s3client.upload_file(filename, BUCKET, filename)


def detect_face(filename):
    response = client.detect_faces(Image={'S3Object': {'Bucket': BUCKET,
                                                       'Name': filename}})
    return response['FaceDetails']


def draw_face(filename, info):
    outfile = 'out-' + filename
    img = Image.open(filename).convert("RGB")
    draw = ImageDraw.Draw(img)
    for i in info:
        box = i['BoundingBox']
        top_left = (img.width*box['Left'], img.height*box['Top'])
        bottom_right = (top_left[0] + img.width*box['Width'], top_left[1] + img.height*box['Height'])
        draw.rectangle((top_left, bottom_right))
    img.save(outfile, "JPEG")


if __name__ == '__main__':
    # filename = snapshot()
    filename = 'test1.jpg'
    send_image(filename)
    info = detect_face(filename)
    draw_face(filename, info)
