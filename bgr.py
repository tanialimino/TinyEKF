from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

with SB(uc=True, test=True) as sb:

    if True:
        url = "https://kick.com/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        sb.uc_gui_click_captcha()
        sb.sleep(1)
        sb.uc_gui_handle_captcha()
        sb.sleep(1)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        if sb.is_element_visible('#injected-channel-player'):
            maaga = sb.get_new_driver(undetectable=True)
            maaga.uc_open_with_reconnect(url, 5)
            maaga.uc_gui_click_captcha()
            maaga.uc_gui_handle_captcha()
            sb.sleep(10)
            if maaga.is_element_present('button:contains("Accept")'):
                maaga.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible('#injected-channel-player'):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)
    if True:
        url = "https://www.twitch.tv/brutalles"
        sb.uc_open_with_reconnect(url, 5)
        if sb.is_element_present('button:contains("Accept")'):
            sb.uc_click('button:contains("Accept")', reconnect_time=4)
        input_field = 'div[aria-label="Chat messages"]'
        if sb.is_element_visible(input_field):
            maaga = sb.get_new_driver(undetectable=True)
            maaga.uc_open_with_reconnect(url, 5)
            sb.sleep(10)
            if maaga.is_element_present('button:contains("Accept")'):
                maaga.uc_click('button:contains("Accept")', reconnect_time=4)
            while sb.is_element_visible(input_field):
                sb.sleep(10)
            sb.quit_extra_driver()
    sb.sleep(1)

