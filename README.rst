A python3 compatible REST utility to retrieve Nagios status as a JSON object via REST.

Requirements
============

* python3.5 or greater
* tornado 5 or greater
* inotify-simple (so, it will probably run only in inotify-compatible environments)

Usage
=====

Clone this repository, run `pip install .`, then run `restgios -h` for the usage (i assure you, it's deadly simple) 

.. code::
   restgios -h
   usage: restgios [-h] [-p [SERVER_PORT]] [-s [STATUS_PATH]]

optional arguments:

  -h, --help            show this help message and exit
  -p [SERVER_PORT]      server will listen at specified port (8979)
  -s [STATUS_PATH]      server will analyze status.dat at specified path


The tool will create a web server on the specified port (default is 8979).  Perform a request to `localhost:8979` and collect your services status.
