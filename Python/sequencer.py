#!/usr/bin/env python3

###############################################################################
#
#
"""Author: HvC"""
"""Date: 2020-08-30"""
#
###############################################################################

import numpy
import time

import argparse
import csv

from pythonosc import udp_client


###############################################################################
# Argument Parser
###############################################################################

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument(
    "--interval",
    type=float,
    default=100.0,
    help="milliseconds between rows"
)
parser.add_argument(
    "--port",
    type=int,
    default=6667,
    help="OSC port (Pure Data netreceive)"
)
parser.add_argument(
    "--col",
    type=int,
    default=0,
    help="column index to play (0-based); default = column 0"
)

args = parser.parse_args()

path        = args.file
interval_ms = args.interval
osc_port    = args.port
col         = args.col


###############################################################################
# Read Data
###############################################################################

data = []

with open(path) as f:
    for line in f:
        if line.strip():
            data.append([float(x) for x in line.strip().split(",")])

print("Read "+str(len(data))+" datapoints.")

###############################################################################
# Playback Loop
###############################################################################

target_OSC = udp_client.SimpleUDPClient("127.0.0.1", osc_port)

for i, row in enumerate(data):
    val = row[col]
    print('Sending: ', i, val)
    target_OSC.send_message("/val", val)
    time.sleep(interval_ms / 1000.0)
