# HAProxy

## Build the container
```
$ docker build -t my-haproxy .
```

## Test the configuration file
```
$ docker run -it --rm my-haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
```

## Run the container
```
$ docker run -d --add-host=host.docker.internal:host-gateway -p 5555:4444 -p 5566:4455 my-haproxy
```

## references
- https://hub.docker.com/_/haproxy
- https://www.haproxy.com/documentation/hapee/latest/load-balancing/protocols/http-2/
- https://github.com/hnasr/javascript_playground/blob/master/proxy/test.cfg
