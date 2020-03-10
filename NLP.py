import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def data1(data):
    new = []
    data = open('10_dataset/text_scrap.txt', "r")
    text = data.readlines()[0]
    data.close()
    pattern = r"(?<=\:).+?(?=\')"  
    match = re.findall(pattern, text)
    for i in range(0, len(match), 2):
        new.append([match[i][1:], match[i + 1][1:]])
    return new
    
def data2(data):
    data = open('10_dataset/Company Details.txt', "r")
    new = []
    for line in data:
        line2 = next(data, None)
        new.append([line[6:-1], line2[9:-1]])
    data.close()
    return new
    
def data3(data):
    data = open("10_dataset/name_purpose.txt", "r")
    data =re.sub(r"[^\w\s]", ' ', data) # remove all non-word characters
    new = []
    for line in data:
        line2 = next(data, None)
        new.append([line[6:-1], line2[9:-1]])
    data.close()
    return new
    
def data4(data):
    data = open('10_dataset/output_Webscrap_HW2.txt', "r")
    new = []
    
    for line in data:
        if line != "\n":
            name = re.search(r".*(?=" + re.escape(",Purpose:") + ")", line[6:]).group(0)
            purpose = re.search(r"((?<=" + re.escape(",Purpose: ") + ").*)", line[6:]).group(0)
            new.append([name, purpose])
    data.close()
    return new


def data5(data):
    data = open("10_dataset/foryou4.txt", "r")
    new = []
    count = 0
    for line in data:
        if count < 50:  
            new.append([line[6:-1]])
        else: 
            new[count - 50].append(line[9:-1])
        count += 1
    data.close()
    return new
 
 
import csv
csv_file = r"10_dataset/napu.csv"
txt_file = r"10_dataset/napu.txt"
text_list = []
with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append("\n".join(line))
with open(txt_file, "w") as my_output_file:
    for line in text_list:
        my_output_file.write(" " + line)
    print('File Successfully written.')    
def data6(data):
    data = open('10_dataset/napu.txt', "r")
    new = []
    for line in data:
        company = re.search(r"((?<=" + re.escape(")") + ").*)", line)
        line2 = next(data)
        new.append([company, line2[2:-1]])
    data.close()
    return new  
 
 
csv_file = r"10_dataset/companys.csv"
txt_file = r"10_dataset/companys.txt"
text_list = []
with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append("\n".join(line))
with open(txt_file, "w") as my_output_file:
    for line in text_list:
        my_output_file.write(" " + line)
    print('File Successfully written.')   
def data7(data):
    data = open('10_dataset/companys.txt', "r")
    new = []
    for line in data:
        company = re.search(r"((?<=" + re.escape(")") + ").*)", line)
        line2 = next(data)
        new.append([company, line2[2:-1]])
    data.close()
    return new  
    
def data8(data):
    data = open('10_dataset/595_HW2.txt', "r")
    new = []
    for line in data:
        line2 = next(data)
        next(data)  
        new.append([line[6:-1], line2[9:-1]])
    data.close()
    return new
    

def data9(data):
    data = open('10_dataset/result.txt', "r")
    new = []
    for line in data:
        line2 = next(data, None)
        new.append([line[6:-1], line2[9:-1]])
    data.close()
    return new
    
    
def data10(data):
    data = open('10_dataset/Company.txt', "r")
    new = []
    for line in data:
        company = re.search(r"((?<=" + re.escape(")") + ").*)", line).group(0)
        line2 = next(data)
        new.append([company, line2[2:-1]])
    data.close()
    return new
    
    
if __name__ == '__main__':
    overall=(data1('10_dataset/text_scrap.txt')+
             data2('10_dataset/Company Details.txt')+
             data3("10_dataset/name_purpose.txt")+
             data4('10_dataset/output_Webscrap_HW2.txt')+
             data5("10_dataset/foryou4.txt")+
             data6('10_dataset/napu.txt')+
             data7('10_dataset/companys.txt')+
             data8('10_dataset/595_HW2.txt')+
             data9('10_dataset/result.txt')+
             data10('10_dataset/Company.txt'))
    output=r"10_dataset/overall.txt"
    output = open("10_dataset/overall.txt","w")
    
    
    text=""
    for company in overall:
        text = text + "Name: " + company[0] + "\nPurpose: " + company[1] + "\n"
    output.write(text)
    output.close()
    overall=r"10_dataset/overall_1.txt"
    
    # use sentiment to sort overall 1000 companies
    for company in overall:
        sent = SentimentIntensityAnalyzer()
        company.append(sent.polarity_scores(company[1])["compound"])
    overall_sent= sorted(master, key=lambda x: x[2])
    neg= overall_sent[0:10]
    pos= overall_sent[-10:]

    # creat 10 most negative sentiment company .txt file
    neg_sent = r("negative_sent.txt")
    text = ""
    neg_sent.write("10 Most Negative Companies" + "\n\n")
    for c in neg:
        text = (text + "Name: " + c[0] + "\nPurpose: " + c[1])
    neg_sent.write(text)
    neg_sent.close()

    # creat 10 most positive sentiment company .txt file
    pos_sent = r("positive_sent.txt")
    pos_sent.write("10 Most Positive Companies" + "\n\n")
    text = ""
    for c in reversed(pos):
        text = (text + "Name: " + c[0] + "\nPurpose: " + c[1])
    pos_sent.write(text)
    pos_sent.close()


