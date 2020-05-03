import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="NFA Program Help Guide"
    )

    parser.add_argument('REGEX', help=" REGEX")
    parser.add_argument('STRING', help="STRING")

    args = parser.parse_args()

    print(args)