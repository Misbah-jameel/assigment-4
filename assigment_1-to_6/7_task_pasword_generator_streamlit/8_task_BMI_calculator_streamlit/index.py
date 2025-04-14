import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stSlider>div>div>div>div {
        background-color: #4CAF50;
    }
    .stMarkdown h1 {
        text-align: center;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("BMI Calculator 🏋️")
st.markdown("Calculate your Body Mass Index (BMI) quickly and easily!")

# Input fields for height and weight
col1, col2 = st.columns(2)

with col1:
    height = st.slider("Height (in cm)", 100, 250, 170)

with col2:
    weight = st.slider("Weight (in kg)", 30, 200, 70)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.balloons()

    # Display BMI result
    st.subheader(f"Your BMI is: **{bmi:.2f}**")

    # BMI Categories
    if bmi < 18.5:
        st.error("Underweight 🏃‍♂️ - You need to gain some weight.")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal Weight 🎉 - You're in a healthy range!")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️ - Consider a healthier diet and exercise.")
    else:
        st.error("Obese 🛑 - Please consult a doctor for advice.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Misbah Jameel]")