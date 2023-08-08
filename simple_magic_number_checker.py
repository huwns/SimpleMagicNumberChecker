import argparse


MAGIC_NUMBER_DICT = {
    b"BM": ".bmp",
    b"SIMPLE": ".fits",
    b"GIF8": ".gif",
    b"GKSM": ".gks",
    b"\x01\xda": ".rgb",
    b"\xf1\x00@\xbb": ".itc",
    b"\xff\xd8\xff\xe0": ".jpg",
    b"IIN1": ".nif",
    b"VIEW": ".pm",
    b"\x89PNG": ".png",
    b"%!": ".[e]ps",
    b"Y\xa6j\x95": ".ras",
    b"MM\x00*": ".tif",
    b"II*\x00": ".tif",
    b"gimp xcf v": ".xcf",
    b"#FIG": ".fig",
    b"/* XPM */": ".xpm",
    b'BZ': '.bz',
    b'\x1f\x9d': '.Z',
    b'\x1f\x8b': '.gz',
    b'PK\x03\x04': '.zip',
    b'ustar': '.tar',
    b'MZ': '.exe',
    b'\x7fELF': 'ELF',
}


def check_magic_number(binary_header):
    for key in MAGIC_NUMBER_DICT.keys():
        if key in binary_header:
            print(MAGIC_NUMBER_DICT[key])
            break
    else:
        print("Unknown")


def main():
    parser = argparse.ArgumentParser(description="Simple Magic Code Checker")
    parser.add_argument("file", type=argparse.FileType("rb"))
    args = parser.parse_args()
    check_magic_number(args.file.read(10))


if __name__ == "__main__":
    main()
