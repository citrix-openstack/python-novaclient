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
HostAggregate interface (1.1 extension).
"""

from novaclient import base


class HostAggregate(base.Resource):
    """
    A os-host-aggregates is a collection of compute services.
    """

    def __repr__(self):
        return "<HostAggregate: %s>" % self.uuid

    def _add_details(self, info):
        dico = 'os-host-aggregate' in info and \
            info['os-host-aggregate'] or info
        for (k, v) in dico.items():
            setattr(self, k, v)

    @property
    def uuid(self):
        return self.name

    def delete(self):
        self.manager.delete(self)


class HostAggregateManager(base.ManagerWithFind):
    resource_class = HostAggregate

    def create(self, name, availability_zone):
        """
        Create a HostAggregate

        :param name: name for the os-host-aggregates to create
        """
        body = {'host-aggregate': {'name': name,
                                   'availability_zone': availability_zone}}
        #if public_key:
        #    body['keypair']['public_key'] = public_key
        return self._create('/os-host-aggregates', body, 'host-aggregate')

    def delete(self, key):
        """
        Delete a os-host-aggregates

        :param key: The :class:`os-host-aggregates` (or its ID) to delete.
        """
        self._delete('/os-host-aggregates/%s' % (base.getid(key)))

    def list(self):
        """
        Get a list of os-host-aggregates.
        """
        return self._list('/os-host-aggregates', 'host-aggregates')
