# Homography
# Calibration

This document explains how to calibrate the camera using a web application designed specifically for this purpose. 

## Procedure

1. **Use the website**: Open the website designed for calibration. 

2. **Modify the script**: Add the necessary code to the bottom of the `app.py` script to connect the camera to the device. The specific code depends on the type of camera you're using, hence it's not included in the script. 

3. **Run the script and the web application**: Execute the `app.py` script and then open the web application.

4. **Plot points and measure**: Plot points on the display shown on the web application and measure them in real life. Ensure that the camera is at the same orientation and height as it will be in real life. You should use a large, flat surface for measurement.

5. **Perform random point tests**: Go through the process of selecting random points throughout the frame. Ensure these points are well distributed for best results. 

6. **Update the homography script**: Open the `log.txt` file and transfer the data to the `homography.py` script. Replace the existing pixel coordinates and real-life coordinates with your data. The current setup is configured for a Raspberry Pi camera placed 11 inches perpendicular to the ground. The format for entering coordinates is `x1, y1, x2, y2...` and so on.

7. **Run the homography script**: Once the coordinates have been added, execute the `homography.py` script. You should now have a calibrated system. For better accuracy, you can add more points.

Happy calibrating!
