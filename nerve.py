#!/usr/bin/python3
import subprocess


def ping(host='127.0.0.1'):
    ping_switch = '-c'
    ping_count = '1'
    ping_destination = host
    ping_command = 'ping' + ' ' + ping_switch + ' ' + ping_count + ' ' + ping_destination
    ping_output = subprocess.run(ping_command, shell=True)
    return ping_output.returncode


class Validation:
    def __init__(self, validation_type, destination='brandbil.dk'):
        if validation_type == 'ping': self.returncode = ping(destination)
        self.destination = destination
