This directory contains:
- `conanfile`s providing packages for Conan with our ARM toolchains. These are needed to build ARM binaries in our CCI fork no a self-hosted runner. You will need access to sdkARM to be able to create packages.
- `build-toolchain.py` helper script for package creation.
- Dockerfile for image to be used by CPT to build ARM binaries. Should be built from repo root, as `docker build . -f toolchains/Dockerfile`.
