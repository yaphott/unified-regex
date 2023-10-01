import sys
import re2


def iterate_codepoints(pattern, file_path):
    with open(file_path, mode="w", encoding="utf-8") as file:
        regex = re2.compile(pattern)
        for i in range(0, 0x10ffff + 1):
            # if 0xd800 <= i <= 0xdfff:
            #     continue
            try:
                char = chr(i).encode("utf-8")
            except UnicodeEncodeError:
                continue
            if regex.match(char):
                file.write(f"{i:04X}\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <pattern> <file_path>")
    else:
        pattern = sys.argv[1]
        file_path = sys.argv[2]
        iterate_codepoints(pattern, file_path)
