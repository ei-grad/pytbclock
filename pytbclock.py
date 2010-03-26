#!/usr/bin/env python
# coding: utf-8

import sys, time
import termbox

def draw_digit(tb, d, x, y, wx, wy, c=termbox.GREEN):

    digit = [ ['111', '101', '101', '101', '111'],
              ['001', '001', '001', '001', '001'],
              ['111', '001', '111', '100', '111'],
              ['111', '001', '111', '001', '111'],
              ['101', '101', '111', '001', '001'],
              ['111', '100', '111', '001', '111'],
              ['111', '100', '111', '101', '111'],
              ['111', '001', '001', '001', '001'],
              ['111', '101', '111', '101', '111'],
              ['111', '101', '111', '001', '111']  ]

    for i in range(3):
        for j in range(5):
            if digit[d][j][i] == '1':
                for i1 in range(wx):
                    for j1 in range(wy):
                        tb.change_cell(x + i * wx + i1, y + j * wy + j1,
                            32, termbox.BLACK, c) # 32 == ord(' ')

def draw_delimeter(tb, x, y, dx, dy, c=termbox.GREEN):
    
    for i in range(dx):
        for j in range(dy, 2 * dy)  + range(3 * dy, 4 * dy):
            tb.change_cell(x + i, y + j, u' ', termbox.BLACK, c)

class Clock(object):

    def __init__(self, tb, w=1):
        self.wx = w
        self.wy = w
        self.tb = tb

    def draw(self):
        
        # calculate dimensions
        
        max_w, max_h = self.tb.width(), self.tb.height()
        
        wx, wy = 1, 1
        while max_w > (wx + 1) * 27 + (wx + 1) * 2:
            wx += 1
        while max_h > (wy + 1) * 5 + (wy + 1) * 2:
            wy += 1

        dx, dy = wx, wy

        while max_w > wx * 27 + (dx + 1) * 2:
            dx += 1
        while max_h > wy * 5 + (dy + 1) * 2:
            dy += 1

        # drawing

        t = time.strftime("%H%M%S")

        y = dy
        x = dx
        draw_digit(self.tb, int(t[0]), x, y, wx, wy) # 1 digit
        x += 3 * wx + wx # digit and space
        draw_digit(self.tb, int(t[1]), x, y, wx, wy) # 2 digit
        x += 3 * wx + wx # digit and space
        draw_delimeter(self.tb, x, y, wx, wy) # :
        x += 2 * wx # delimeter and space
        draw_digit(self.tb, int(t[2]), x, y, wx, wy) # 3 digit
        x += 3 * wx + wx # digit and space
        draw_digit(self.tb, int(t[3]), x, y, wx, wy) # 4 digit
        x += 3 * wx + wx # digit and space
        draw_delimeter(self.tb, x, y, wx, wy) # :
        x += 2 * wx # delimeter and space
        draw_digit(self.tb, int(t[4]), x, y, wx, wy) # 5 digit
        x += 3 * wx + wx # digit and space
        draw_digit(self.tb, int(t[5]), x, y, wx, wy) # 6 digit
       

with termbox.Termbox() as tb:

    clock = Clock(tb)
    
    old_sec = time.localtime().tm_sec

    tb.clear()
    clock.draw()
    tb.present()

    run_app = True

    while run_app:
        event = tb.peek_event(100)
        if event:
            type, ch, key, mod, w, h = event
            if type == termbox.EVENT_KEY:
                run_app = False
            elif type == termbox.EVENT_RESIZE:
                tb.clear()
                clock.draw()
                tb.present()
        else:
            if old_sec != time.localtime().tm_sec:
                old_sec = time.localtime().tm_sec

                tb.clear()
                clock.draw()
                tb.present()

