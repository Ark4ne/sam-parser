class Status:
    UNMAPPED = 1
    MAPPED = 2
    PARTIAL = 4

    def __init__(self):
        self.__reads = {
            self.UNMAPPED: 0,
            self.MAPPED: 0,
            self.PARTIAL: 0
        }

        self.__pairs = {
            self.MAPPED: {
                self.UNMAPPED: 0,
                self.MAPPED: 0,
                self.PARTIAL: 0
            },
            self.PARTIAL: {
                self.UNMAPPED: 0,
                self.PARTIAL: 0
            },
            self.UNMAPPED: {
                self.UNMAPPED: 0
            }
        }

    def pair(self, a, b):
        self.__reads[a] += 1
        self.__reads[b] += 1

        if a == self.MAPPED:
            self.__pairs[a][b] += 1
        elif b == self.MAPPED:
            self.__pairs[b][a] += 1
        elif a == self.PARTIAL:
            self.__pairs[a][b] += 1
        else:
            self.__pairs[b][a] += 1

    def read(self, a):
        self.__reads[a] += 1

    def print(self):
        print("Il y a " + str(self.__reads[self.MAPPED]) + " reads mappés")
        print("Il y a " + str(self.__reads[self.PARTIAL]) + " reads partiellement mappés")
        print("Il y a " + str(self.__reads[self.UNMAPPED]) + " reads non mappés")
        print("Il y a " + str(self.__pairs[self.MAPPED][self.MAPPED]) + " pairs parfaitement mappés")
        print("Il y a " + str(self.__pairs[self.MAPPED][self.PARTIAL]) + " pairs mappés + partial")
        print("Il y a " + str(self.__pairs[self.MAPPED][self.UNMAPPED]) + " pairs mappés + unmapped")
        print("Il y a " + str(self.__pairs[self.PARTIAL][self.PARTIAL]) + " pairs partial + partial")
        print("Il y a " + str(self.__pairs[self.PARTIAL][self.UNMAPPED]) + " pairs partial + unmapped")
        print("Il y a " + str(self.__pairs[self.UNMAPPED][self.UNMAPPED]) + " pairs unmapped + unmapped")
