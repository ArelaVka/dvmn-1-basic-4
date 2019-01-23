import os
import sys
from tinytag import TinyTag
from os.path import join, getsize
from itertools import groupby
from operator import itemgetter

def get_tags_by_artist(path, artist_filter):
    files = [
        os.path.join(root, name) for root, dirs, files in os.walk(path)
        for name in files
        ]
    albums = []
    for file in files:
        tag = TinyTag.get(file)
        if str(tag.artist).upper() == artist_filter.upper():
          albums.append(tag)
    return albums

def print_songs(albums):
    for key, group in groupby(albums, key=lambda x:x.album):
        print('{}:\n'.format(key))
        for item in group:
            print('Название: {}\nАльбом: {}\nИсполнитель: {}\n'.
              format(item.title, item.album, item.artist))

def main():
    path='music'
    if len(sys.argv) > 1:
        artist = sys.argv[1]
        music_library = get_tags_by_artist(path, artist)
        print_songs(music_library)
    else:
        sys.exit('Enter correct artist!')


if __name__ == '__main__':
    main()
