import conanfile_base

class Toolchain_Hisi3531d(conanfile_base.ArmToolchain):
    name = "toolchain-hi3531d"
    version = "0.1"
    _platform_triplet = "arm-hisiv500-linux"
