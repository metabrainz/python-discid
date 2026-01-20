#!/usr/bin/env python
# Copyright (C) 2013  Johannes Dewender
# This example is free. You can redistribute and/or modify it at will.

# this will load Libdiscid
import discid


def simple_example():
    disc = discid.read()  # use default device
    print(f"id: {disc.id}")
    print(f"used {discid.get_default_device()} as device")
    print(f"submit with:\n{disc.submission_url}")


def _length_str(seconds, sectors):
    hours = seconds // 3600
    seconds = seconds % 3600
    if hours:
        return f"{hours}:{seconds // 60:>02}:{seconds % 60:>02} ({sectors:>6})"
    else:
        return f"  {seconds // 60:>2}:{seconds % 60:>02} ({sectors:>6})"


def complex_example():
    device_name = discid.get_default_device()
    disc = discid.read(device_name, ["mcn", "isrc"])
    print(f"device:\t{device_name}")
    print(f"id:\t{disc.id}")
    print(f"MCN:\t{disc.mcn}")
    print(f"length:\t{_length_str(disc.seconds, disc.sectors)}")
    for track in disc.tracks:
        length = _length_str(track.seconds, track.sectors)
        print(f"{track.number:>2}: {track.offset:>6} {length}\tISRC: {track.isrc}")


if __name__ == "__main__":
    # simple_example()
    complex_example()

# vim:set shiftwidth=4 smarttab expandtab:
