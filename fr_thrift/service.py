from kazoo.client import KazooClient
from os.path import join
import json


class NotRunningException(Exception): pass
class AmbiguousException(Exception): pass


def discover(hosts, service_mode, service_name):
    zk = KazooClient(hosts=hosts)
    zk.start()

    path = "/fr/{}/service/{}".format(service_mode, service_name)

    children = zk.get_children(path)
    if len(children) > 1:
        raise AmbiguousException("Make sure you only have one instance of the service running!")
    elif len(children) == 0:
        raise NotRunningException()

    (data, _) = zk.get(join(path, children[0]))

    data = json.loads(data)

    return (data["serviceEndpoint"]["host"], int(data["serviceEndpoint"]["port"]))
