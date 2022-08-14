# gRPC + HAProxy

## container
### get ip addr of container
```
docker exec dockerhive_namenode cat /etc/hosts
```

## grpc
### build pd2
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. train.proto
```

## network
### find ip addr
```
hostname -I
```
### reach host ip inside container
add `--add-host=host.docker.internal:host-gateway` option to command `docker run`, then `host.docker.internal` can be resolved in container
