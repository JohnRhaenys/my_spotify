# My Spotify #

my_spotify is a music player software that aims to provide a complete and ad-free listening experience, both online and offline.

It uses YouTube as the host and allows users to search for, play, and add videos to their playlists, providing access to a wider range of content,
including podcasts and other audio-only content that Spotify itself doesn't have.

## Features ##
- Search for YouTube videos using the search bar 
  - By default, the first 10 videos on YouTube are listed
- Open the searched video on YouTube itself (the user is redirected to YouTube through the browser)
- Create multiple playlists
- Add videos to playlists
- Remove videos from playlists
- Ad-free listening experience
- Works offline (since the videos are downloaded in mp3 format, the user can listen to songs without an internet connection)
- Graphical interface similar to Spotify's

## Technologies Used ##
- PyQt5 for the graphical interface
- SQLAlchemy and MySQL to store information about playlists, songs, and the paths of the mp3 files
- "youtubesearchpython" module to find YouTube videos
- "pytube" module to download YouTube videos in mp3 format

## Screenshots ##
![Screenshot from 2022-12-17 16-14-50](https://user-images.githubusercontent.com/29712183/208261558-3de0407f-e899-40de-80d6-0d31c08e8344.png)

![Screenshot from 2022-12-17 16-15-16](https://user-images.githubusercontent.com/29712183/208262961-4f35dea2-9b96-48a4-8d8e-ed56c0b76519.png)

![Screenshot from 2022-12-17 16-15-23](https://user-images.githubusercontent.com/29712183/208262980-1aac6c8c-c72d-4ac2-ad04-ef7975640d1f.png)

![Screenshot from 2022-12-17 16-15-32](https://user-images.githubusercontent.com/29712183/208262993-ac53e323-f640-4d00-99bc-608c557d41ed.png)


## Installation ##
1) Install all dependencies:
    - anyio==3.6.1
    - beautifulsoup4==4.11.1
    - certifi==2022.6.15
    - charset-normalizer==2.1.1
    - docopt==0.6.2
    - greenlet==1.1.3
    - h11==0.12.0
    - httpcore==0.15.0
    - httpx==0.23.0
    - idna==3.3
    - mysqlclient==2.1.1
    - numpy==1.23.4
    - pandas==1.5.1
    - pipreqs==0.4.11
    - PyMySQL==1.0.2
    - PyQt5==5.15.7
    - PyQt5-Qt5==5.15.2
    - PyQt5-sip==12.11.0
    - PyQt5-stubs==5.15.6.0
    - python-dateutil==2.8.2
    - pytube==12.1.0
    - pytz==2022.6
    - requests==2.28.1
    - rfc3986==1.5.0
    - six==1.16.0
    - sniffio==1.3.0
    - soupsieve==2.3.2.post1
    - SQLAlchemy==1.4.40
    - urllib3==1.26.12
    - yarg==0.1.9
    - youtube-search-python==1.6.6
    
2) Setup a MySQL connection with the following credentials:
    - username: admin
    - password: 1234
    - server: localhost
    - database name: my_spotify
 
3) Execute the main.py file 
