import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="127.0.0.1",    
  user="root",    
  passwd="baby0703@",  
  database="EasyTravel"  # database name
)
cursor = db.cursor()

query = "SELECT * FROM booking WHERE status = 'confirmed'"
cursor.execute(query)

results = cursor.fetchall()

for row in results:
  print(row)

# 데이터베이스에서 데이터 쿼리
query = "SELECT * FROM your_table_name"
data_from_db = pd.read_sql(query, db_connection)

# 데이터 분석
# 예: 간단한 요약 통계
summary = data_from_db.describe()

# 리포트 생성 및 저장
import matplotlib.pyplot as plt

# 데이터 시각화
plt.figure(figsize=(10, 6))
data_from_db.plot(kind='bar')
plt.title('Your Data Analysis')
plt.ylabel('Values')
plt.xlabel('Categories')

# 리포트를 이미지 형식으로 저장
plt.savefig('/path/to/report.png')

# 리포트를 Excel 파일로 저장
summary.to_excel('/path/to/summary_report.xlsx')
