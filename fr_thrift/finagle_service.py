import argparse
import sys
import IPython
import time

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from . import service
from . import compile


def prepare_thrift(thrift_filename):
    thrift_dir = compile.compile_thrift(thrift_filename)
    sys.path.insert(0, thrift_dir)


def connect(zk, service_mode, service_name):
    (service_host, service_port) = service.discover(zk, service_mode, service_name)

    transport = TSocket.TSocket(service_host, service_port)
    transport = TTransport.TFramedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    return (protocol, transport)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a Python shell which is connected to a Thrift service")
    parser.add_argument("--zk", default="zookeeper1.prod.footballradar.net:2181,zookeeper2.prod.footballradar.net:2181,zookeeper3.prod.footballradar.net:2181")
    parser.add_argument("--service-mode", required=True)
    parser.add_argument("--service-name", required=True, help="name of the service to connect to")
    parser.add_argument("--thrift-file", required=True, help="name of the thrift file to compile")
    args = parser.parse_args()

    (protocol, transport) = connect(zk=args.zk, service_mode=args.service_mode, service_name=args.service_name)
    prepare_thrift(args.thrift_file)

    transport.open()

    IPython.embed()
