import streamlit as st
from PIL import Image
image = Image.open(r"C:\Users\jorda\OneDrive\Documents\Pictures\nice_pic.jpg")

st.header("About Me")
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(image)
    with text_col:
        st.subheader("Jordan Lee")
        st.write(
            "Thank you for checking out my webpage! Below you can find some of my passions, goals, hobbies."
            "I am a recent graduate from Christopher Newport University with "
            "an entrepreneurial mindset and strong will to invest into building relationships."
            " In the next 5 years, I plan on pursing my CFA (Chartered Financial Analyst) and shortly after "
            "register JMM Group, LLC as an RIA (Registered Investment Advisor). "
            "A major detail I learned from my masters is within businesses "
            "there are systems within systems and I believe a great"
            " way to incorporate systems thinking into business decision making is through information science."

        )

with st.container():
    text_col, image_col = st.columns((2, 1))
    with image_col:
        st.image("https://mediacloud.kiplinger.com/image/private/s--x2_BoIgn--/f_auto,t_primary-image-desktop"
                 "@1/v1604352227/Investing/stock-market-today-110220.jpg")
    with text_col:
        st.subheader("Stock Analysis")
        st.write("""Over time, I've noticed a lot of people don't know much about the stock market or even what a stock
        is in general. One of my goals is to create an avenue for the average person to be able to learn how to grow 
        their income based on their own knowledge and confidence.""")
        st.markdown("Click [here](https://www.jmmgroupllc.xyz/templates/products.html) "
                    "for a glimpse of a couple analysis tools.")
        st.markdown("Click [subscribe](https://www.jmmgroupllc.xyz/templates/subscribe.html) "
                    "to be redirected to the subscribe page.")


with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://images.squarespace-cdn.com/content/v1/"
                 "58fffa62ebbd1a6b493a5cc2/1493171975996-XZCUH51COEBWDEL6X5NS/image-asset.jpeg?format=750w")
    with text_col:
        st.subheader("Grow the game")
        st.write("""CNU Men's lacrosse has given me th opportunity to go abroad to grow the game of lacrosse by going to
        places where they never heard of it before. [Read more...](https://www.lacrossethenations.org/)""")

with st.container():
    text_col, image_col = st.columns((1, 1))
    with image_col:
        st.image("https://www.alphasoftware.com/hs-fs/hubfs/2015/09/"
                 "background.png?width=1350&height=840&name=background.png")
    with text_col:
        st.subheader("Apps")
        st.write("""The Total [Compensation Calculator](https://share.streamlit.io/jordanleefinance/streamlit/main/CityofNNGUI.py)
         was designed for the City of Newport News.
         Frontline is the first digital temp staffing platform tailored for green jobs. I was able to
         explore different ways to help, for example the 
         [Independent Contractor Time Tracker](https://www.lacrossethenations.org/) and 
         [Park Litter Calculator]().
         Personalize your stock search with my 
        [Stock Search Web App](https://share.streamlit.io/jordanleefinance/streamlit/main/gitexample.py)!""")

with st.container():
    image_col, text_col = st.columns((2, 2))
    with image_col:
        st.image("https://advantagefamily.com/wp-content/uploads"
                 "/2018/06/financial-planner-blog-topics-1.png")
    with text_col:
        st.subheader("Blog")
        st.write("""My [blog](https://www.jmmgroupllc.xyz/templates/blog.html) is aimed to give people more knowledge on common financial tools/concepts. Also, this blog 
        gives you an opportunity to provide any feedback on my website, strategies, etc.""")
