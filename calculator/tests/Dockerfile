
FROM python:3.12
# Means we all the things we need to have python in the container

WORKDIR /app

ADD . /app

# The needed file

# RUN pip install unittest
# Requirementsdef print_text():


CMD [ "python", "./calculator_tests.py" ]
# The entry command when stsrting the container, simply runs main file

# After that in terminal you need to buill an  image, insert:
# 1.docker build -t <name of image>
# 2. docker run <name of image> (if there is no input option)/
# docker run -t -i <name of image> (if there is an nput option) - i: interactive mode/t: sudo terminal

