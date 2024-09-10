import os
import playsound
import pyt_play
import pyt_query

def main():
    title_n = input("Which song wanna listen? _ ")
    artist_n = input("By whom? _ ")
    links = pyt_query.ret_3_first_links(title_n, artist_n)
    directory = os.getcwd()
    filename_in = pyt_play.yt_dl(f"https://www.youtube.com/watch?v={links[0]}", directory)
    base, ext = os.path.splitext(filename_in)
    file_in = f"{directory}\\{filename_in}"
    file_out = f"{directory}\\{base}.mp3"
    pyt_play.mp4_to_mp3(file_in, file_out)
    os.remove(file_in)
    print("Enjoy!")
    playsound.playsound(file_out)

if __name__ == "__main__":
    main()
