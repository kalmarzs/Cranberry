#!/usr/bin/env python3

import vlc

url = 'http://prem1.rockradio.com:80/bluesrock?9555ae7caa92404c73cade1d'
instance=vlc.Instance()
media=vlc.MediaPlayer(url)
media.play()