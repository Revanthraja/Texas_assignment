## Live Human Detection using OpenCV and Laptop Camera
This Python script detects humans in real-time using OpenCV and the laptop camera. It utilizes a pre-trained human detection model based on the Histogram of Oriented Gradients (HOG) algorithm.

### Prerequisites
Python 3.6 or higher
OpenCV library (pip install opencv-python)
### Usage
Clone the repository or download the main.py file.

### Install the required dependencies by running the following command:

pip install opencv-python
Run the script using the following command:


python main.py
The laptop camera will be initialized, and a new window titled "Human Detection" will open displaying the live video feed.

Detected humans will be outlined by green rectangles on the video feed. The total number of detected humans will be printed in the console.

To exit the script, press the 'q' key.

### Customization
You can modify the parameters of the hog.detectMultiScale() function in the code to adjust the human detection sensitivity. For example, you can change the winStride, padding, and scale values to achieve desired results.

Feel free to incorporate additional features or integrate the code into your own projects as needed.

### Acknowledgements
The human detection in this script is based on the HOG-based pedestrian detector provided by the OpenCV library.

### License
This project is licensed under the MIT License.

