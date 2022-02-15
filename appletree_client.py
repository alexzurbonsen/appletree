import logging

import appletree_pb2
import appletree_pb2_grpc
import grpc
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.grpc import GrpcInstrumentorClient
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "appletree"})
    )
)

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

instrumentor = GrpcInstrumentorClient().instrument()

tracer = trace.get_tracer(__name__)


def input_time():
    time_min = input('How long do you want to shake the apple tree? Please enter time in minutes: ')
    try:
        time_min = int(time_min)
        return appletree_pb2.Time(time_min=time_min)
    except ValueError:
        print("Please enter a number.")


def run(time):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = appletree_pb2_grpc.AppleTreeStub(channel)
        num_apples = stub.ShakeAppleTree(time)
        print(f'{num_apples.num_apples} apples fell from the tree. Please collect!')


if __name__ == '__main__':
    logging.basicConfig()
    time = input_time()
    run(time)
