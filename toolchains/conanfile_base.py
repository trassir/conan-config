from conans import ConanFile
from conans import tools
import os

class ArmToolchain(ConanFile):
    exports = "conanfile_base.py"
    settings = "os_build", "arch_build"

    def build(self):
        _archive_name = name + ".tar.gz"
        tools.unzip(os.path.join(self.source_folder, _archive_name))

    def package(self):
        self.copy("*", dst="", src=self.name)

    def package_info(self):
        bin_folder = os.path.join(self.package_folder, "bin")
        self.env_info.path.append(bin_folder)
        self.env_info.CC = os.path.join(bin_folder, self._toolchain_prefix() + "gcc")
        self.env_info.CXX = os.path.join(bin_folder, self._toolchain_prefix() + "g++")
        self.env_info.SYSROOT = self.package_folder

    def _toolchain_prefix(self):
        return self._platform_triplet + "-uclibcgnueabi-"
