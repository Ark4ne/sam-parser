from src.Evaluator.Evaluator import Evaluator
from src.Model.Read import Read
from src.Model.Status import Status


class Flag(Evaluator):
    READ_PAIRED = 1                                     # 0b000000000001
    READ_MAPPED_IN_PROPER_PAIR = 2                      # 0b000000000010
    READ_UNMAPPED = 4                                   # 0b000000000100
    MATE_UNMAPPED = 8                                   # 0b000000001000
    READ_REVERSE_STRAND = 16                            # 0b000000010000
    MATE_REVERSE_STRAND = 32                            # 0b000000100000
    FIRST_IN_PAIR = 64                                  # 0b000001000000
    SECOND_IN_PAIR = 128                                # 0b000010000000
    NOT_PRIMARY_ALIGNMENT = 256                         # 0b000100000000
    READ_FAILS_PLATFORM_VENDOR_QUALITY_CHECKS = 512     # 0b001000000000
    READ_IS_PCR_OR_OPTICAL_DUPLICATE = 1024             # 0b010000000000
    SUPPLEMENTARY_ALIGNMENT = 2048                      # 0b100000000000

    def __init__(self):
        self.__flags = {}

    def require_additionnal(self):
        return False

    def get_mapping_status(self, read: Read):
        flag = read.flag

        if flag not in self.__flags:
            if flag & Flag.READ_UNMAPPED:
                self.__flags[flag] = Status.UNMAPPED
            else:
                self.__flags[flag] = Status.MAPPED

        return self.__flags[flag]
