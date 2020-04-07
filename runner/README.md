# What?
Docker image with Ubuntu to launch [Github Actions Runner](https://github.com/actions/runner) in.

# Why?
Because Runner and its actions (like [setup-python](https://github.com/actions/setup-python)) require exactly Ubuntu to run in, and ideally should be isolated and independent from surrounding OS.

# How?
1. Build your docker image
```
user@node $ docker build . -t actions-runner
```
2. [Download](https://github.com/actions/runner/releases), unpack and configure your GHA Runner instance according to instructions in your repo Settings under "Actions" tab. See [[1]](https://help.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners) and [[2]](https://help.github.com/en/actions/hosting-your-own-runners/using-self-hosted-runners-in-a-workflow).
3. Create new Github [access token](https://github.com/settings/tokens) with `read:packages, repo` permissions for use with NPM.
4. Setup NPM to use Github Package Registry according to [instructions](https://help.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-npm-for-use-with-github-packages#authenticating-to-github-package-registry). For example, you can create a `.npmrc` file near unpacked `run.sh` with contents like:
```
//npm.pkg.github.com/:_authToken=<your token from github>
registry=https://npm.pkg.github.com/actions
```
5. `cd` to unpacked directory and enter into built image:
```
user@node $ docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock -v `pwd`:/actions-runner actions-runner bash
```
Note the mounting of `docker.sock`. You could genuinely install `docker-ce` inside a Ubuntu image and run `service docker start`, but it may cause mighty lags (up to 30s) on any `docker run` command. It is easier and faster to install just `docker-ce-cli`, forward the socket file, and send commands from inside a running container to the daemon on your host machine.
6. Check that Docker commands are working inside your container. [CPT](https://github.com/conan-io/conan-package-tools) builds require Docker, and we are already inside one:
```
root@docker $ docker ps
```
7. Install Python 3 toolchain for `setup-python` action, since it itself only switches between installations present locally:
```
root@docker $ npm install @actions/toolcache-python-ubuntu-1804-x64@3.8.21582900205
```
This will download, compile and install Python binaries to `/opt/hostedtoolcache`
8. Switch to `runner` user in docker image and start the configured runner:
```
root@docker su runner
runner@docker $ export AGENT_TOOLSDIRECTORY=/opt/hostedtoolcache/
runner@docker $ ./run.sh
```
You now should a working GHA Runner inside a container that will be able to process workflows running with `os: self-hosted`.
