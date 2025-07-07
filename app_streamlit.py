import streamlit as st
import numpy as np
import tensorflow as tf
from src.image_utils import load_and_preprocess_image
from src.recommend_utils import get_recommendations
from src.hospital_finder import get_hospitals_by_district

# Disease labels
labels = ['allergy', 'bleeding', 'cold', 'diarrhea', 'ear infection', 'fever', 'fracture', 'infection',
          'limping', 'mange', 'normal', 'parvo', 'rabies', 'tick', 'tumor', 'vomiting', 'wound']

# First aid info
disease_first_aid = {
    "allergy": "Keep your pet away from allergens. If scratching, apply a cold compress. Consult a vet for antihistamines.",
    "bleeding": "Apply gentle pressure with a clean cloth. Elevate the area if possible.",
    "cold": "Keep your pet warm and dry. Use a blanket. Consult a vet if symptoms worsen.",
    "diarrhea": "Offer small amounts of water frequently. Avoid food for 12 hours and monitor closely.",
    "ear infection": "Clean ears with vet-approved solution. Prevent scratching.",
    "fever": "Cool with a damp towel and ensure hydration. See a vet if fever continues.",
    "fracture": "Immobilize the limb and avoid movement. Go to the vet immediately.",
    "infection": "Clean the area and apply antiseptic. Prevent licking or scratching. See a vet.",
    "limping": "Rest the affected leg. If pain continues, see a vet.",
    "mange": "Isolate the pet. Use vet-prescribed medicated shampoos.",
    "normal": "Keep up with diet, hygiene, and vaccinations.",
    "parvo": "Highly contagious. Isolate pet and visit vet immediately.",
    "rabies": "Dangerous and life-threatening. Seek urgent medical treatment.",
    "tick": "Remove tick gently with tweezers. Disinfect the area.",
    "tumor": "Keep pet calm. See a vet to evaluate treatment options.",
    "vomiting": "Give small sips of water. If persists, see a vet.",
    "wound": "Clean with antiseptic. Apply bandage and prevent licking."
}

# 🧠 Load model with cache
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/pet_disease_model.h5")

# 🌐 Page config
st.set_page_config(page_title="🐾 Pet Help Recommendation System", layout="centered")
st.title("🐾 Pet Help Recommendation System")
st.subheader("Upload Pet Image to Detect Disease")

# 📷 Upload Section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # 🧠 Load model and predict
    with st.spinner("Analyzing image with AI model..."):
        model = load_model()
        image = load_and_preprocess_image(uploaded_file)
        prediction = model.predict(np.array([image]))[0]
        predicted_index = np.argmax(prediction)
        predicted_label = labels[predicted_index]
        confidence = round(float(prediction[predicted_index]), 2)

    # 🩺 Prediction Result
    st.markdown(f"### 🐶 Prediction: `{predicted_label}`")
    st.markdown(f"**Confidence:** `{confidence}`")
    st.markdown("---")

    # 🏥 Hospital Recommendations
    district = st.text_input("Enter your District for Hospital Recommendation:")
    if district:
        hospitals = get_hospitals_by_district(district)
        if hospitals:
            st.markdown("### 🏥 Recommended Hospitals:")
            for h in hospitals:
                st.markdown(f"- **{h['name']}**, {h['address']} – 📞 {h['phone']}")
        else:
            st.warning("No hospitals found for that district.")

    # 💊 Treatment & Diet
    st.markdown("---")
    st.markdown("### 🩺 Treatment & Diet Suggestions")
    recommendations = get_recommendations(predicted_label)
    first_aid = disease_first_aid.get(predicted_label, "Follow the vet's advice for specific first aid steps.")

    st.markdown(f"**Treatment:** {recommendations['treatment']}")
    st.markdown(f"**First Aid:** {first_aid}")
    st.markdown(f"**Diet Tips:** {recommendations['diet']}")
    st.markdown(f"**Vaccines:** {recommendations.get('vaccines', 'Consult your vet for vaccination schedule.')}")
