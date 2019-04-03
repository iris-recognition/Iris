from cv2 import imread

from fnc.segment import segment
from fnc.normalize import normalize
from fnc.encode import encode


eyelashes_thres = 80

radial_res = 20
angular_res = 240

minWaveLength = 18
mult = 1
sigmaOnf = 0.5


def extractFeature(file):
        im = imread(im_filename)
	ciriris, cirpupil, imwithnoise = segment(im, eyelashes_thres, use_multiprocess)

	polar_array, noise_array = normalize(imwithnoise, ciriris[1], ciriris[0], ciriris[2],
										 cirpupil[1], cirpupil[0], cirpupil[2],
										 radial_res, angular_res)

	
	template, mask = encode(polar_array, noise_array, minWaveLength, mult, sigmaOnf)
    return file
