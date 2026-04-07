import streamlit as st
import requests
import numpy as np
import sounddevice as sd
import io
from scipy.io.wavfile import write
import wave
import openai
from openai import OpenAI
client = OpenAI(api_key="jgihugr9hjA")



def speech_to_text(file_path):
    audio_file= open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file
    )
    print("transcript:")
    print(transcription.text)
    return transcription.text



def describe_image(image_url):
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "Describe this AI & ML related image technically and creatively."},
            {
              "type": "image_url",
              "image_url": {
                "url": image_url,
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )
    print("Chat GPT:")
    print(response.choices[0].message.content)
    return response.choices[0].message.content



def compare_descriptions(model_desc, user_desc):
    st.write(f"**AI's Description:** {model_desc}")
    st.write(f"**Your Description:** {user_desc}")
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
      {"role": "system", "content": "You are a Computer Science evaluator. You have a predefined technical description of an AI/ML image, and a user's transcribed speech describing the same image. Judge the user's technical understanding, accuracy, and explanation skills. Be supportive and helpful."},
      {"role": "user", "content": f"AI Description: {model_desc}\nUser Description: {user_desc}\nBased on these two, respond with feedback on what the user understood well and what they can improve."}
      ]
    )

    print(completion.choices[0].message.content)
    st.subheader('Feedback')
    st.write(f"Analysis: {completion.choices[0].message.content.strip()}")


def app():
    st.header('AI & ML Image Speech Comprehension')
    st.write('Generate an AI/ML concept image and speak about it for 10 seconds. The AI will evaluate your technical explanation!')

    if 'image_shown' not in st.session_state:
        st.session_state.image_shown = False
    if 'recording_started' not in st.session_state:
        st.session_state.recording_started = False
    if 'image_generated' not in st.session_state:
        st.session_state.image_generated = False

    # Start button to display the image
    if st.button('Generate AI/ML Image'):
        st.session_state.image_shown = True
        st.session_state.image_generated = False

    if st.session_state.image_shown:
        # Display the image
        if st.session_state.image_generated == False:
            with st.spinner("Generating an AI/ML image..."):
                response = client.images.generate(
                  model="dall-e-2",
                  prompt="A conceptual high-quality image representing a concept or place in Artificial Intelligence and Machine Learning, such as a futuristic data center, a neural network visualization, or robots working on data.",
                  size="1024x1024",
                  n=1,
                )
                image_url = response.data[0].url
                st.session_state.image_url=image_url
                st.session_state.image_generated = True
        
        st.image(st.session_state.image_url, caption='Describe this AI/ML concept.')
        st.subheader('You have to describe and talk about what you see in the image. Take your time to look and analyse the image, think about what you want to say, and then start.\nYou will have 10 seconds to speak about it.')

        if st.button('Start Talking (10 seconds)'):
            st.session_state.recording_started = True
            duration = 10  # seconds
            sample_rate = 44100  # Sample rate
            st.write('Recording started... speak now!')
            myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
            st.write('Recording Done!')
            st.session_state.recording_started = False
            # Convert the NumPy array to audio file
            st.write('Processing audio and generating feedback...')
            output_file = "output2.wav"
            with wave.open(output_file, 'w') as wf:
                wf.setnchannels(1)  # Stereo
                wf.setsampwidth(2)  # Sample width in bytes
                wf.setframerate(sample_rate)
                wf.writeframes(myrecording.tobytes())

            print(f"Audio saved to {output_file}")
            with st.spinner("Transcribing your speech..."):
                user_description = speech_to_text("output2.wav")
            with st.spinner("Analyzing image..."):
                model_description = describe_image(st.session_state.image_url)
            with st.spinner("Comparing descriptions..."):
                compare_descriptions(model_description, user_description)
