import conanfile_base

class Toolchain_Hisi3536(conanfile_base.ArmToolchain):
    name = "toolchain-hi3536"
    version = "0.1"
    _platform_triplet = "arm-hisiv300-linux"
