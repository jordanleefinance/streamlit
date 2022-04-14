import streamlit as st


st.header("Jordan Lee")
st.subheader("Financial Analyst")
st.write("Thank you for checking out my webpage! I am a recent graduate from Christopher Newport University with"
         "an entrepreneurial mindset and strong will to invest into building relationships."
         " In the next 5 years, I plan on pursing my CFA (Chartered Financial Analyst) and shortly after "
         "register JMM Group, LLC as an RIA (Registerd Investment Advisor). "
         "A major detail I learned from my masters is within businesses there are systems within systems and I believe a great"
         " way to incorporate systems thinking into business decision making is through information science."
         "Below you can find some of my passions, goals, hobbies."
         )


with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://www.cnusports.com/images/2021/9/24/Lee_Jordan.jpg?width=300")
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