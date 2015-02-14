# -*- coding: utf-8 -*-
import uuid
import os
import sys


def get_current_node():
    node = uuid.getnode()
    hex_node = hex(node)
    particle_size = 2
    hex_list = [hex_node[j:j+particle_size].capitalize() for j in range(2, len(hex_node), particle_size)]
    return u':'.join(hex_list)


def is_user_root():
    return os.getuid() == 0


def yes_or_no(message, default=True):
    prompt = ' [y/N] ' if not default else ' [Y/n] '
    valid_inputs = {'yes': True, 'y': True,
                    'no': False, 'n': False}

    while 1:
        sys.stdout.write(message + prompt)
        answer = raw_input().strip().lower()

        if answer == '':
            return default

        elif answer in valid_inputs.keys():
            return valid_inputs.get(answer)

        else:
            sys.stderr.write('Incorrect input {input}.\n'.format(input=answer))


def relaunch_with_sudo():
    os.execvp("sudo", ["sudo"] + sys.argv)
