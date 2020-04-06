import conanfile_base

class Toolchain_Hisi3521dv100(conanfile_base.ArmToolchain):
    name = "toolchain-hi3521dv100"
    version = "0.1"
    _platform_triplet = "arm-hisiv500-linux"
