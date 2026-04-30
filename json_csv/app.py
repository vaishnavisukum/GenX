def main():

    file = open("Salary_preediction2.csv","r")
    file_data = file.read()

    file_items = file_data.split("\n")

    headers = file_items[0]
    headers = headers.split(",")
    
    data = []
    for d in range(1,len(file_items)):
        data.append(file_items[d].split(","))

    json = []
    temp = {}
    
    for d in range(0,len(data)):
        for h in range(0,len(headers)):
            temp[headers[h]] = data[d][h]

        json.append(temp)
        temp = {}

    file = open("xyz.json","a")
    file.write("[")
    for i in json:
        file.write(str(i).replace("'",'"')+",\n")

    file.close()

    file = open("xyz.json","r")
    data = file.read()
    data = data[0:-2]+"]"

    file = open("xyz.json","w")
    file.write(data)
    file.close()

if __name__=="__main__":
    main()