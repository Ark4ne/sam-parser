class Read:

    def __init__(self, qname, flag, rname, pos, mapq, cigar, rnext, pnext, tlen, seq, qual, additional):
        self.__qname = qname
        self.__flag = flag
        self.__rname = rname
        self.__pos = pos
        self.__mapq = mapq
        self.__cigar = cigar
        self.__rnext = rnext
        self.__pnext = pnext
        self.__tlen = tlen
        self.__seq = seq
        self.__qual = qual
        self.__additional = additional

        self.__pair = None

    @property
    def qname(self):
        return self.__qname

    @property
    def flag(self):
        return self.__flag

    @property
    def rname(self):
        return self.__rname

    @property
    def pos(self):
        return self.__pos

    @property
    def mapq(self):
        return self.__mapq

    @property
    def cigar(self):
        return self.__cigar

    @property
    def rnext(self):
        return self.__rnext

    @property
    def pnext(self):
        return self.__pnext

    @property
    def tlen(self):
        return self.__tlen

    @property
    def seq(self):
        return self.__seq

    @property
    def qual(self):
        return self.__qual

    @property
    def additional(self):
        return self.__additional

    @property
    def pair(self):
        return self.__pair

    def link(self, read):
        self.__pair = read
        read.__pair = self

    def has_pair(self):
        return self.__pair is not None
