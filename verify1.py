import argparse
from time import time
from picamera import PiCamera
from time import sleep

from fnc.extractFeature import extractFeature
from fnc.matching import matching


camera = PiCamera()

parser = argparse.ArgumentParser()


parser.add_argument("--temp_dir", type=str, default="./templates/",
					help="Path to the directory containing templates.")

parser.add_argument("--thres", type=float, default=0.38,
					help="Threshold for matching.")

args = parser.parse_args()


camera.start_preview()
camera.brightness=60
sleep(10)
           
camera.stop_preview()

camera.capture('/home/pi/Downloads/img1.jpg')
file='/home/pi/Downloads/img1.jpg'
start = time()
print(file)
template, mask, file = extractFeature(file)

result = matching(template, mask, args.temp_dir, args.thres)

if result == -1:
	print('>>> No registered sample.')

elif result == 0:
	print('>>> No sample matched.')

else:
	print('>>> {} samples matched (descending reliability):'.format(len(result)))
	for res in result:
		print("\t", res)


end = time()
print('\n>>> Verification time: {} [s]\n'.format(end - start))
