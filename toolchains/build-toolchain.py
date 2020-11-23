#!/usr/bin/python3
import argparse
import os
import shutil
import subprocess
from contextlib import contextmanager

def platform_path(value):
    value = value.rstrip('/')
    if not os.path.isdir(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not an existing directory")
    platform = os.path.basename(value)
    return value, platform


@contextmanager
def chdir(dirname):
    cwd = os.getcwd()
    os.chdir(dirname)
    try:
        yield cwd
    finally:
        os.chdir(cwd)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--platform_path', required=True, type=platform_path)
    parser.add_argument('--username', required=True)
    parser.add_argument('--channel', required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    tree, platform = args.platform_path
    toolchain = f"toolchain-{platform}"
    tar_gz = f"{toolchain}.tar.gz"
    print(f"Using: {tree}, {platform}")
    with chdir(tree) as cwd:
        conanfile = os.path.join(cwd, f"conanfile_{platform}.py")
        reference = f"{args.username}/{args.channel}"
        print(f"Running conan export-pkg -f {conanfile} {reference}")
        subprocess.check_call(["conan", "export-pkg", "-f", conanfile, reference])


if __name__ == '__main__':
    main()
