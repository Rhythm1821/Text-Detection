**Text Detection Project**
This project aims to detect text in images using the EasyOCR library, which provides an easy-to-use interface for optical character recognition (OCR). The main.py script utilizes EasyOCR to read text from an image and highlights the detected text regions with bounding boxes.

**Installation**
To run this project on your local machine, follow these steps:

**Clone the repository:**

git clone https://github.com/Rhythm1821/Text-Detection
cd Text-Detection
Install the required dependencies from the requirements.txt file:

pip install -r requirements.txt

**Usage**

* Place the images you want to process in the Data folder.
* Open the main.py script and modify the image_path variable to point to the image you want to process:
* image_path = os.path.join('Data', 'test1.png')

* Run the script:

python main.py
The script will read the image, detect text using EasyOCR, and display the image with highlighted bounding boxes around the detected text.

**Requirements**
The project requires the following Python packages, which can be installed using the provided requirements.txt file:

* easyocr==1.6.2
* matplotlib
* opencv-python-headless==4.5.4.60

Make sure to install the required packages before running the script.

**Note**
The text detection threshold is set to 0.25 (THRESHOLD = 0.25) in the script. You can adjust this threshold value to control the sensitivity of the text detection process.

**Support**
If you have any questions or need further assistance with the project, feel free to reach out. Happy text detection!

