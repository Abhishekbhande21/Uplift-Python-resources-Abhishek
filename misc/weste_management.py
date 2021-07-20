import streamlit as st
from streamlit.proto.Button_pb2 import Button 

def main():
      st.title("Login Page")
      menu = ["Home","Login","Signup"]
      choice = st.sidebar.selectbox("Menu",menu)
      
      if choice == "Home":
          st.subheader("Home") 
          st.title("GARBAGE MANAGEMENT APP")
          from PIL import Image
          img = Image.open("save earth from garbage.jpg") 
          st.image(img,width=600)
          st.subheader("About Us:")
          st.text("The aim of the project is to provide a better solution to waste management.")
          st.text("Instead of dumping waste to another area,") 
          st.text("this app proposes to transport waste to those who require it for useful purposes.") 
          st.text("Hence the 'bekaar' is delivered to the companies who 'sweekar' it.")
          st.subheader("Importance")
          st.subheader("Working")
          st.text("Our website involves a total of 3 steps:")
          st.text("1)Collection of waste from the user. The waste collected is divided in 5 Categories : ")
          st.text("Paper, Plastic, Organic, Glass, Metal. The users can submit waste that")
          st.text("2)The delivery of the waste from the user to the company where the latter can order")
          st.text("the waste materials they want to use/process, right to their doorstep.")

          st.text("3)Utilisation of Waste : The company now, uses the waste by amicably collecting it,")
          st.text("profusely processing it and efficiently recycling it. (for example: A packaging company ")
          st.text(" may require old newspaper/books, an animal farm may require organic wastes and so on.)")
          st.sidebar.header("Contact Us:xxxxxxxxxxx")
          st.sidebar.header("Contact Us:xxxxxxxxxxx@gmai.com")














      elif choice == "Login":
          st.subheader("Login Section")
          username = st.sidebar.text_input("User Name")
          password = st.sidebar.text_input("password",type='password')
          if st.sidebar.checkbox('Login'):
              st.success("Logged In as {}".format(username))
              task = st.selectbox("Task",["Role","Waste Giver","Waste Taker"])
              if task =="Task":
                  st.subheader("Add your Role")
              elif task == "Waste Giver":
                  st.subheader("Waste Giver")
              elif task == "Waste Taker":
                  st.subheader("Waste Taker")  






      elif choice == "Signup":
          st.subheader("Create New Account")
          new_user = st.text_input("Username")
          new_password = st.text_input("Password",type='password')
          
          
          if  st.button("signup"):
              st.success("You have successfully created an account")
              st.info("Goto Login Menu to Login")  
               


if _name_ == '_main_':
    main(import streamlit as st)
from streamlit.proto.Button_pb2 import Button 
def main():
      st.title("Login Page")
      menu = ["Home","Login","Signup"]
      choice = st.sidebar.selectbox("Menu",menu)
      
      if choice == "Home":
          st.subheader("Home") 
          st.title("GARBAGE MANAGEMENT APP")
          from PIL import Image
          img = Image.open("save earth from garbage.jpg") 
          st.image(img,width=600)
          st.subheader("About Us:")
          st.text("The aim of the project is to provide a better solution to waste management.")
          st.text("Instead of dumping waste to another area,") 
          st.text("this app proposes to transport waste to those who require it for useful purposes.") 
          st.text("Hence the 'bekaar' is delivered to the companies who 'sweekar' it.")
          st.subheader("Importance")
          st.subheader("Working")
          st.text("Our website involves a total of 3 steps:")
          st.text("1)Collection of waste from the user. The waste collected is divided in 5 Categories : ")
          st.text("Paper, Plastic, Organic, Glass, Metal. The users can submit waste that")
          st.text("2)The delivery of the waste from the user to the company where the latter can order")
          st.text("the waste materials they want to use/process, right to their doorstep.")

          st.text("3)Utilisation of Waste : The company now, uses the waste by amicably collecting it,")
          st.text("profusely processing it and efficiently recycling it. (for example: A packaging company ")
          st.text(" may require old newspaper/books, an animal farm may require organic wastes and so on.)")
          st.sidebar.header("Contact Us:xxxxxxxxxxx")
          st.sidebar.header("Contact Us:xxxxxxxxxxx@gmai.com")














      elif choice == "Login":
          st.subheader("Login Section")
          username = st.sidebar.text_input("User Name")
          password = st.sidebar.text_input("password",type='password')
          if st.sidebar.checkbox('Login'):
              st.success("Logged In as {}".format(username))
              task = st.selectbox("Task",["Role","Waste Giver","Waste Taker"])
              if task =="Task":
                  st.subheader("Add your Role")
              elif task == "Waste Giver":
                  st.subheader("Waste Giver")
              elif task == "Waste Taker":
                  st.subheader("Waste Taker")  






      elif choice == "Signup":
          st.subheader("Create New Account")
          new_user = st.text_input("Username")
          new_password = st.text_input("Password",type='password')
          
          
          if  st.button("signup"):
              st.success("You have successfully created an account")
              st.info("Goto Login Menu to Login")  
               


if _name_ == '_main_':
    main()