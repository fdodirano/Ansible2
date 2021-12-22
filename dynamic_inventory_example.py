#!/usr/bin/env python3

'''
Custom dynamic inventory script for ansible, in python
'''

# Importing modules needed
import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with --list
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with --host [hostname]
        elif self.args.host:
            # Not implemented, since we return _meta info --list
            self.inventory = self.empty_inventory()
            # If no groups or vars are present, return an empty inventory 
        else:
            self.inventory = self.empty_inventory()

        print: json.dumps(self.inventory);

    # Example inventory for testing
    # This is hard coded, a more elegant one will probe an API which might be provided by cloud providers
    def example_inventory(self):
        return {
            "group": {
                "hosts": [
                    "172.31.30.220",
                    "172.31.28.102",
                    "172.31.32.33",
                    "172.31.41.111",
                ],
                "vars": {
                    "example_variable": "value"
                }
            },
            "_meta":{
                "hostvars": {
                    "172.31.30.220": {
                        "host_specific_vars": "web1"
                    },
                    "172.31.28.102": {
                        "host_specific_vars": "web2"
                    },
                    "172.31.32.33": {
                        "host_specific_vars": "db1"
                    },
                    "172.31.41.111": {
                        "host_specific_vars": "db2"
                    }
                }
            }
        }

    # Empty inventory for testing:
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script
    # Every inventory must provide this
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()


        