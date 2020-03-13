import argparse
import socket

PARSER = argparse.ArgumentParser(description="Find the services bound to a range of ports.")
PARSER.add_argument("--start", type=int, default=0, help="The start of the range to search")
PARSER.add_argument("--end", type=int, default=1500, help="The end of the range to search")


def read_ports(start, end):
    print(f"Getting services in range {start}-{end} on {socket.gethostname()}")
    if start < 0 or start > 65535:
        raise ValueError("Start of range cannot be less than 0 and great than 65535")

    if end < 0 or end > 65535:
        raise ValueError("End of range cannot be less than 0 and great than 65535")

    if end < start:
        raise ValueError("End of range cannot be less than the start of the range")

    for i in range(start, end + 1):
        try:
            service = socket.getservbyport(i)
            print(f"Service on port {i}: {service}")
        except OSError:
            pass


if __name__ == "__main__":
    args = PARSER.parse_args()
    read_ports(args.start, args.end)
