from gtts import gTTS
import os

text = "Fidelity Investments Inc., commonly referred to as Fidelity, earlier as Fidelity Management & Research or FMR, is an American multinational financial services corporation based in Boston, Massachusetts."

tts = gTTS(text)

name = 'v' + '.mp3'
tts.save(name)

os.system('start "' + name)

