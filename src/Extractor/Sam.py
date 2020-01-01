import csv

from src.Model.Header import Header
from src.Model.Read import Read


class Sam:
    def __init__(self, file: str):
        self.__file = open(file)
        self.__reader = csv.reader(self.__file, delimiter='\t')
        self.__headers = self.__extract_headers()

    def __extract_headers(self):
        self.__file.seek(0)
        header = Header()
        for row in self.__reader:
            if str(row[0]).startswith('@'):
                header.push(row[0], row[1:])
            else:
                return header

    def __seek_to_contents(self):
        headers_line = self.__headers.len()
        self.__file.seek(0)
        while headers_line:
            self.__file.readline()
            headers_line -= 1

    def headers(self):
        return self.__headers

    def extract(self, with_additional=False):
        self.__seek_to_contents()

        sn = self.__headers.get_sn()
        has_sn = sn is not None

        tmp_reads = {}
        for row in self.__reader:
            qname = row[0]
            pos = int(row[3])
            pnext = int(row[7])
            rname = row[2]
            rnext = row[6]

            additionnal = {}

            if with_additional:
                for value in row[11:]:
                    parts = str(value).rsplit(':', maxsplit=1)
                    additionnal[parts[0]] = parts[1]

            read = Read(
                qname,  # qname
                int(row[1]),  # flag
                rname,
                pos,
                row[4],  # mapq
                row[5],  # ciagr
                rnext,  # rnext
                pnext,  #
                row[8],  # tlen
                row[9],  # seq
                row[10],  # qual
                additionnal
            )

            if pos != 0 \
                    and rnext != "*" \
                    and (has_sn and rname == sn or rname != "*"):
                if pnext in tmp_reads:
                    read.link(tmp_reads[pnext])

                    yield read

                    del tmp_reads[pnext]
                else:
                    tmp_reads[pos] = read
            else:
                yield read

        for read in tmp_reads:
            yield read
