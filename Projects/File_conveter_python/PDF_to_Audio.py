from gtts import gTTS
from PyPDF2 import PdfReader
import pygame

def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file,'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_audio(text,output_file):
    tts = gTTS(text)
    tts.save(output_file)

def play_audio(text,output_file):
    tts = gTTS(text)
    tts.save(output_file)

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    
    
    while pygame.mixer.music.get_busy():
        continue

def stop_audio():
    pygame.mixer.music.stop()
   
pdf_file = "./SQL connectivity in Python1.pdf"
output_audio_file = "./SQL connectivity in Python1.pdf"

text = pdf_to_text(pdf_file)
text_to_audio(text,output_audio_file)

play_audio(output_audio_file)


