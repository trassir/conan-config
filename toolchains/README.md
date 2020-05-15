This directory contains:
- `conanfile`s providing packages for Conan with our ARM toolchains. These are needed to build ARM binaries in our CCI fork no a self-hosted runner. You will need access to sdkARM to be able to create packages.
- `build-toolchain.py` helper script for package creation.
- `Dockerfile.arm` creating an image to be used by CPT to build ARM binaries. Should be built from repo root, as `docker build . -f toolchains/Dockerfile.arm`.
- `Dockerfile.gcc8` creating an image to be used in GHA instead of `conanio/gcc8`, since we need older `glibc`.
