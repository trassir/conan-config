#!/usr/bin/python3
import argparse
import os
import shutil
import subprocess
import tarfile

#from conans.client.conan_api import Conan
#from conans.client.command import Command

def profile_path(value):
    value = value.rstrip('/')
    if not os.path.isdir(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not an existing directory")
    lst = os.listdir(value)
    if not len(lst) == 1:
        raise argparse.ArgumentTypeError("'{value}' directory should contain only prefix-triplet subfolder")
    triplet = lst[0]
    subdir = os.path.join(value, triplet)
    if not os.path.isdir(os.path.join(subdir, 'bin')):
        raise argparse.ArgumentTypeError("No 'bin' subdirectory in '{subdir}'")
    profile = os.path.basename(value)
    return subdir, profile


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile_path', required=True, type=profile_path)
    parser.add_argument('--username', required=True)
    parser.add_argument('--channel', required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    tree, profile = args.profile_path
    toolchain = f"toolchain-{profile}"
    tar_gz = f"{toolchain}.tar.gz"
    print(f"Using: {tree}, {profile}")
    if not os.path.isfile(tar_gz):
        print("Copying tree...")
        shutil.copytree(tree, toolchain)
        print("Compressing tree...")
        with tarfile.open(tar_gz, "w:gz") as tar:
            tar.add(toolchain)
    else:
        print(f"Archive {tar_gz} exists, skipping compression")

    conanfile = f"./conanfile_{profile}.py"
    reference = f"{args.username}/{args.channel}"
    print(f"Running conan create {conanfile} {reference}")
    subprocess.call(["conan", "create", conanfile, reference])
    #Command(Conan()).create(conanfile, reference)


if __name__ == '__main__':
    main()