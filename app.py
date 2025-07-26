import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("logistic_model.pkl")

# App title and description
st.set_page_config(page_title="🚢 Titanic Survival Predictor", layout="centered")
st.title("🚢 Titanic Survival Predictor")
st.markdown(
    """
    Use this interactive app to predict whether a passenger would have survived the Titanic disaster,
    based on input features used in the logistic regression model.
    """
)

# Sidebar inputs
st.sidebar.header("Passenger Details")
pclass = st.sidebar.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.sidebar.radio("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 100, 30)
sibsp = st.sidebar.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
parch = st.sidebar.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
fare = st.sidebar.number_input("Fare", 0.0, 600.0, 50.0)
embarked = st.sidebar.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Encode categorical variables
sex_encoded = 1 if sex == "male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked_encoded = embarked_map[embarked]

# Prepare input
input_data = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])

# Main prediction section
st.markdown("---")
st.subheader("🎯 Prediction Result")

# Choose gender-specific icon
image_url = "https://cdn-icons-png.flaticon.com/512/168/168882.png"  # Male
if sex == "female":
    image_url = "https://cdn-icons-png.flaticon.com/512/2922/2922561.png"  # Female

col1, col2 = st.columns([1, 3])
with col1:
    st.image(image_url, width=100)
with col2:
    if prediction == 1:
        st.success(f"✅ This passenger would have **survived**!")
        st.markdown(f"**Survival Probability:** `{probability:.2%}`")
    else:
        st.error(f"❌ This passenger would **not have survived**.")
        st.markdown(f"**Survival Probability:** `{probability:.2%}`")

    st.markdown("---")
    st.info("Note: This prediction is based on a logistic regression model trained on historical Titanic data.")

# Footer
st.markdown("""
<style>
    footer {visibility: hidden;}
    .stApp {
        background-color: #f4f6f8;
    }
</style>
""", unsafe_allow_html=True)
