import logging
from concurrent import futures
from random import randrange

import appletree_pb2
import appletree_pb2_grpc
import grpc
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.grpc import GrpcInstrumentorServer
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

grpc_server_instrumentor = GrpcInstrumentorServer()
grpc_server_instrumentor.instrument()

tracer = trace.get_tracer(__name__)


class AppleTreeServicer(appletree_pb2_grpc.AppleTreeServicer):

    def ShakeAppleTree(self, request, context):
        return appletree_pb2.NumberOfApples(num_apples=min(randrange(0, 30*request.time_min), 500))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    appletree_pb2_grpc.add_AppleTreeServicer_to_server(
        AppleTreeServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
