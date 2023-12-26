import streamlit as st

st.title("title -> welcome to machine learninig")
st.header("header -> welcome to machine learninig")
st.subheader("subheader -> welcome to machine learninig")
st.text("text -> welcome to machine learninig")

st.markdown("# hi")
st.markdown("## hi")
st.markdown("### hi")
st.markdown("#### hi")
st.markdown("##### hi")

st.success("submitted successfully")
st.info("this is command for displpaying the information")
st.warning("this is command for warming")
st.error("this is command for error")

exp = ZeroDivisionError("Division is not possible with zero")
st.exception(exp)

st.write("1+2+3")
st.write(1+2+3)

#writing a code

st.code("x = 10\n"
        "for i in range(10):\n"
        "    print(i)\n")


#checkbox

st.text("select the gender")
st.checkbox("Male")

st.checkbox("Female")
if(st.checkbox("Other")):
    st.warning("you are nor eligible")

#radiobutton

radioButton = st.radio("select :" , ("Male" , "Female","Other"))
if(radioButton == "Male"):
    st.success("you are a male")
elif(radioButton == "Female"):
    st.success("you are a female")
elif(radioButton == "Other"):
    st.success("you are from a other gender")


#select box
st.subheader("select box")
selectBox = st.selectbox("Data science :" , ["Data analysis" , "Data mining", "Machine learning" , "Neural networks" , "Deep learning"])

if(selectBox == "Data analysis"):
    st.success("you choose " + selectBox)
elif(selectBox == "Data mining" ):
    st.success("you choose " +selectBox)
elif(selectBox == "Machine learning" ):
    st.success("you choose " +selectBox)
elif(selectBox == "Neural networks"):
    st.success("you choose "+selectBox)
elif(selectBox == "Deep learning"):
    st.success("you choose "+selectBox)

#multiselectbox

st.subheader('multiselect box')

mulselBox = st.multiselect("Data science :" , ["Data analysis" , "Data mining", "Machine learning" , "Neural networks" , "Deep learning"])
st.write("you have selected ",len(mulselBox) , "courses")

#slider

volume = st.slider('select the volume',1,100,step = 1)
st.write("volume --> " , volume)


st.subheader("taking input from the user")
name = st.text_input("enter your name -")
passWord = st.text_input("password : " , type = 'password')

st.write("pass - " ,passWord)
st.text_area("write about yourself in 500 words : ")


st.subheader("number input")
age = st.number_input("enter your age" , 18,100)
st.write("the age is : ", age)


st.subheader("date input")
date = st.date_input("enter the date")

st.subheader("time input")
st.time_input("time")
