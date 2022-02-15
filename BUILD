#load("@rules_proto//proto:defs.bzl", "proto_library")
#load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")
load("@rules_python//python:defs.bzl", "py_binary") #, "py_library")
load("@rules_proto_grpc//python:defs.bzl", "python_grpc_compile")

proto_library(
    name = 'appletree',
    srcs = ['appletree.proto'],
)

#py_proto_library(
#    name = 'py_appletree',
#    srcs = ['appletree.proto'],
#)

python_grpc_compile(
    name = 'appletree_py_grpc',
    protos = [':appletree'],
    #output_mode = 'NO_PREFIX',
)

#genrule(
#    name = "copy",
#    srcs = ["bazel-bin/appletree_py_grpc/appletree_pb2.py"], # "bazel-bin/appletree_pb2_grpc.py"
#    outs = ["appletree_pb2.py"], # "appletree_pb2_grpc.py"
#    #output_to_bindir = 1,
#    cmd = "cp $< $@",
#)

