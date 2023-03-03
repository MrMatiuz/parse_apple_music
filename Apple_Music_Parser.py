
import xml.etree.ElementTree as EL
import numpy as np


def get_song(xml_element):
    artist = np.nan
    song = np.nan
    artist_num = np.nan
    song_num = np.nan
    for i, key in enumerate(xml_element):
        if key.text == 'Name':
            song_num = i + 1
        if i == song_num:
            song = key.text

        if key.text == 'Artist':
            artist_num = i + 1
        if i == artist_num:
            artist = key.text

    return [artist, song]


def get_playlist(file_name='Library.xml'):
    tree = EL.parse(file_name)
    playlist = []

    for i in tree.find('dict/dict'):
        if i.tag == 'dict':
            playlist += [get_song(i)]
            
    return playlist


def write_txt(playlist, file_name='myplaylist'):
    with open(file_name + '.txt', 'w') as f:
        for line in playlist:
            f.write(" - ".join(line))
            f.write("\n")

if __name__ == '__main__':
    write_txt(get_playlist())

