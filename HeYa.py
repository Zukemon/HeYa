from moviepy.editor import *
# import animation
# import time
from flask import flash
import os
import sys
# import cv2
from flask import (
    request)

class Heya(object):
    def __init__(self, text = "HeYa!"):
        self.text = text


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text


    def merge(self):
        # print("Select a theme: (1) Summer, (2) Winter, or (3) Atumn")
        # num = int(input())
        ans = int(request.form.get("maya"))

        num = ans
        
        if num == None:
            backG = VideoFileClip("static/mov/autumn/summer_bck1.mp4")
            emoji = VideoFileClip("static/mov/autumn/summer_emojs.mov", has_mask=True)
            return backG, emoji
        elif num == 1:
            backG = VideoFileClip("static/mov/summer/summer_bck1.mp4")
            emoji = VideoFileClip("static/mov/summer/summer_emojs.mov", has_mask=True)
            return backG, emoji
        elif num == 2:
            backG = VideoFileClip("static/mov/spring/spring_bck1.mp4")
            emoji = VideoFileClip("static/mov/spring/spring_petals.mov", has_mask=True)
            return backG, emoji
        elif num == 3:
            backG = VideoFileClip("static/mov/autumn/autumn_bck1.mp4")
            emoji = VideoFileClip("static/mov/autumn/autumn_leaves.mov", has_mask=True)
            return backG, emoji
        elif num == 4:
            backG = VideoFileClip("static/mov/winter/winter_bck1.mp4")
            emoji = VideoFileClip("static/mov/winter/winter_flakes.mov", has_mask=True)
            return backG, emoji
        else:
            raise ValueError

    def splitter(self, words):        
        words = str(words).split()
        count = 0
        b = []
        
        for i in words:
            count += 1
            b.append(i)
            if count > 6:        
                one = " ".join(b[0:7])
                two = " ".join(b[7:14])
                three = " ".join(b[14:21])

        return str(one), str(two), str(three)

def main():
    try:
        cuz = Heya()
                
        vid1, vid2 = cuz.merge()
        
        # hey = str(cuz.text)
        hey = request.form.get("gaya")
        cap = hey.split()
        count = 0
        for _ in cap:
            count += 1
            if count > 10:
                n = 30
                one, two, three = cuz.splitter(hey)
            elif count < 5:
                n = 50
                one, two, three = hey, " ", " "
            else:
                n = 40
                one, two, three = hey, " ", " "
        
        txt_clipA = ( TextClip(one, fontsize=n, color='white', font="Courier")
                .set_position(("center",220))
                .set_duration(20) )
        txt_clipB = ( TextClip(two, fontsize=n, color='white', font="Courier")
                    .set_position(("center",250))
                    .set_duration(20) )
        txt_clipC = ( TextClip(three, fontsize=n, color='white', font="Courier")
                    .set_position(("center",280))
                    .set_duration(20) )

        # creating title from message text
        title = str(one).split()

        title = "_".join(title[:2]).capitalize()

        homeDir = os.path.expanduser("~/Downloads")

        # flash("Rendering card.")
        # long_running_function()
        result = CompositeVideoClip([vid1, txt_clipA, txt_clipB, txt_clipC, vid2]) # Overlay text on video
        vid_name = f"{homeDir}/{title}.webm"
        result.write_videofile(vid_name, fps=25) # Many options...
        
    except ValueError:
        sys.exit


if __name__ == "__main__":
    main()