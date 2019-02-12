#!/usr/bin/env python
import requests
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for, abort
import time
import sms
import smtplib, ssl

app = Flask(__name__)


def main():
    text_sent = False
    first_connect = False
    while 1 == 1:
        time.sleep(10)
        try:
            r = requests.get('http://127.0.0.1:5000/heartbeat')
            if r.content == b'working':
                print("Connected: " + str(datetime.now()))
                text_sent = False
                firstConnect = True
            else:
                print("INVALID RETURN DATA " + str(datetime.now()))
        except Exception:
            print("DISCONNECTED SYSTEM ADMIN ASSISTANCE NEEDED " + str(datetime.now()))
            if not text_sent and not first_connect:
                sms.send_sys_admin_text()
                send_email.send_sys_admin_email()
                text_sent = True


main()
