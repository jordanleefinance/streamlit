import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center;'>Meet the Founder</h1>", unsafe_allow_html=True)
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://i.ibb.co/VCF2fHY/nice-pic.jpg")
    with text_col:
        st.write(
    "My name is Jordan Lee, I am a financial and technological enthusiast, owner of [JMM Group](https://www.jmmgrp.com/index.html), an investor and a partner at a business information systems and process consulting firm. I obtained my Bachelor's degree in Finance and Information Science, as well as a Masters in Financial Analysis from Christopher Newport University. My primary objective is to empower entrepreneurs by supporting them in conceptualizing, synthesizing, and achieving their business objectives, assuming the roles of financial quarterback, stress reliever, and advocate for growth."
    " My motivation is driven by my desire to build healthy relationships and an entrepreneurial mindset, I approach every problem with diligence and a willingness to invest my abilities to make complex issues, simple. As a lifelong learner, I am dedicated to furthering my education by pursuing certifications such as the Series 63, 65, 66, 79, and CFA. Below, you will find a selection of my APIs/projects, and insights into my passions and life goals."
)


with st.container():
        st.write("""A key insight I gained from my master's program and previous roles is that businesses operate with complex systems within systems, greatly enhancing my ability to manage clients' needs effectively. The [Total Compensation Calculator](https://share.streamlit.io/jordanleefinance/streamlit/main/CityofNNGUI.py)
         (access upon request) created for the City of Newport News to attract new employees and provide current employees with a comprehensive view of their total compensation. Additionally, Frontline, the first digital temp staffing platform for green jobs, allowed me to explore innovative solutions such as the 
         [Independent Contractor Time Tracker](https://www.appsheet.com/start/76c16fba-7e57-48a4-ad40-8d17850daa92).
          I have always been a strong advocate for transparency in financial matters, especially regarding interest payments on loans. I encourage you to try the [Loan AM Schedule Calculator](https://jordanleefinance-streamlit-financeam-calculator-ty3xw0.streamlit.app/) to see exactly how much you are paying in interest.
         """)
# Want a sketch of a picture, I have the perfect tool for you [Memory Sketcher](https://jordanleefinance-streamlit-stinslepicture-9gdtbv.streamlit.app/).

with st.container():
    text_col, image_col = st.columns((1, 1))
    with image_col:
        st.image("https://images.squarespace-cdn.com/content/v1/58fffa62ebbd1a6b493a5cc2/1493231727410-J4VQU30C6G2FW1L7EIRH/DSC_0964.JPG?format=1000w", caption="Photo from www.lacrossthenations.org")
    with text_col:
        st.write(""" 
        During my second and third years of undergrad, I had the incredible opportunity to go abroad and introduce lacrosse to regions where the game was virtually unknown. One of my greatest passions is increasing diversity within the sport. I kindly ask you to consider donating to support this cause. [Read more...](https://www.lacrossethenations.org/)
        "To become a truly great leader, you must embrace the principles of servant leadership." One impactful way to give back is by volunteering with your local Habitat for Humanity nonprofit at a nearby ReStore. Their mission to build strength, stability, and self-reliance through shelter aligns with the values I strive to instill in our clients. [For more information...](https://www.habitat.org)
        """)


with st.container():
    st.write("""One of my goals is to create a platform that empowers entrepreneurs and investors to grow their income based on their own knowledge and confidence. Customize your stock search with my...
        [Stock Search Web App](https://share.streamlit.io/jordanleefinance/streamlit/main/gitexample.py)! 
        Click [here](https://jordanleefinance-streamlit-marcella-1c4vww.streamlit.app/) for a dashboard of a couple 
        macro-economic analysis tools in the recent US economy. Make better decisions with your portfolio by using the 
        [Portfolio Optimizer](https://jordanleefinance-streamlit-dfdemo-hftefy.streamlit.app/). Thank you for your time!""")


