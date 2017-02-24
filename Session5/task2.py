# data is loaded from a local variable with a given name
# data is loaded from a global variable with a given name
# data is loaded from a file with a given name located at a specific folder
# (the class should support addition of any number of search folders to the chain)
import os.path


class ChainLink:
    def __init__(self, chain, strategy):
        self.strategy = strategy
        self.chain = chain
        self.chain.append(self)

    def next(self):
        location = self.chain.index(self)  # where this link is in the chain
        if not self.end():
            return self.chain[location + 1]

    def end(self):
        return self.chain.index(self) + 1 >= len(self.chain)

    def __call__(self, *request):
        r = self.strategy(*request)
        if r:
            return r
        elif self.end():
            print("Could not find name")
        else:
            return self.next()(*request)


class TryLocal:
    def __call__(self, var_name, *args):
        if var_name in locals():
            return locals()[var_name]


class TryGlobal:
    def __call__(self, var_name, *args):
        if var_name in globals():
            return globals()[var_name]


class TryFile:
    def __call__(self, file_name, folder_name=None):
        path = "{}/{}".format(file_name, folder_name) if folder_name else file_name
        if os.path.isfile(path):
            with open(path, 'r') as file:
                return file.readlines()

chain = []
ChainLink(chain, TryLocal())
ChainLink(chain, TryGlobal())
ChainLink(chain, TryFile())
ChainLink(chain, TryFile())

x = 10
print(chain[0]('x', "./DataFolder"))
