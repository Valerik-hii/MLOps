import csv

#Читай входной файл
with open('dvc_homework/raw_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    total = sum(float(row['mass']) for row in reader)

#Результат сохраняй вот сюда
with open('metrics.txt', 'w') as f:
    f.write(f"Total mass: {total}\n")
    
print(f"Pipeline finished! Total mass: {total}")
