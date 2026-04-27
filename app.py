import streamlit as st
from api_calling import note_generator,audio_transcription
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload Up to 3 Images to generate note summary and quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")

    # images
    images = st.file_uploader(
       "Upload the photos of your notes",
       type=['jpg','jpeg','png'],
       accept_multiple_files = True
                     )
    
     # converting streamlit image to pillow image that is readable to machine
    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded images")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

# difficulty

    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index = None
        )
    
    if selected_option:
        st.markdown(f"Your selected {selected_option} as difficulty of your quiz")

    pressed = st.button("Click the button to initiate AI ",type ="primary")

if pressed:
    if not images:
        st.error("You must at least Upload a images")
    elif not selected_option:
        st.error("You must select difficulty")

    if images and  selected_option:


        # note

        with st.container(border = True):
            st.subheader("Your note")

            with st.spinner("AI is writing notes for you"):

                generated_notes=note_generator(pil_images)
                st.markdown(generated_notes)


        # Audio transcript
        with st.container(border = True):
            st.subheader("Audio Transcription")

            with st.spinner("AI is transcribing the audio notes for you"):

                # clearing the markdown

                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")
                generated_notes = generated_notes.replace("$","")


                Audio_transcript=audio_transcription(generated_notes)
                
                st.audio(Audio_transcript)

        # quiz
        with st.container(border = True):
            st.subheader(f"Quiz {selected_option} Difficulty")

            with st.spinner("AI is creating Quizzes  for you"):
                
                st.text("Note will be shown here")
