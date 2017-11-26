# -*- coding: utf-8 -*-

import socket
import requests


class ZiggoMediaboxXL(object):
    """
    Ziggo Mediabox XL object.
    Library to command the Ziggo Mediabox XL.
    """

    def __init__(self, ip):
        self._ip = ip
        self._port = {"state": 62137, "cmd": 5900}
        self._channels_url = 'https://restapi.ziggo.nl/1.0/channels-overview'
        self._fetch_channels()
        self._keys = {
            "POWER": "E0 00", "OK": "E0 01", "BACK": "E0 02",
            "CHAN_UP": "E0 06", "CHAN_DOWN": "E0 07",
            "HELP": "E0 09", "MENU": "E0 0A", "GUIDE": "E0 0B",
            "INFO": "EO 0E", "TEXT": "E0 0F", "MENU1": "E0 11",
            "MENU2": "EO 15", "DPAD_UP": "E1 00",
            "DPAD_DOWN": "E1 01", "DPAD_LEFT": "E1 02",
            "DPAD_RIGHT": "E1 03", "PAUSE": "E4 00", "STOP": "E4 02",
            "RECORD": "E4 04", "FWD": "E4 05", "RWD": "E4 07",
            "MENU3": "E4 07", "ONDEMAND": "EF 28", "DVR": "EF 29",
            "TV": "EF 2A"}
        for i in range(10):
            self._keys["NUM_{}".format(i)] = "E3 {:02d}".format(i)

    def _fetch_channels(self):
        """Retrieve Ziggo channel information."""
        json = requests.get(self._channels_url).json()
        self._channels = {c['channel']['code']: c['channel']['name']
                          for c in json['channels']}

    def channels(self):
        return self._channels

    def test_connection(self):
        """Make sure we can reach the given IP address."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if sock.connect_ex((self._ip, self._port['cmd'])) == 0:
                return True
            else:
                return False
        except socket.error:
            raise

    def turned_on(self):
        """Update and return switched on state."""
        self.update_state()
        return self.state

    def update_state(self):
        """Find out whether the media box is turned on/off."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if sock.connect_ex((self._ip, self._port['state'])) == 0:
                self.state = True
            else:
                self.state = False
            sock.close()
        except socket.error:
            raise

    def send_keys(self, keys):
        """Send keys to the device."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self._ip, self._port['cmd']))
            # mandatory dance
            version_info = sock.recv(15)
            sock.send(version_info)
            sock.recv(2)
            sock.send(bytes.fromhex('01'))
            sock.recv(4)
            sock.recv(24)
            # send our command now!
            for key in keys:
                if key in self._keys:
                    sock.send(bytes.fromhex("04 01 00 00 00 00 " +
                                            self._keys[key]))
                    sock.send(bytes.fromhex("04 00 00 00 00 00 " +
                                            self._keys[key]))
            sock.close()
        except socket.error:
            raise
