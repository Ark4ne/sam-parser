from src.Evaluator.Evaluator import Evaluator
from src.Extractor.Sam import Sam
from src.Model.Status import Status


class Parser:

    def __init__(self, file: str):
        self.__extractor = Sam(file)

    def headers(self):
        return self.__extractor.headers()

    def analyse(self, evaluator: Evaluator):
        status = Status()

        for read in self.__extractor.extract(with_additional=evaluator.require_additionnal()):
            if read.has_pair():
                status.pair(
                    evaluator.get_mapping_status(read),
                    evaluator.get_mapping_status(read.pair)
                )
            else:
                status.read(evaluator.get_mapping_status(read))

        return status
