#!/usr/bin/env python3
import os
import pathlib
import random


def play():
    bash_history_path = pathlib.Path().home().joinpath(".bash_history")
    bash_history_lines = bash_history_path.read_bytes().split(b"\n")
    bash_history_line = random.choice(bash_history_lines).decode("utf-8")
    print("You've won:","\"{}\".".format(bash_history_line),"Congrats!")
    os.system(bash_history_line)


if __name__ == "__main__":
    play()
