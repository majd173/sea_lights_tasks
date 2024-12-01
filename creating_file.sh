#!/bin/bash

file="info_file.txt"
touch $file
echo "This file contains some details about using basic linux command for writing a simple text in the terminal" > $file  
echo "1. Right click in the desktop screen" >> $file
echo "2. Open in terminal" >> $file
echo '3. write: (echo "hello world!") NOTE: without parentheses' >> $file
echo "hello world! will appear in your terminal in a single line" >> $file
cp $file ~/Documents/copy_of_info_file.txt
echo "A file named: $file, was created in the desktop dir."
echo "A copy of the $file was added to Documents dir under name: copy of_info_file.txt"

