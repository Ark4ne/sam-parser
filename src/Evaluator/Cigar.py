from src.Evaluator.Evaluator import Evaluator
from src.Model.Read import Read
from src.Model.Status import Status


class Cigar(Evaluator):

    def require_additionnal(self):
        return False

    def get_mapping_status(self, read: Read):
        if read.pos == 0 or read.rname == "*" or read.rnext == "*":
            return Status.UNMAPPED

        cigar = read.cigar

        if cigar == '100M':
            return Status.MAPPED
        elif cigar == '*':
            return Status.UNMAPPED
        else:
            return Status.PARTIAL
