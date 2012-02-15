# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
host interface (1.1 extension).
"""
from novaclient import base


class Host(base.Resource):
    def __repr__(self):
        return "<Host: %s>" % self.host

    def _add_details(self, info):
        dico = 'resource' in info and info['resource'] or info
        for (k, v) in dico.iteritems():
            setattr(self, k, v)

    def update(self, values):
        return self.manager.update(self, values)

    def startup(self, host):
        return self.manager.startup_host(self, host)

    def shutdown(self, host):
        return self.manager.shutdown_host(self, host)

    def reboot(self, host):
        return self.manager.reboot_host(self, host)


class HostManager(base.ManagerWithFind):
    resource_class = Host

    def get(self, host):
        """
        Describes cpu/memory/hdd info for host.

        :param host: destination host name.
        """
        return self._list("/os-hosts/%s" % (host), "host")

    def update(self, host, values):
        """Update status or maintenance mode for the host."""
        result = self._update("/os-hosts/%s" % base.getid(host), values)
        return self.resource_class(self, result)

    def host_action(self, host, action):
        """Performs an action on a host."""
        url = "/os-hosts/%s/%s" % (base.getid(host), action)
        return self._get(url)
