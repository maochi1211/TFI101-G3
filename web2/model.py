import pymysql

def search_ROI(company,forecast_date):
    connectInfo = {
        'host': 'tfi10103.ctlciggyxwly.ap-northeast-1.rds.amazonaws.com',
        'port': 3306,
        'user': 'admin',
        'passwd': 'tfi10103',
        'db': 'mysqldb',
        'charset': 'utf8mb4'
    }
    search_company = company
    result_date = forecast_date
    conn = pymysql.connect(**connectInfo)
    cursor = conn.cursor()

    if len(result_date) == 1:
        sql_query = f"""select StockDate,ret_3,ret_5,ret_10,ret_20,ret_60 from {search_company}
         where StockDate = '{result_date[0]}'
         ORDER BY StockDate; """
    elif len(result_date) > 1:
        sql_query = f"""select StockDate,ret_3,ret_5,ret_10,ret_20,ret_60 from {search_company}
         where StockDate in {tuple(result_date)}
         ORDER BY StockDate; """
    else:
        sql_query = f"""select StockDate,ret_3,ret_5,ret_10,ret_20,ret_60 from {search_company}
         where StockDate is NULL
         ORDER BY StockDate; """
    print(sql_query)
    cursor.execute(sql_query)
    data = cursor.fetchall()
    return data




