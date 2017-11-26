=================
Ziggo Mediabox XL
=================


.. image:: https://img.shields.io/pypi/v/ziggo_mediabox_xl.svg
        :target: https://pypi.python.org/pypi/ziggo_mediabox_xl

.. image:: https://img.shields.io/travis/b10m/ziggo_mediabox_xl.svg
        :target: https://travis-ci.org/b10m/ziggo_mediabox_xl

.. image:: https://readthedocs.org/projects/ziggo-mediabox-xl/badge/?version=latest
        :target: https://ziggo-mediabox-xl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/b10m/ziggo_mediabox_xl/shield.svg
     :target: https://pyup.io/repos/github/b10m/ziggo_mediabox_xl/
     :alt: Updates


Installation
------------

From PyPI
~~~~~~~~~

Assuming you already are inside a virtualenv:

.. code-block:: bash

    pip install ziggo_mediabox_xl

From Git
~~~~~~~~

Create a new virtualenv (if you are not already in one) and install the
necessary packages:

.. code-block:: bash

    git clone https://github.com/b10m/ziggo_mediabox_xl.git
    cd ziggo_mediabox_xl
    mkvirtualenv ziggo_mediabox_xl
    pip install -r requirements.txt

Usage
-----

This quick example will connect to the IP address listed, verify the box
is turned on and sends NUM_3, NUM_0, and NUM_2 to the device. This will
result in the same action as pressing 302 on your remote control (the
Disney Jr. channel will be selected).

.. code-block:: python

    from ziggo_mediabox_xl import ZiggoMediaboxXL

    box = ZiggoMediaboxXL('aaa.bbb.ccc.ddd')
    if box.turned_on():
        box.send_keys(['NUM_3', 'NUM_0', 'NUM_2'])
