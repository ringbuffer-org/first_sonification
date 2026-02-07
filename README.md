

# 1: Clone Repository

    $ git clone https://github.com/anwaldt/first_sonification.git
    $ cd python_sequencing


# 2: Launch Pd Synth



# Python Control

## Create and Activate Virtual Environment

    $ python3 -m venv sonification_venv
    $ source sonification_venv/bin/activate

## Install pythonosc

    $ pip3 install numpy
    $ pip3 install python-osc

## Run Script

    $ python3 sequencer.py ../../fnc150.csv --col 1 --interval 100

