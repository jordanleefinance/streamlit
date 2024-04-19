import streamlit as st


st.markdown("<h1 style='text-align: center;'>About Me</h1>", unsafe_allow_html=True)
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://images.squarespace-cdn.com/content/v1/60be58fa133ce37a9d039d31/0f886309-0ec5-4bc7-bbfd-11fb2045044d/JL+-+Website+Select.jpg?format=750w")
    with text_col:
        st.write(
    "Thank you for visiting my webpage. I am financial enthusiast and a partner at a business systems and process consulting firm. I obtained my Bachelor's degree in Finance and Information Science, as well as a Master's degree in Financial Analysis from Christopher Newport University. My primary objective is to empower entrepreneurs by supporting them in conceptualizing, synthesizing, and achieving their business objectives, assuming the roles of financial quarterback, stress reliever, and advocate for growth."
    "With an entrepreneurial mindset and a firm commitment to cultivating relationships, I approach every problem with diligence and a willingness to invest my abilities to make complex issues, simple. As a lifelong learner, I am dedicated to furthering my education by pursuing certifications such as the CFA, Series 63, 65, 66, and 79. Below, you will find a selection of my APIs/projects, and insights into my passions and life goals."
)


with st.container():
        st.write("""A major detail I learned from my masters and previous roles is within businesses
            there are systems within systems which translated tremendously
        into my understanding of how to manage clients' needs. The Total [Compensation Calculator](https://share.streamlit.io/jordanleefinance/streamlit/main/CityofNNGUI.py)
         (must request access) was designed for the City of Newport News to attract new employees as well as give current employees a visual of their total compensation.
         Frontline is the first digital temp staffing platform tailored for green jobs. I was able to
         explore different ways to help, for example the 
         [Independent Contractor Time Tracker](https://www.appsheet.com/start/76c16fba-7e57-48a4-ad40-8d17850daa92) and 
         Park Litter Calculator (Purchased).
        If you love to workout and hate the hassel of tracking your progress, try 
        [MAR (My Average Routine) Works Out](https://www.appsheet.com/start/198ae0e8-52d5-4428-927a-f0dc6770edaa) where you can personalize
         your schedule and track progress at your finger tips! I've always been a strong advocate of having full 
         transparency with how much you are paying the banks in interest when taking out a loan, 
         please try out [Loan AM Schedule Calculator](https://jordanleefinance-streamlit-financeam-calculator-ty3xw0.streamlit.app/).
         """)
# Want a sketch of a picture, I have the perfect tool for you [Memory Sketcher](https://jordanleefinance-streamlit-stinslepicture-9gdtbv.streamlit.app/).

with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://images.squarespace-cdn.com/content/v1/58fffa62ebbd1a6b493a5cc2/1493231727410-J4VQU30C6G2FW1L7EIRH/DSC_0964.JPG?format=1000w")
    with text_col:
        st.write(""" 
        CNU Men's lacrosse has given me the opportunity to go abroad to grow the game of lacrosse by going to
        places where they never heard of it before. A greater passion of mine is to increase the diversity in lacrosse, 
        please take time to consider donating. [Read more...](https://www.lacrossethenations.org/)
        "To become truly a great leader, you must become a servant leader."
        """)


with st.container():
    text_col, image_col = st.columns((2, 2))
    with image_col:
        st.image("https://mediacloud.kiplinger.com/image/private/s--x2_BoIgn--/f_auto,t_primary-image-desktop@1/v1604352227/Investing/stock-market-today-110220.jpg")
    with text_col:
        st.write("""One of my goals is to create an avenue for the average entreprenuer/investor to be able to learn how to grow 
        their income based on their own knowledge and confidence. Personalize your stock search with my 
        [Stock Search Web App](https://share.streamlit.io/jordanleefinance/streamlit/main/gitexample.py)! 
        Click [here](https://jordanleefinance-streamlit-marcella-1c4vww.streamlit.app/) for a dashboard of a couple 
        macro-economic analysis tools in the recent US economy. Make better decisions with your portfolio by using the 
        [Portfolio Optimizer](https://jordanleefinance-streamlit-dfdemo-hftefy.streamlit.app/)""")


with st.container():
    st.write("""[Research & Investment blog coming soon...](https://jmmgroupllc.blogspot.com/)
    This blog is aimed to give people more knowledge on common financial tools/concepts. Also, this blog 
        gives you an opportunity to provide any feedback on my website, strategies, etc. I am gathering ideas for what 
        topics to discuss and would love your input!
        """)
