# 🖼️ Image Classification using OpenCV & Scikit-learn

## 📌 Project Overview
This project demonstrates a simple **Image Classification pipeline** using **OpenCV** for image preprocessing and **scikit-learn** for training a machine learning model.  
The goal is to build a classifier that can differentiate between two classes of images (e.g., cats vs dogs, or any two categories).

## 🛠️ Tech Stack
- **Python 3**
- **OpenCV (cv2)** → for image loading and preprocessing
- **NumPy** → for array manipulations
- **Scikit-learn** → for building and evaluating the ML model

## 📂 Project Workflow
1. **Data Collection**  
   - Load a dataset of images (two categories).
   
2. **Preprocessing (OpenCV)**  
   - Resize all images to a fixed size.  
   - Convert images to grayscale.  
   - Flatten images into feature vectors.  

3. **Model Training (Scikit-learn)**  
   - Train a **Logistic Regression** classifier on the extracted features.  
   - Split data into training and test sets.  

4. **Model Evaluation**  
   - Evaluate accuracy on the test set.  
   - Display a **confusion matrix**.  

5. **Prediction on New Images**  
   - Load and preprocess a new unseen image.  
   - Predict its class using the trained model.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python numpy scikit-learn matplotlib

   or 

   pip install -r requirements.txt

2. Run the script:
   ```bash
   python image_classifier.py

3. To test with your own images, replace the sample dataset with your custom images.

📊 Results

   - Successfully trained a Logistic Regression classifier.
   - Achieved good classification accuracy on the test set.
   - Model is able to predict unseen images correctly.

🔮 Future Scope

   - Try different ML algorithms (SVM, Random Forest, etc.).
   - Add Deep Learning models (CNNs with TensorFlow/PyTorch).
   - Experiment with color features instead of grayscale.
   - Deploy as a Flask API for real-world applications.