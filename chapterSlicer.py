import pydub

def trim_mp3(idx):
    start = songsData[idx][1]*1000
    end = songsData[idx+1][1]*1000
    originalSong[start:end].export(f"/Users/tushar/Downloads/Car Songs Playlist/KK/(unamplified) {songsData[idx][0]}.mp3")

songsData = []

for i in range(15):#number of chapters you want
    name, time = input("Enter: ").split(sep='|')#Copy paste the part from description which has the names+timestamps
    time = [int(i) for i in time.split(sep=":")]
    time = time[0]*3600 + time[1]*60 + time[2]
    songsData.append([name.title(), time])

originalSong = pydub.AudioSegment.from_mp3('/Users/tushar/Downloads/Car Songs Playlist/KK/[T-Series] Evergreen Hits of KK (Audio Jukebox) ｜ Remembering the Golden Voice ｜ T Series - Bhushan Kumar.mp3')
for i in range(len(songsData)-1):
    trim_mp3(i)
    print(f"Done with {songsData[i][0]}: {i+1}/15")
