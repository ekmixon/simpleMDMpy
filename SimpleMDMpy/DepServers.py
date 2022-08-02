#!/usr/bin/env python

"""module for interacting with dep server configurations"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class DepServers(SimpleMDMpy.SimpleMDM.Connection):
    """module for interacting with dep server configurations"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/dep_servers")

    def get_dep_servers(self, dep_server_id="all"):
        """returns dep servers, defaults to all if none specified"""
        url = self.url
        if dep_server_id != 'all':
            url = f"{url}/{dep_server_id}"
        return self._get_data(url)

    def sync_dep_servers(self, dep_server_id):
        """syncs specified server with Apple DEP"""
        url = f"{self.url}/{dep_server_id}/sync"
        data = {}
        return self._post_data(url, data)

    def get_dep_devices(self, dep_server_id, dep_device_id="all"):
        """return a DEP device via an ID, defaults to all if none specified"""
        url = f"{self.url}/{dep_server_id}/dep_devices"
        if dep_device_id != 'all':
            f"{url}/{dep_device_id}"
        data = {}
        return self._get_data(url, data)
