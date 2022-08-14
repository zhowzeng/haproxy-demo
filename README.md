# gRPC + HAProxy

## Container

- Get ip addr of container
  ```
  docker exec dockerhive_namenode cat /etc/hosts
  ```

## gRPC

- Build pd2
  ```
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. train.proto
  ```

## Network

- Find ip addr
  ```
  hostname -I
  ```
- Reach host ip inside container
  add `--add-host=host.docker.internal:host-gateway` option to command `docker run`, then `host.docker.internal` can be resolved in container
