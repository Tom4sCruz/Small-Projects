import yt_dlp


def dwn_video(url, output_path="~/Downloads"):
    ydl_opts = {
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]',  # Forces WebM
        'outtmpl': f'{output_path}%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def dwn_audio(url, output_path="~/Downloads"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',    # Forces MP3
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])




if __name__ == "__main__":
    link = input("Paste the URL of the video you want to download: ")
    option = input("(0) Video, (1) Audio: (Default=0) ")
    option = 0 if option == "" else int(option)
    try:
        if option == 0:
            dwn_video(link, "~/Media/")
            print("\033[92mThe video was downloaded successfully!\033[0m")
        else:
            dwn_audio(link, "~/Media/")
            print("\033[92mThe audio was downloaded successfully!\033[0m")

    except:
        print("\033[91mFailed to download the video. Try again!\033[0m")
        

