load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")


proto_library(
    name = 'appletree',
    srcs = ['appletree.proto'],
)

py_proto_library(
    name = 'py_appletree',
    srcs = [':appletree'],
)