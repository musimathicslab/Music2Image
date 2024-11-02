from transformers import pipeline
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
from pydub import AudioSegment
import time
from torch import autocast

# Specificare il percorso completo di ffmpeg se pydub non riesce a trovarlo
#AudioSegment.converter = ""
#AudioSegment.ffprobe = ""

# Carica il modello Whisper (versione GPU)
whisper_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base", device="cuda")

# Carica il modello Stable Diffusion (versione GPU e ottimizzato)
model_id = "runwayml/stable-diffusion-v1-5"
text_to_image_pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
text_to_image_pipe.enable_sequential_cpu_offload()
#Safety cheker disabilitato
text_to_image_pipe.safety_checker = None

# Carica il modello di riassunto (versione GPU)
summarization_pipeline = pipeline("summarization", model="t5-small", tokenizer="t5-small", device="cuda")


# Funzione per convertire da mp3 a wav
def convert_mp3_to_wav(mp3_path):
    audio = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path


# Funzione per sintetizzare il testo
def summarize_text(text):
    max_length = min(len(text) + 10, 50)
    summary = summarization_pipeline(text, max_length=max_length, min_length=5, do_sample=False)[0]['summary_text']
    return summary


# Funzione per generare l'immagine con ottimizzazioni
def generate_image_optimized(text):
    # Riduci il numero di passi di inferenza a 25 (per migliorare la velocità)
    generated_image = text_to_image_pipe(text, num_inference_steps=25).images[0]
    return generated_image


# Funzione per trascrivere segmenti di audio in tempo reale
def transcribe_audio_in_intervals(audio_path, interval_duration=20):
    # Conversione in mp3 se necessario
    if (audio_path.endswith(".mp3")):
        audio_path = convert_mp3_to_wav(audio_path)

    # Carica l'audio e ottieni la sua durata
    audio = AudioSegment.from_wav(audio_path)
    total_duration = len(audio) / 1000  # Durata totale in secondi

    current_position = 0
    accumulated_text = ""

    # Loop per processare l'audio in segmenti
    while current_position < total_duration:
        # Estrai segmento di audio
        segment = audio[current_position * 1000:(current_position + interval_duration) * 1000]
        segment_path = "temp_segment.wav"
        segment.export(segment_path, format="wav")

        # Trascrivi il segmento
        transcribed_segment = whisper_pipeline(segment_path, return_timestamps=True)["text"]

        # Aggiungi il testo trascritto al testo accumulato
        accumulated_text += " " + transcribed_segment
        print("testo accumulato:", accumulated_text)
        # Sintetizza il testo accumulato
        summarized_text = summarize_text(accumulated_text)
        print("testo sintetizzato:", summarized_text)
        # Genera l'immagine ottimizzata
        generated_image = generate_image_optimized(summarized_text)

        # Salva e mostra l'immagine generata
        image_path = f"generated_image_{current_position}.png"
        generated_image.save(image_path)
        generated_image.show()

        # Simula il tempo reale (attendi per l'intervallo di tempo successivo)
        time.sleep(interval_duration)

        current_position += interval_duration


# Specificare il path dell'audio
audio_path = ""
# Esegui il processo
transcribe_audio_in_intervals(audio_path)
