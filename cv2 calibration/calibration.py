import numpy as np
import cv2 as cv
import glob

# Define calibration pattern parameters
pattern_size = (9, 6)  # Number of inner corners in the calibration pattern
pattern_type = cv.CALIB_CB_ADAPTIVE_THRESH | cv.CALIB_CB_NORMALIZE_IMAGE  # Pattern detection flags

# Prepare object points (3D coordinates of calibration pattern corners)
objp = np.zeros((np.prod(pattern_size), 3), np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from all calibration images
objpoints = []  # 3D object points in real-world coordinates
imgpoints = []  # 2D image points in image coordinates

# Read calibration images
image_folder = '/Users/logandelaar/Desktop/renamed/'
images = glob.glob(image_folder + '*.jpg')

# Iterate over calibration images
for image_path in images:
    img = cv.imread(image_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find calibration pattern corners
    ret, corners = cv.findChessboardCorners(gray, pattern_size, flags=pattern_type)

    # If pattern found, add object points and image points
    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

# Perform camera calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Print calibration results
print("Camera Matrix:")
print(mtx)
print("\nDistortion Coefficients:")
print(dist)

# Save calibration data
calibration_data = {'mtx': mtx, 'dist': dist}
np.savez('calibration_data.npz', **calibration_data)
