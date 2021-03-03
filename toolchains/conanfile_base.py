from conans import ConanFile
from conans import tools
import os

class ArmToolchain(ConanFile):
    exports = "conanfile_base.py"
    settings = "os_build", "arch_build"
    _abi = "uclibcgnueabi"

    def package(self):
        self.copy("*", dst="", src=self._platform_triplet, symlinks=True)

    def package_info(self):
        bin_folder = os.path.join(self.package_folder, "bin")
        self.env_info.path.append(bin_folder)
        gcc = os.path.join(bin_folder, self._toolchain_prefix() + "gcc")
        assert os.path.isfile(gcc)
        self.env_info.CC = gcc
        gpp = os.path.join(bin_folder, self._toolchain_prefix() + "g++")
        assert os.path.isfile(gpp)
        self.env_info.CXX = gpp
        strip = os.path.join(bin_folder, self._toolchain_prefix() + "strip")
        assert os.path.isfile(strip)
        self.env_info.STRIP = strip
        self.env_info.SYSROOT = self.package_folder

    def _toolchain_prefix(self):
        return "{}-{}-".format(self._platform_triplet, self._abi)
