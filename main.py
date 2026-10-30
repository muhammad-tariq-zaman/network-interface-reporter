"""Summarise network interfaces from /proc/net/dev-style text.

Usage: python3 main.py [/proc/net/dev]
Reports RX/TX megabytes and error counts per interface, busiest first.
"""
import argparse
import sys


def parse(text):
    interfaces = []
    for line in text.splitlines():
        if ":" not in line:
            continue
        name, rest = line.split(":", 1)
        name = name.strip()
        if not name or name.startswith("Inter") or name.startswith("face"):
            continue
        fields = rest.split()
        if len(fields) < 16:
            continue
        try:
            rx, rx_err = int(fields[0]), int(fields[2])
            tx, tx_err = int(fields[8]), int(fields[10])
        except ValueError:
            continue
        interfaces.append({"name": name, "rx_mb": rx / 1e6, "tx_mb": tx / 1e6,
                           "rx_errors": rx_err, "tx_errors": tx_err})
    interfaces.sort(key=lambda i: i["rx_mb"] + i["tx_mb"], reverse=True)
    return interfaces


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="/proc/net/dev")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        interfaces = parse(f.read())
    for i in interfaces:
        print(f"{i['name']}: RX {i['rx_mb']:.1f} MB TX {i['tx_mb']:.1f} MB errors RX={i['rx_errors']} TX={i['tx_errors']}")
    print(f"{len(interfaces)} interface(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
