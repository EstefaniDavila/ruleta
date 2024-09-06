# # import numpy as np
# # from scipy.io.wavfile import write

# # sampling_rate = 44100
# # duration = 1.0  # en segundos
# # frequency = 440.0  # en Hz

# # t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# # audio = 0.5 * np.sin(2 * np.pi * frequency * t)

# # write('spin_sound.wav', sampling_rate, audio.astype(np.float32))
# import numpy as np
# from scipy.io.wavfile import write

# # Generar un tono diferente para el sonido de ganar
# sampling_rate = 44100
# duration = 1.0  # en segundos
# frequency = 880.0  # en Hz, tono más alto

# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# audio = 0.5 * np.sin(2 * np.pi * frequency * t)

# # Guardar como archivo WAV
# write('win_sound.wav', sampling_rate, audio.astype(np.float32))
# import numpy as np
# from scipy.io.wavfile import write

# # Generar un tono diferente para el sonido de perder
# sampling_rate = 44100
# duration = 1.0  # en segundos
# frequency = 220.0  # en Hz, tono más bajo

# t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
# audio = 0.5 * np.sin(2 * np.pi * frequency * t)

# # Guardar como archivo WAV
# write('lose_sound.wav', sampling_rate, audio.astype(np.float32))
import numpy as np
from scipy.io.wavfile import write

# Parámetros generales
sampling_rate = 44100
duration = 1.0  # Duración total del sonido

# Crear una señal que varíe en frecuencia para simular un giro
frequencies = [440.0, 554.37, 659.25, 440.0]  # Frecuencias en Hz
segments = len(frequencies)
segment_duration = duration / segments  # Duración de cada segmento

# Generar el sonido
audio = np.array([])

for freq in frequencies:
    t = np.linspace(0, segment_duration, int(sampling_rate * segment_duration), endpoint=False)
    segment = 0.5 * np.sin(2 * np.pi * freq * t)
    audio = np.concatenate((audio, segment))

# Guardar el sonido como archivo WAV
write('spin_sound.wav', sampling_rate, audio.astype(np.float32))
