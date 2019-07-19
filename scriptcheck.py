from mpi4py import MPI

def main():
        #  Initializations and preliminaries                        
        print ("hello world")
        comm = MPI.COMM_WORLD   # get MPI communicator object       
        size = comm.size        # total number of processes         
        rank = comm.rank        # rank of this process              
        status = MPI.Status()   # get MPI status object             

        name = MPI.Get_processor_name()
        print("Hello World %d on %s." % (rank, name))

if __name__ =="__main__":
    main()
