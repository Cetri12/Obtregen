#Obtregen. 1.00.00 made 10/20/2026
Version = "Version: 1.00.00"
Build_Data = [Version, "Utility File", "Gen1"]
contents = ""

def intro():
    print("===Obtregen===")
    a = input("Encrypt Or Decrypt (E/D): ")

    if a.lower() == "e":
        Encrypt()

    if a.lower() == "d":
        print("Not added yet")

def Encrypt():
    global contents
    print()
    File = input("Name of File: ")
    with open(File, "r") as file:
        contents = file.read()
    
    # Very Basic way of encrypting unconditionally
    contents = contents.replace("print(", "\\A")
    contents = contents.replace("input(", "\\B")
    contents = contents.replace("import", "\\C")
    contents = contents.replace("int(", "\\D")
    contents = contents.replace("global", "\\E")
    contents = contents.replace("with", "\\F")
    contents = contents.replace("open", "\\G")
    contents = contents.replace("abs(", "\\H")
    contents = contents.replace("divmod(", "\\I")
    contents = contents.replace("max(", "\\J")
    contents = contents.replace("min(", "\\K")
    contents = contents.replace("pow(", "\\L")
    contents = contents.replace("round(", "\\M")
    contents = contents.replace("sum(", "\\N")
    contents = contents.replace("bool(", "\\O")
    contents = contents.replace("float(", "\\P")
    contents = contents.replace("list(", "\\Q")
    contents = contents.replace("str(", "\\R")
    contents = contents.replace("all(", "\\S")
    contents = contents.replace("any(", "\\T")
    contents = contents.replace("enumerate(", "\\U")
    contents = contents.replace("type(", "\\V")
    contents = contents.replace("eval(", "\\W")
    contents = contents.replace(".replace", "\\X")
    contents = contents.replace(".lower(", "\\Y")
    contents = contents.replace(".write(", "\\Z")
    contents = contents.replace(".read(", "\\aA")
    contents = contents.replace(".readlines(", "\\aB")
    contents = contents.replace('("")', "\\aC")


    #Writes into a file
    NewFile = File.replace(".py", ".obtregen")
    with open(NewFile, "w") as encodedfile:
        encodedfile.write(contents)

    print()
    print("Finished")

intro()