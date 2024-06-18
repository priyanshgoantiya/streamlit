import streamlit as st
import pandas as pd
import time
from io import StringIO
st.title("Startup Dashboard")
st.header("I am learing streamlit")
st.subheader("And I am loving it")
st.write("This is a normal text")
st.markdown("""
### My favorite Movies
- matrix
- lord of the rings
- my name is khan 
""")

st.code("""
def foo(input):
return foo**2
x=foo(2)
""")

st.latex('x^2+Y^2+7=0')

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 95],
    "Package": [100000, 120000, 110000]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.metric('Revenue','Rs 3L','+3%')

st.json({
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 90, 95],
    "Package": [100000, 120000, 110000]
})

image_url = "https://media.wired.com/photos/5ca648a330f00e47fd82ae77/master/pass/Culture_Matrix_Code_corridor.jpg"

# Display the image
st.image(image_url, caption='matrix', use_column_width=True)

video_url = 'https://archive.org/download/BigBuckBunny_328/BigBuckBunny_512kb.mp4'
st.video(video_url)

st.title("The Matrix Movie Clip")

# Display a YouTube video (The Matrix Trailer)
youtube_url = 'https://www.youtube.com/watch?v=vKQi3bBA1y8'
st.video(youtube_url)

st.sidebar.title("Sidebar ka title")

col1,col2,col3=st.columns(3)

with col1:
    st.image("data:image/jpeg;base64,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")
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVS8svV4Xrasy0CmWUjzigjRa0-ug7w5VoXg&s")
with col3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi6qIBfKhVuhMvBCEKHWNM82cvHuXoOtMKQw&s")

st.error("Login failed")
st.success("Login successfull")
st.info("Login successfull")
st.warning("Login successfull")


bar = st.progress(0)

for i in range(1,101):
    bar.progress(i)

Email=st.text_input("Enter your Email:")
age=st.number_input("Enter your age:")
reg_date=st.date_input("Enter the date")

email=st.text_input("Enter your email:")
password=st.text_input("Enter your password:")
gender=st.selectbox('select gender',['Male','Female','others'])
btn=st.button("Login")

if btn:
    if email=='priyanshgoantiya@gmail.com' and password=='P123':
        st.balloons()
        st.write(gender)
    else:
        st.error("login failed")

file=st.file_uploader("upload your file")

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df)
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()

    # Display the info as text
    st.text(s)

