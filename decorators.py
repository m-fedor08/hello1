def announce(f):
    def wrapper():
        print("About the run function ...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, wordl!")

hello()
