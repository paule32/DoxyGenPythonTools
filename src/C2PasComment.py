# ----------------------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2024 Jens Kallup
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------------
import os
import re

def convert_c_to_pascal_comments_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Ersetze /** durch (**
    content = re.sub(r"/\*\*", "(**!", content)
    # Ersetze */ durch *)
    content = re.sub(r"\*/", "*)", content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Konvertiert: " + filepath)

def convert_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".pas", ".pp", ".p")):
                convert_c_to_pascal_comments_in_file(os.path.join(root, file))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Verwendung: python c2pascal.py <datei oder ordner>")
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            convert_c_to_pascal_comments_in_file(path)
        elif os.path.isdir(path):
            convert_directory(path)
        else:
            print("Pfad nicht gefunden:", path)
