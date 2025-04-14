import streamlit as st
from streamlit_lottie import st_lottie
import requests

# 🌟 Page Configuration
st.set_page_config(page_title="My Animated Website", page_icon="🚀", layout="wide")

# 🌟 Load Lottie Animations Function
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(f"Error loading Lottie animation: {e}")
        return None

# ✅ Load animations with fallback
home_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_kkflmtur.json") or {}
services_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vzsnvxpv.json") or {}
about_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_fcfjwiyb.json") or {}

# 🎯 Sidebar Navigation
st.sidebar.title("🔹 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🛠 Services", "📚 About", "📮 Contact"])

# 🏠 Home Page
if page == "🏠 Home":
    st.title("🚀 Welcome to Our Animated Website!")
    st.markdown("### 🌟 Explore the world of **technology**, **design**, and **innovation**! 💡🔥")
    st_lottie(home_animation, height=300, key="home")

    # 🌈 Key Features
    st.subheader("✨ Why Choose Us?")
    st.write("✅ **Creative Designs** - We bring ideas to life with stunning visuals. 🎨")
    st.write("✅ **Advanced Technology** - We use the latest tools to build amazing projects. 🖥")
    st.write("✅ **User-Friendly Experience** - Smooth, responsive, and interactive interfaces. 📱")

# 🛠 Services Page
elif page == "🛠 Services":
    st.title("🛠 Our Services")
    st.markdown("### 🚀 We offer **top-notch** solutions to enhance your business! 💼✨")
    st_lottie(services_animation, height=300, key="services")

    # 📌 Services List
    st.subheader("📌 What We Offer?")
    st.write("🔹 **Website Development** - Fully responsive and modern designs. 🌐")
    st.write("🔹 **AI-Powered Apps** - Smart applications with artificial intelligence. 🤖")
    st.write("🔹 **Mobile App Development** - Android & iOS apps for your business. 📱")
    st.write("🔹 **Graphic Design** - Creative logos, banners, and branding. 🎨")
    st.write("🔹 **SEO & Digital Marketing** - Rank higher and grow faster. 📈")

# 📚 About Page
elif page == "📚 About":
    st.title("📚 About Us")
    st.markdown("### 🏆 Passionate About **Technology, Innovation, and Growth**! 🚀")
    st_lottie(about_animation, height=300, key="about")

    # 💡 Company Mission
    st.subheader("💡 Our Mission")
    st.write("🎯 **Empowering businesses** through technology and innovation.")
    st.write("🎯 **Building creative and interactive** digital experiences.")
    st.write("🎯 **Delivering high-quality and performance-driven solutions.** 💎")

    # 🏆 Achievements
    st.subheader("🏆 Our Achievements")
    st.write("🏅 5+ Years of Experience in IT Industry.")
    st.write("🏅 100+ Successful Projects Delivered.")
    st.write("🏅 50+ Satisfied Clients from Around the World.")

# 📮 Contact Page
elif page == "📮 Contact":
    st.title("📮 Get in Touch!")
    st.markdown("### ✨ We'd love to hear from you! **Send us a message below.** 💌")

    # 📞 Contact Form
    name = st.text_input("**Your Name**", placeholder="Enter your name...")
    email = st.text_input("**Your Email**", placeholder="Enter your email...")
    message = st.text_area("**Your Message**", placeholder="Type your message here...")

    if st.button("📮 Submit"):
        if name and email and message:
            st.success("✅ Thank you for your message! We'll get back to you soon.")
        else:
            st.error("⚠️ Please fill in all fields before submitting.")

# 🎉 Footer
st.sidebar.markdown("---")
st.sidebar.markdown("✨ **Designed with ❤️ in Streamlit**")
st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://github.com/Misbah-jameel?tab=repositories)  [![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://www.linkedin.com/in/misbah-jameel-509aa32b8/)  [![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/Misbah55066)")

st.markdown("""
    <div style="text-align: center;">
        Made with ❤️ by <b>Misbah Jameel</b>
    </div>
""", unsafe_allow_html=True)