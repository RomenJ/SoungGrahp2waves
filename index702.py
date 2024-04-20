import numpy as np
import wave
import matplotlib.pyplot as plt

def read_audio(file_name):
    try:
        audio_file = wave.open(file_name, 'r')
        signal = audio_file.readframes(-1)
        soundwave = np.frombuffer(signal, dtype='int16')
        framerate = audio_file.getframerate()
        return soundwave, framerate
    except Exception as e:
        print(f"Error al leer el archivo {file_name}: {e}")
        return None, None

def normalize_waveform(soundwave):
    mean = np.mean(soundwave)
    std_dev = np.std(soundwave)
    normalized_waveform = (soundwave - mean) / std_dev
    return normalized_waveform

def plot_waveform(time, soundwave, color, label):
    plt.plot(time, soundwave, color=color, label=label, alpha=0.5)

def main():
    # Archivos de audio
    file_names = ['Goodmorn.wav', 'Lemmeatt.wav']

    # Leer y procesar los archivos de audio
    plt.figure(figsize=(12, 8))

    for i, file_name in enumerate(file_names, 1):
        soundwave, framerate = read_audio(file_name)
        if soundwave is not None:
            time = np.linspace(start=0, stop=len(soundwave) / framerate, num=len(soundwave))
            normalized_waveform = normalize_waveform(soundwave)

            # Colores alternativos para los gráficos
            colors = ['blue', 'red']
            color = colors[i - 1]

            # Etiquetas para los gráficos
            labels = ['Good Mor', 'Lemmeatt']
            label = labels[i - 1]

            # Graficar la forma de onda original
            plt.subplot(2, 2, i)
            plot_waveform(time, soundwave, color, label)
            plt.title(f"Original Sound Wave - {label}")
            plt.xlabel("Time (seconds)")
            plt.ylabel("Amplitude")
            plt.legend()

            # Graficar la forma de onda normalizada
            plt.subplot(2, 2, i + 2)
            plot_waveform(time, normalized_waveform, color, label)
            plt.title(f"Normalized Sound Wave - {label}")
            plt.xlabel("Time (seconds)")
            plt.ylabel("Normalized Amplitude")
            plt.legend()

    plt.tight_layout()
    plt.savefig('Nomalized and No Normalized of two Sound Waves')
    plt.show()

if __name__ == "__main__":
    main()
