### Jaeger? Sammler! Harvesting apples, Apfelernte, or how they say in Hessen: Äppelärnde

To gather some apples with support from Jaeger first run (from the project root)

```
pip install -r requirements.txt
```

then run

```
./gen_proto_grpc.sh
```

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

2) start the client.

```
python appletree_server.py
```

In Hessen they like to make Äppler out of the Äppel. But that is not supported yet...