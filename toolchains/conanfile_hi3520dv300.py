import conanfile_base

class Toolchain_Hisi3520dv300(conanfile_base.ArmToolchain):
    name = "toolchain-hi3520dv300"
    version = "0.1"
    _platform_triplet = "arm-hisiv300-linux"
