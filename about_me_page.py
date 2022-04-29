import streamlit as st
from PIL import Image
image = Image.open(r"C:\Users\jorda\OneDrive\Documents\Pictures\nice_pic.jpg")

st.header("Jordan Lee")
st.subheader("Financial Analyst")
st.image(image)
st.write("Thank you for checking out my webpage! I am a recent graduate from Christopher Newport University with "
         "an entrepreneurial mindset and strong will to invest into building relationships."
         " In the next 5 years, I plan on pursing my CFA (Chartered Financial Analyst) and shortly after "
         "register JMM Group, LLC as an RIA (Registered Investment Advisor). "
         "A major detail I learned from my masters is within businesses "
         "there are systems within systems and I believe a great"
         " way to incorporate systems thinking into business decision making is through information science."
         "Below you can find some of my passions, goals, hobbies."
         )

with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.squarespace-cdn.com%"
                 "2Fcontent%2Fv1%2F58fffa62ebbd1a6b493a5cc2%2F1493231761575-WDH1W20PRMVBEFOZ4UE0%2FIMG_"
                 "9293.JPG%3Fformat%3D1000w&imgrefurl=https%3A%2F%2Fwww.lacrossethenations.org%2F&tbnid=VIr89ozQdltT9M&"
                 "vet=12ahUKEwjSsM78r7r3AhVvn3IEHT0eCDkQMygFegUIARDGAQ..i&docid=tEpMMga8-6AEZM&w=1000&h=667&q=lacrosse%2"
                 "0the%20nations&ved=2ahUKEwjSsM78r7r3AhVvn3IEHT0eCDkQMygFegUIARDGAQ")
    with text_col:
        st.subheader("Grow the game")
        st.write("""CNU Men's lacrosse has given me th opportunity to go abroad to grow the game of lacrosse by going to
        places where they never heard of it before.""")
        st.markdown("[Read more...] (https://www.lacrossethenations.org/)")

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
        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.alphasoftware.com%2Fblog%2Fwere-all-"
                 "app-happy-people-spend-more-time-in-mobileapps-than-watching-tv&psig=AOvVaw3upkm9qRcEKuWe8I"
                 "o_WvUl&ust=1651357073651000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLigztemuvcCFQAAAAAdAAAAABAD")
    with text_col:
        st.subheader("Apps")
        st.write("""The Total Compensation Calculator was designed for the City of Newport News.""")
        st.markdown("[Compensation Calculator...] "
                    "(https://share.streamlit.io/jordanleefinance/streamlit/main/CityofNNGUI.py)")
        st.write("""**Frontline** is the first digital temp staffing platform tailored for green jobs.""")
        st.markdown("[Independent Contractor Time Tracker...] (https://www.lacrossethenations.org/)")
        st.write("""Personalize your stock search with this web app!""")
        st.markdown("[Stock Search Web App...] "
                    "(https://share.streamlit.io/jordanleefinance/streamlit/main/gitexample.py)")

with st.container():
    image_col, text_col = st.columns((2, 1))
    with image_col:
        st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fadvantagefamily.com%2Fblog%2F19-blog-topics-to-"
                 "attract-new-leads-to-your-financial-management-practice%2F&psig=AOvVaw0G6oW6jAKrwihK6CnOF3jI&ust="
                 "1651356896390000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIjYme6suvcCFQAAAAAdAAAAABAJ")
    with text_col:
        st.subheader("Blog")
        st.write("""My blog is aimed to give people more knowledge on common financial tools/concepts. Also, this blog 
        gives you an opportunity to provide any feedback on my website, strategies, etc.""")
        st.markdown("[JMM Blog] "
                    "(https://www.jmmgroupllc.xyz/templates/blog.html)")
