"""Synthetic CLI fixture: no dependencies, network, files or private inputs."""
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description="Synthetic greeting fixture")
    parser.add_argument("name")
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
