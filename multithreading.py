#multithreading

class Process():
    def __init__(selfself,filename,dr):
        super(Process,self).__init__()
        self.filename=filename
        self.dr=dr

    def run(self):
        print(find_files(self.filename,self.dr))

def main():
    for d in drives:

        p=Process(filename,d)
        p.start()
        p.join()

    #p=Process(filename,drives[1])
    #p.start()
    #p.join()
    #p=Process(filename,drives[2])
    #p.start()
    #p.join()
