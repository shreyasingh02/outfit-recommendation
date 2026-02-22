👗 Outfit Recommendation System (Color Matching)
📌 Project Overview

The Outfit Recommendation System is a machine learning–based application that helps users find the best clothing combinations based on color similarity. The system analyzes uploaded images of tops and bottoms (jeans) and recommends the top matching outfit pairs using image processing and clustering techniques.

This project demonstrates the use of computer vision, machine learning, and web app deployment to solve a real-world fashion problem.

🚀 Features

Upload multiple top wear images

Upload multiple bottom wear images (jeans)

Extract dominant colors from each clothing item

Compare color similarity between outfits

Recommend Top 3 best matching pairs

Display matching score for each pair

Interactive web interface using Streamlit

🧠 How It Works
1. Image Upload

Users upload images of:

Tops

Bottoms (Jeans)

2. Image Processing

The system processes each image by:

Resizing the image

Converting it to RGB format

Extracting pixel color data

3. Color Extraction

Using K-Means Clustering, the algorithm finds dominant colors in the clothing item.

4. Feature Creation

Each image is represented using its average dominant color vector.

5. Similarity Calculation

The system calculates similarity between tops and bottoms using Euclidean Distance.

6. Ranking Outfits

All possible pairs are compared and sorted.
The Top 3 pairs with the smallest color distance are recommended.

🛠 Tech Stack

Programming Language

Python

Libraries Used

Streamlit

NumPy

OpenCV

TensorFlow

Scikit-learn

(From requirements.txt) 

requirements

Machine Learning

K-Means Clustering

Distance-based similarity

Deployment

Streamlit Web Application


▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/outfit-recommendation-system.git
cd outfit-recommendation-system
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py
4️⃣ Open in Browser
http://localhost:8501
📊 Output

The system displays:

Best outfit combinations

Matching score

Visual comparison of clothing items

Example Output:

Pair 1: Black Top + Blue Jeans
Matching Score: 92%

Pair 2: White Top + Light Blue Jeans
Matching Score: 88%

Pair 3: Red Top + Dark Jeans
Matching Score: 84%