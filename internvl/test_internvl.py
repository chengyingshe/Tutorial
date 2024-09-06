from lmdeploy import pipeline
from lmdeploy.vl import load_image

pipe = pipeline("/home/scy/models/OpenGVLab/InternVL2-2B")

image = load_image('004atEXYgy1gpx0ifty7tj60x80x51jt02.jpg')
response = pipe(('请你根据这张图片，讲一个脑洞大开的梗', image))
print(response.text)