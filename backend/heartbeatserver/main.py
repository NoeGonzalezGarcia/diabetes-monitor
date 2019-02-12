#!/usr/bin/env python
import requests
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for, abort
import time
import smtplib, ssl

app = Flask(__name__)


def main():
    email_sent = False
    while 1 == 1:
        time.sleep(2)
        try:
            r = requests.get('http://127.0.0.1:5000/heartbeat')
            if r.content == b'working':
                print("Connected: " + str(datetime.now()))
                email_sent = False
            else:
                print("INVALID RETURN DATA " + str(datetime.now()))
        except Exception:
            print("DISCONNECTED SYSTEM ADMIN ASSISTANCE NEEDED " + str(datetime.now()))
            if not email_sent:
                # send_sys_admin_email()
                email_sent = True




main()
