import streamlit as st

st.header("User Information")
username = st.text_input("Enter your name")
if(username):
    st.text("Hi " + username)

passWord = st.text_input("Enter your password" , type = 'password')
#st.write(passWord)
df = st.file_uploader("upload your photo : " ,type = ["png",'jpeg'])

if(passWord):
    st.success("submitted successfully")

st.text("Select the gender")

Gender = st.radio("Select the gender",['Male','Female','Other'])
if(Gender == 'Other'):
    st.text("please specify")
    Other_gender_info = st.text_area("write about yourself in 500 words : ")

age = st.number_input("enter your age" ,18,100)

multi_select = st.multiselect("Enter the domain" ,["Data Science","Machine Learning" , "Web Development","App Development"])
#st.write(multi_select)

user_info = st.text_area("specify why are you intrested in this domain/domains :")
#st.image(df)

st.subheader("The code for creating this streamlit file is as follows")

Submit = st.button("Submit")

if(Submit):
    st.success("Submitted successfully")
    st.write("heyy " + username)
    st.write("Here are some links for more information about your selected domains ")
    for i in multi_select:
        if(i == "Data Science"):
            st.write("Data Science")
            st.write('https://www.geeksforgeeks.org/what-is-data-science/')
        elif(i == "Machine Learning"):
            st.write("Machine Learning")
            st.write('https://www.geeksforgeeks.org/introduction-machine-learning/')
        elif(i == "Web Development"):
            st.write("Web Development")
            st.write('https://www.geeksforgeeks.org/web-development/')
        elif(i == "App Development"):
            st.write("App Development")
            st.write('https://www.geeksforgeeks.org/android-app-development-fundamentals-for-beginners/')

    st.header("the code for this stream lit machine learning model deploying file uploaded on github ")
    st.write("repo link: " + 'https://github.com/Aniketbhand05/Streamlit')
