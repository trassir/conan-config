import conanfile_base

class Toolchain_Hisi3536dv100(conanfile_base.ArmToolchain):
    name = "toolchain-hi3536dv100"
    version = "0.1"
    _platform_triplet = "arm-hisiv510-linux"
