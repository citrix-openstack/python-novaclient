from novaclient.v1_1 import host_aggregates
from tests import utils
from tests.v1_1 import fakes


cs = fakes.FakeClient()


class HostAggregatesTest(utils.TestCase):

    def test_list_host_aggregates(self):
        kps = cs.host_aggregates.list()
        cs.assert_called('GET', '/os-host-aggregates')
        [self.assertTrue(isinstance(kp, host_aggregates.HostAggregate))
            for kp in kps]

    def test_delete_host_aggregate(self):
        kp = cs.host_aggregates.list()[0]
        kp.delete()
        cs.assert_called('DELETE', '/os-host-aggregates/test')
        cs.host_aggregates.delete('test')
        cs.assert_called('DELETE', '/os-host-aggregates/test')
        cs.host_aggregates.delete(kp)
        cs.assert_called('DELETE', '/os-host-aggregates/test')

    def test_create_host_aggregate(self):
        kp = cs.host_aggregates.create("foo")
        cs.assert_called('POST', '/os-host-aggregates')
        self.assertTrue(isinstance(kp, host_aggregates.HostAggregate))

    def test_import_host_aggregate(self):
        kp = cs.host_aggregates.create("foo")
        cs.assert_called('POST', '/os-host-aggregates')
        self.assertTrue(isinstance(kp, host_aggregates.HostAggregate))
