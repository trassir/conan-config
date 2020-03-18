#from conanfile_base import ArmToolchain
import conanfile_base

class ToolchainHisi3520dv300Conanfile(conanfile_base.ArmToolchain):
    name = "toolchain-hi3520dv300"
    version = "0.1"
    _platform_name = "arm-hisiv300-linux"
    _archive_name = name + ".tar.gz"
    exports_sources = [ _archive_name ] 
