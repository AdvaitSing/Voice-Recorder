import pyaudio
import wave

# Define the audio format.
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Create an audio object.
audio = pyaudio.PyAudio()

# Open a stream to record from the microphone.
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=1024)

# Start recording.
print("Recording...")
frames = []
for i in range(0, int(RATE / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

# Stop recording.
print("Done recording.")
stream.close()

# Save the recorded data to a file.
wavefile = wave.open("output.wav", "wb")
wavefile.setnchannels(CHANNELS)
wavefile.setsampwidth(audio.get_sample_size(FORMAT))
wavefile.setframerate(RATE)
wavefile.writeframes(b"".join(frames))
wavefile.close()

# Close the audio object.
audio.terminate()
