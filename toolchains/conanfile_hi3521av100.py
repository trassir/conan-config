import conanfile_base

class Toolchain_Hisi3521av100(conanfile_base.ArmToolchain):
    name = "toolchain-hi3521av100"
    version = "0.1"
    _platform_triplet = "arm-hisiv300-linux"
