import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

# Designing the interface
st.title("Not a Lizard? Classification App")
# For newline
st.write('\n')

image = Image.open('intro.png')
show = st.image(image, use_column_width=True)

st.sidebar.title("Upload Image")

#Disabling warning
st.set_option('deprecation.showfileUploaderEncoding', False)
#Choose your own image
uploaded_file = st.sidebar.file_uploader(" ",type=['png', 'jpg', 'jpeg', 'bmp'] )

if uploaded_file is not None:
    
    test_image = Image.open(uploaded_file)
    show.image(test_image, 'Uploaded Image', use_column_width=True)
    
    img = np.asarray(test_image)

    resize = tf.image.resize(img, (256,256))



st.sidebar.write('\n')

@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model('newtslizards.h5')
  return model

model = load_model()

if st.sidebar.button("Click Here to Classify"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Please upload an Image to Classify")
    
    else:
        
        with st.spinner('Classifying ...'):


          current_prediction = model.predict(np.expand_dims(resize/255, axis=0))

          probability = "{:.3f}".format(float(current_prediction*100))
        
        st.sidebar.header("Algorithm Predicts: ")
           
        if current_prediction > 0.5:
            
            st.sidebar.write("Newt!", '\n' )
                             
        else:
            st.sidebar.write("Lizard! ",'\n')
          
        st.sidebar.write('Probability: ',probability,'%')
       