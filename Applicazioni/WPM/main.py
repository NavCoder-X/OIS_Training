import curses
from curses import wrapper
import time
from src.utilitis import *

"""Tutti i file in Archivio sono AI generated per velocizzare il processo di scrittura, e sono stati creati con l'intento di essere difficili da scrivere, in modo da rendere più interessante il test."""

def main(stdscr):
    # inzio
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(1)
    stdscr.keypad(True)

    # keys
    backspace_keys = {curses.KEY_BACKSPACE, 127, 8}
    delete_keys = {curses.KEY_DC}
    tab = 9

    i = j = 0
    start_time = time.time()
    countChar = countErrori = 0
    file = getRandomFileName()
    stdscr.addstr(j,0,f"File: {file}")
    stdscr.addstr(j+1,0,"_" * 100)
    j+=2
    with open("archivio/" + file, "r") as f:
        
        for raw_line in f.readlines():
            if raw_line.startswith("//"):
                stdscr.addstr(j,0,raw_line[2:].rstrip("\n"), curses.color_pair(1))
                j+=1
                continue

            line = raw_line.rstrip("\n")
            countChar += len(line)
            i = 0
            stdscr.addstr(j,0,line)
            stdscr.move(j, i)
            stdscr.refresh()

            while True:
                stdscr.refresh()
                key = stdscr.getch()
                if i == len(line):
                    break

                elif key < 0 or key > 255:
                    continue

                elif key in backspace_keys or key in delete_keys:
                    if i > 0:
                        i -= 1 
                        stdscr.addstr(j,i,line[i])
                    stdscr.move(j, i)
                    continue

                # caso in cui sia tab
                if key == tab:
                    key = ' '
                    for _ in range(4):
                        if key == line[i]:
                            stdscr.addstr(j,i,key,curses.color_pair(1))
                        else:
                            stdscr.addstr(j,i,key,curses.color_pair(2))
                            countErrori += 1
                        i+=1
                    stdscr.move(j, i)
                    continue

                # controllo se è un carattere valido
                key = chr(key)
                if key == line[i]:
                    stdscr.addstr(j,i,key,curses.color_pair(1))
                else:
                    stdscr.addstr(j,i,key,curses.color_pair(2))
                    countErrori += 1
                i+=1
                stdscr.move(j, i)
            j+=1

    end_time = time.time()
    elapsed_time = end_time - start_time
    WPM = (countChar / elapsed_time) * 60 / 5
    stdscr.addstr(j+1, 0, f"Tempo: {elapsed_time:.2f} secondi, WPM: {WPM:.2f} | Errori: {countErrori}")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)