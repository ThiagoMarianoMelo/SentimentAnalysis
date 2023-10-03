import csv
from AnalyzeSentimenteService import analyze_sentiment
from Classes.DataClass import DataClass



with open('CSVs/InputData.csv', encoding='UTF-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        inputData = DataClass(row['Id'],row['Comment'],row['Date'])
    
        result = analyze_sentiment([inputData.Comment])
        doc_result = [doc for doc in result if not doc.is_error]

        for result in doc_result:
            with open('CSVs/OutPutData.csv', 'a', newline='', encoding='UTF-8') as outPut_file:
                writer = csv.writer(outPut_file, delimiter=',') 
                writer.writerow([inputData.Id, inputData.Comment, inputData.Date,result.sentiment])



