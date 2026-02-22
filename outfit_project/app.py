import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
import os
from sklearn.metrics.pairwise import euclidean_distances

st.title("👗 Outfit Recommendation System (Color Matching)")
st.write("Upload your **Tops** and **Bottoms (Jeans)**, and get the **top 3 best matching pairs** based on color similarity!")

# Upload multiple images
top_files = st.file_uploader("Upload Top Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
bottom_files = st.file_uploader("Upload Bottom Images (Jeans)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Extract average color from image
def extract_average_color(image, num_colors=3):
    image_resized = cv2.resize(image, (200, 200))
    image_rgb = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)
    avg_color = np.mean(kmeans.cluster_centers_, axis=0)
    return avg_color

if top_files and bottom_files:
    # Extract color features for tops
    top_features = {}
    for top_file in top_files:
        top_image = cv2.imdecode(np.frombuffer(top_file.read(), np.uint8), 1)
        avg_color = extract_average_color(top_image)
        top_features[top_file.name] = (avg_color, top_image)

    # Extract color features for bottoms
    bottom_features = {}
    for bottom_file in bottom_files:
        bottom_image = cv2.imdecode(np.frombuffer(bottom_file.read(), np.uint8), 1)
        avg_color = extract_average_color(bottom_image)
        bottom_features[bottom_file.name] = (avg_color, bottom_image)

    # Compute all possible pairings and distances
    all_pairs = []
    for top_name, (top_color, top_img) in top_features.items():
        for bottom_name, (bottom_color, bottom_img) in bottom_features.items():
            distance = np.linalg.norm(top_color - bottom_color)
            all_pairs.append((top_name, bottom_name, top_img, bottom_img, distance))

    # Sort by best match (lowest distance)
    all_pairs.sort(key=lambda x: x[4])

    # Select top unique matches
    used_tops = set()
    used_bottoms = set()
    best_pairs = []

    for top_name, bottom_name, top_img, bottom_img, distance in all_pairs:
        if top_name not in used_tops and bottom_name not in used_bottoms:
            best_pairs.append((top_name, bottom_name, top_img, bottom_img, distance))
            used_tops.add(top_name)
            used_bottoms.add(bottom_name)
        if len(best_pairs) >= 3:
            break

    # Display results
    st.subheader("🔥 Top 3 Best Matching Pairs")
    for i, (top_name, bottom_name, top_img, bottom_img, distance) in enumerate(best_pairs):
        st.markdown(f"### Pair {i+1}: {top_name} + {bottom_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.image(top_img, caption=f"Top: {top_name}", use_column_width=True)
        with col2:
            st.image(bottom_img, caption=f"Jeans: {bottom_name}", use_column_width=True)

        match_score = max(0, 100 - distance)  # Ensure score is not negative
        st.write(f"🔥 **Matching Score:** {match_score:.2f}%")
        if distance < 5:
            st.success("✅ Excellent Match!")
        else:
            st.info("ℹ️ Decent Match")
        st.markdown("---")
