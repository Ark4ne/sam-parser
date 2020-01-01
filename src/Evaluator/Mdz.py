from src.Evaluator.Evaluator import Evaluator
from src.Model.Read import Read
from src.Model.Status import Status


class Mdz(Evaluator):

    def require_additionnal(self):
        return True

    def get_mapping_status(self, read: Read):
        if read.pos == 0 or read.rname == "*" or read.rnext == "*":
            return Status.UNMAPPED

        cigar = read.cigar

        if cigar == '100M':
            add = read.additional

            if "MD:Z" in add:
                if add["MD:Z"] == "100":
                    return Status.MAPPED
                else:
                    return Status.PARTIAL
            else:
                return Status.PARTIAL  # TODO check
        elif cigar == '*':
            return Status.UNMAPPED
        else:
            return Status.PARTIAL
