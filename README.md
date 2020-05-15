# conan-config

This repository contains:
- [Conan](https://conan.io/) profiles for building [Trassir](http://trassir.com/) and dependencies;
- Dockerfiles for images to be used with [CPT](https://github.com/conan-io/conan-package-tools) for build automation
- Dockerfile for [self-hosted GHA Runner](https://help.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)

See [Conan-Center Index fork](https://github.com/trassir/conan-center-index) for recipies and build workflows.

### How to use

To install configuration:
```
conan config install --args https://github.com/trassir/conan-config.git
```

To build and use Docker images, see corresponding READMEs in subdirectories.
