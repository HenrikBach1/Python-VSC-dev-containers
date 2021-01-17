from Hello import Hello as ho

def Hello():
    print("Hello World from: " + __name__)

def main():
    ho.Hello()
    Hello()

if __name__ == "__main__":
    main()