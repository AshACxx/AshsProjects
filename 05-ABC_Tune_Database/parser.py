from database import inserting

books_dir = "abc_books"



def process_file(file):

    tunes = [] #1
    current_tune = {}

    with open(file, 'r') as f:
        lines = f.readlines()
    # list comprehension to strip the \n's
    lines = [line.strip() for line in lines]

    # just print the files for now
    for line in lines:


        #if the line starts with X, we are on a tune
        if line.startswith("X:"):
            #saving previous tune 
            if current_tune:
                tunes.append(current_tune)

            #new tune present 
            #body is used to append remainder of lines into body later 
            current_tune = {"X": line[2:].strip(),"body":""}
            print(line)  

        elif line.startswith("T:"):
            current_tune["title"] = line[2:].strip()

        elif line.startswith("K:"):
            current_tune["key"] = line[2:].strip()

        elif line.startswith("R:"):
            current_tune["type"] = line[2:].strip()

        #current_tune["body"] taking "body from the dictionary and adding the lines that dont have x t k or r
        else:


            if "body" not in current_tune:
                #making body a key
                current_tune["body"] = ""
                #adding on body to a new line
            current_tune["body"] += line + "\n"


    if current_tune:
        tunes.append(current_tune)

    return tunes #returns to #1


def process(file, book_number):
    tunes = process_file(file)
    inserting(book_number, tunes)
