import yt_dlp
import openai

openai.api_key = "SUA_CHAVE_AQUI"

def baixar_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.mp3",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "audio.mp3"

def transcrever(caminho):
    with open(caminho, "rb") as f:
        return openai.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f,
            response_format="text",
            language="pt"
        )

if __name__ == "__main__":
    url = input("Cole a URL do vídeo: ")
    texto = transcrever(baixar_audio(url))
    print("\n📜 Transcrição:\n", texto)