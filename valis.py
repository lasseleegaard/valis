#!/usr/bin/python3
import socket
from subprocess import run


def ping(host="127.0.0.1"):
    if host != "":
        ping_switch = "-c"
        ping_count = "1"
        ping_destination: str = host
        ping_command = (
            "ping" + " " + ping_switch + " " + ping_count + " " + ping_destination
        )
        ping_output = run(ping_command, shell=True)
        return ping_output.returncode
    return 0


def tcp(host="brandbil.dk", port=22):
    if host == "":
        return 1
    if socket.getfqdn(host) != host:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_connection:
            tcp_connection.connect((host, port))
            tcp_connection.close()
        return 0


class Validation:
    def __init__(self, validation_type, destination="brandbil.dk", port=22):
        if validation_type == "ping":
            self.returncode = ping(destination)
        if validation_type == "tcp":
            self.returncode = tcp(destination, port)
        self.destination = destination
