# coding: utf-8
# code from psa net, thanks jiwoon-ahn.
# see https://github.com/jiwoon-ahn/psa for details.

class Logger(object):
    def __init__(self, outfile):
        self.terminal = sys.stdout
        self.log = open(outfile, "w")
        sys.stdout = self

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        

log_name = "out"
Logger(log_name + '.log') # all print will also dump to out.log
