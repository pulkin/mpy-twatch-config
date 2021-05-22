mpy-twatch-config
=================

This repository contains `boot.py` for [T-Watch 2020](https://t-watch-document-en.readthedocs.io/en/latest/introduction/product/2020.html), programmable smart watch based on ESP32.
Applies to [micropython](micropython.org) firmware only.

What for
--------

- Charging parameters.
  Default charging parameters are 4.2V / 500mA while the stock firmware [sets the latter](https://github.com/Xinyuan-LilyGO/TTGO_TWatch_Library/blob/396d5db84b1b450c9c92939902049c9658bfc048/src/TTGO.h#L1371) to 300mA.
  To make sure high currents do not damage the battery this script sets the charging current to the minimal value 300mA.

How to use
----------

Copy `boot.py` to the board and the settings will apply on the next reboot.
```bash
rshell --port /dev/ttyUSB0 cp boot.py /pyboard/
```
Adjust the file as you need it.

License
-------

BSD 2-clause

