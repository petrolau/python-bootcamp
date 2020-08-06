playlist = {
    "title":"Sharp claws",
    "author":"Laura Petrola",
    "songs": 
    [
        {"title": "Psycho","artist":["Redvelvet"],"duration":3.5 },
        {"title": "Come see me","artist":["AOA"],"duration":3.5},
        {"title": "Snow","artist":["Surl"],"duration":3.5 }

    ]
}

for song in playlist['songs']:
    print(song['title'])

total_lenght = 0
for song in playlist['songs']:
    total_lenght+=song['duration']
print("Total lenght : {} mins".format(total_lenght))