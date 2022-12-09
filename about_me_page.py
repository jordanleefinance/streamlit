import streamlit as st


st.header("About Me")
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://media-exp1.licdn.com/dms/image/D4E03AQGiCmy0yRdqag/profile-displayphoto-shrink_800_800/0/1667658333213?e=1675900800&v=beta&t=M74I47KgX40ZrtsYObWoR4-ISAQB8cZ3-RGBXRGsao0")
    with text_col:
        st.write(
            "Thank you for checking out my webpage! "
            "I am currently an analyst for a consulting group and recently graduated from "
            "Christopher Newport University with my Master's in Financial Analysis. "
            "A major detail I learned from my masters is within businesses "
            "there are systems within systems and translated tremendously "
            "into my understanding of how to manage clients' needs. "
            "I have an entrepreneurial mindset and strong will to invest into building relationships."
            " In the next 5 years, I plan on pursing my CFA and shortly after "
            "pursue my Series 63, 65, 66, and 79. "
            "Below you can find some of my apps/projects, passions, goals, hobbies."
        )

with st.container():
        st.write("""The Total [Compensation Calculator](https://share.streamlit.io/jordanleefinance/streamlit/main/CityofNNGUI.py)
         was designed for the City of Newport News to attract new employees as well as give current employees a visual of their total compensation.
         Frontline is the first digital temp staffing platform tailored for green jobs. I was able to
         explore different ways to help, for example the 
         [Independent Contractor Time Tracker](https://www.appsheet.com/start/76c16fba-7e57-48a4-ad40-8d17850daa92) and 
         Park Litter Calculator (Purchased).
        If you love to workout and hate the hassel of tracking your progress, try 
        [Mar Works Out](https://www.appsheet.com/start/198ae0e8-52d5-4428-927a-f0dc6770edaa) where you can personalize
         your schedule and track progress at your finger tips! Want a sketch of a picture, I have the perfect tool for you
          [Memory Sketcher](https://jordanleefinance-streamlit-stinslepicture-9gdtbv.streamlit.app/)""")


with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://images.squarespace-cdn.com/content/v1/58fffa62ebbd1a6b493a5cc2/1493231727410-J4VQU30C6G2FW1L7EIRH/DSC_0964.JPG?format=1000w")
    with text_col:
        st.write(""""To become truly a great leader, you must become a servant leader" 
        CNU Men's lacrosse has given me the opportunity to go abroad to grow the game of lacrosse by going to
        places where they never heard of it before. [Read more...](https://www.lacrossethenations.org/)
        A greater passion of mine is to increase the diversity in lacrosse, please take time to consider donating.""")


with st.container():
    text_col, image_col = st.columns((2, 2))
    with image_col:
        st.image("https://mediacloud.kiplinger.com/image/private/s--x2_BoIgn--/f_auto,t_primary-image-desktop@1/v1604352227/Investing/stock-market-today-110220.jpg")
    with text_col:
        st.write("""One of my goals is to create an avenue for the average person to be able to learn how to grow 
        their income based on their own knowledge and confidence. Personalize your stock search with my 
        [Stock Search Web App](https://share.streamlit.io/jordanleefinance/streamlit/main/gitexample.py)! 
        Click [here](https://www.jmmgroupllc.xyz/templates/products.html) for a glimpse of a couple macro-economic analysis tools.""")


with st.container():
    st.write("""[Research & Investment blog coming soon...](https://www.jmmgroupllc.xyz/templates/blog.html)
    This blog is aimed to give people more knowledge on common financial tools/concepts. Also, this blog 
        gives you an opportunity to provide any feedback on my website, strategies, etc. I have yet to start posting due time
        constraints, but I am gathering ideas for what topics to discuss and would love your input! 
        """)
