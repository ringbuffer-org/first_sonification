

# 1: Clone Repository

    $ git clone https://github.com/anwaldt/first_sonification.git
    $ cd python_sequencing

----

# 2: Launch Pd Synth

Launch the Pd patch and:

- activate DSP (Media dropdown menu)
- click the 'listen 6667' message to active

----

# Python Control

## Create and Activate Virtual Environment

    $ python3 -m venv sonification_venv
    $ source sonification_venv/bin/activate

## Install Dependencies

    $ pip3 install numpy
    $ pip3 install python-osc

## Run Script

The script can be called like this:

    $ python3 sequencer.py PATH_TO_FILE --col 1 --interval 100

