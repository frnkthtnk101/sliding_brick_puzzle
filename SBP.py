from read_file import get_file
import argparse

def main(file_path):
    content = get_file(file_path)
    if content is None:
        print("no good")
    else:
        print(content)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("file", help ="file path of file", type = str)
    ARGS = PARSER.parse_args()
    main(ARGS.file)