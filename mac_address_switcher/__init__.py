#!/usr/bin/python
# -*- coding: utf-8 -*-

from .helpers import get_current_node, user_is_root, yes_or_no, relaunch_with_sudo


def switch():
    # Sudo check
    if not user_is_root():
        if yes_or_no('Please launch with sudo, re-launch now?', default=True):
            relaunch_with_sudo()
        else:
            exit()


