from conans import ConanFile
from conans import tools
import os

class ArmToolchain(ConanFile):
    exports = "conanfile_base.py"
    settings = "os_build", "arch_build"

    def build(self):
        tools.unzip(os.path.join(self.source_folder, self._archive_name))

    def package(self):
        self.copy("*", dst="", src=self.name)

    def package_info(self):
        bin_folder = os.path.join(self.package_folder, "bin")
        self.env_info.path.append(bin_folder)
        self.env_info.CC = os.path.join(bin_folder, self._triplex_prefix() + "gcc")
        self.env_info.CXX = os.path.join(bin_folder, self._triplex_prefix() + "g++")
        self.env_info.SYSROOT = self.package_folder

    def _triplex_prefix(self):
        return self._platform_name + "-uclibcgnueabi-"

