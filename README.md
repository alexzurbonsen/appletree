### Jaeger? Sammler! Harvesting apples, Apfelernte, or how they say in Hessen: Ebbelärnde

To gather some apples with support from Jaeger first run (from the project root)

```
pip install -r requirements.txt
```

then run

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. appletree.proto```
```
(and don't be irritated by the Bazel stuff. It's not of much use...) 

Afterwards start the Jaeger all-in-one Docker Container with

```
docker run -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one
```

(see [https://opentelemetry.io/docs/instrumentation/python/getting-started/](https://opentelemetry.io/docs/instrumentation/python/getting-started/) for more details).

The GUI should be reachable under [http://localhost:16686/](http://localhost:16686/) now.

In two separate terminals: 1) start the server

```
python appletree_server.py
```

and 2) start the client.

```
python appletree_client.py
```

In Hessen they like to make Äppler out of the Äppel. But that is not supported yet...