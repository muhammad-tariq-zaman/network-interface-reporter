# network-interface-reporter

Summarise per-interface traffic and errors from /proc/net/dev, busiest interface first.

## How to run

```sh
python3 main.py /proc/net/dev
```

## Example output

```
eth0: RX 5.0 MB TX 2.0 MB errors RX=2 TX=1
lo: RX 1.0 MB TX 1.0 MB errors RX=0 TX=0
2 interface(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
