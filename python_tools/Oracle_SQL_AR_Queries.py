#リカルドに作れたプログラム
#自動的なメールを送るのために。
import cx_Oracle as oracledb
import time
from datetime import date
from datetime import timedelta
from datetime import datetime

#connection = cx_Oracle.connect("apps/pr4d1ppsrv@10.32.252.22:1521/DBGLPRD")
#connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.22:1521/DBGLPRD", encoding="UTF-8")
#cursor1 = connection.cursor()
#cursor2 = connection.cursor()
#cursor3 = connection.cursor()
#cursor4 = connection.cursor()
#cursor5 = connection.cursor()
#cursor6 = connection.cursor()

def AR_Files_Queries():

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()
    cursor6 = connection.cursor()
    cursor7 = connection.cursor()
    cursor8 = connection.cursor()
    cursor9 = connection.cursor()
    cursor10 = connection.cursor()

    string_query = ''
    cursor1.execute("SELECT 'FAC_ENC_CO: ' || COUNT(*) || '/47' AS FAC_ENC_CO FROM logs_table where table_name like '%Fac_enc%' and country_code = 'CO' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor2.execute("SELECT 'FAC_DET_CO: ' || COUNT(*) || '/47' AS FAC_DET_CO FROM logs_table where table_name like '%Fac_det%' and country_code = 'CO' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor3.execute("SELECT 'FAC_ENC_CR: ' || COUNT(*) || '/14' AS FAC_ENC_CR FROM logs_table where table_name like '%Fac_enc%' and country_code = 'CR' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor4.execute("SELECT 'FAC_DET_CR: ' || COUNT(*) || '/14' AS FAC_DET_CR FROM logs_table where table_name like '%Fac_det%' and country_code = 'CR' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor5.execute("SELECT 'FAC_ENC_EC: ' || COUNT(*) || '/20' AS FAC_ENC_EC FROM logs_table where table_name like '%Fac_enc%' and country_code = 'EC' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor6.execute("SELECT 'FAC_DET_EC: ' || COUNT(*) || '/20' AS FAC_DET_EC FROM logs_table where table_name like '%Fac_det%' and country_code = 'EC' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor7.execute("SELECT 'FAC_ENC_HO: ' || COUNT(*) || '/10' AS FAC_ENC_HO FROM logs_table where table_name like '%Fac_enc%' and country_code = 'HN' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor8.execute("SELECT 'FAC_DET_HO: ' || COUNT(*) || '/10' AS FAC_DET_HO FROM logs_table where table_name like '%Fac_det%' and country_code = 'HN' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor9.execute("SELECT 'FAC_ENC_GT: ' || COUNT(*) || '/20' AS FAC_ENC_GT FROM logs_table where table_name like '%Fac_enc%' and country_code = 'GT' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor10.execute("SELECT 'FAC_DET_GT: ' || COUNT(*) || '/20' AS FAC_DET_GT FROM logs_table where table_name like '%Fac_det%' and country_code = 'GT' AND substr(table_name,24,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    
    rows1 = cursor1.fetchall()
    for row in rows1:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows2 = cursor2.fetchall()
    for row in rows2:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows3 = cursor3.fetchall()
    for row in rows3:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows4 = cursor4.fetchall()
    for row in rows4:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows5 = cursor5.fetchall()
    for row in rows5:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows6 = cursor6.fetchall()
    for row in rows6:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows7 = cursor7.fetchall()
    for row in rows7:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows8 = cursor8.fetchall()
    for row in rows8:
        #print(row)
        string_query = string_query + str(row) + '\n'  
    rows9 = cursor9.fetchall()
    for row in rows9:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows10 = cursor10.fetchall()
    for row in rows10:
        #print(row)
        string_query = string_query + str(row) + '\n' 

    characters_to_remove = "(),'"
    clean_string_query = string_query

    # Removing specified characters
    for char in characters_to_remove:
        clean_string_query = clean_string_query.replace(char, '')

    connection.close()
    now = datetime.now()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterdayx = yesterday.strftime("%d/%m/%y")
    final_query = '\n' + clean_string_query + '\n' + 'Fecha de los archivos depositados: ' + yesterdayx + '\n' + 'Fecha generación de Notificación: ' + str(now)
    return final_query

def AR_Files_Sended_Stage_Queries_old():

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()
    cursor6 = connection.cursor()
    cursor7 = connection.cursor()
    cursor8 = connection.cursor()

    string_query = ''
    cursor1.execute("SELECT 'AR_LINES_CO: ' || COUNT(*) || '/47' FROM ar_file_summary where file_name like '%PLC_ae_fa_0%' and country_code = 'CO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor2.execute("SELECT 'AR_HEADERS_CO: ' || COUNT(*) || '/47' FROM ar_file_summary where file_name like '%PLC%fac%' and country_code = 'CO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor3.execute("SELECT 'AR_LINES_CR: ' || COUNT(*) || '/14' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'CR' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor4.execute("SELECT 'AR_HEADERS_CR: ' || COUNT(*) || '/14' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'CR' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor5.execute("SELECT 'AR_LINES_EC: ' || COUNT(*) || '/20' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'EC' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor6.execute("SELECT 'AR_HEADERS_EC: ' || COUNT(*) || '/20' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'EC' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor7.execute("SELECT 'AR_LINES_HO: ' || COUNT(*) || '/10' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'HO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor8.execute("SELECT 'AR_HEADERS_HO: ' || COUNT(*) || '/10' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'HO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")

    rows1 = cursor1.fetchall()
    for row in rows1:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows2 = cursor2.fetchall()
    for row in rows2:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows3 = cursor3.fetchall()
    for row in rows3:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows4 = cursor4.fetchall()
    for row in rows4:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows5 = cursor5.fetchall()
    for row in rows5:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows6 = cursor6.fetchall()
    for row in rows6:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows7 = cursor7.fetchall()
    for row in rows7:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows8 = cursor8.fetchall()
    for row in rows8:
        #print(row)
        string_query = string_query + str(row) + '\n'    

    characters_to_remove = "(),'"
    clean_string_query = string_query

    # Removing specified characters
    for char in characters_to_remove:
        clean_string_query = clean_string_query.replace(char, '')

    connection.close()
    now = datetime.now()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterdayx = yesterday.strftime("%d/%m/%y")
    final_string_query = '\n' + clean_string_query + '\n' + 'Fecha de los archivos cargados: ' + yesterdayx + '\n' + 'Fecha generación de Notificación: ' + str(now)
    return final_string_query

def AR_Files_Sended_Stage_Queries():

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()
    cursor6 = connection.cursor()
    cursor7 = connection.cursor()
    cursor8 = connection.cursor()
    cursor9 = connection.cursor()
    cursor10 = connection.cursor()

    string_query = ''
    cursor1.execute("SELECT 'AR_LINES_CO: ' || COUNT(distinct(substr(file_name,15,6))) || '/47' FROM ar_file_summary where file_name like '%PLC_ae_fa_0%' and country_code = 'CO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor2.execute("SELECT 'AR_HEADERS_CO: ' || COUNT(distinct(substr(file_name,21,6))) || '/47' FROM ar_file_summary where file_name like '%PLC%fac%' and country_code = 'CO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor3.execute("SELECT 'AR_LINES_CR: ' || COUNT(distinct(substr(file_name,15,6))) || '/14' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'CR' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor4.execute("SELECT 'AR_HEADERS_CR: ' || COUNT(distinct(substr(file_name,21,6))) || '/14' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'CR' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor5.execute("SELECT 'AR_LINES_EC: ' || COUNT(distinct(substr(file_name,15,6))) || '/20' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'EC' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor6.execute("SELECT 'AR_HEADERS_EC: ' || COUNT(distinct(substr(file_name,21,6))) || '/20' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'EC' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor7.execute("SELECT 'AR_LINES_HO: ' || COUNT(distinct(substr(file_name,15,6))) || '/10' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'HO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor8.execute("SELECT 'AR_HEADERS_HO: ' || COUNT(distinct(substr(file_name,21,6))) || '/10' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'HO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor9.execute("SELECT 'AR_LINES_GT: ' || COUNT(distinct(substr(file_name,15,6))) || '/10' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'GT' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor10.execute("SELECT 'AR_HEADERS_GT: ' || COUNT(distinct(substr(file_name,21,6))) || '/10' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'GT' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")

    rows1 = cursor1.fetchall()
    for row in rows1:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows2 = cursor2.fetchall()
    for row in rows2:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows3 = cursor3.fetchall()
    for row in rows3:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows4 = cursor4.fetchall()
    for row in rows4:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows5 = cursor5.fetchall()
    for row in rows5:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows6 = cursor6.fetchall()
    for row in rows6:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows7 = cursor7.fetchall()
    for row in rows7:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows8 = cursor8.fetchall()
    for row in rows8:
        #print(row)
        string_query = string_query + str(row) + '\n'  
    rows9 = cursor9.fetchall()
    for row in rows9:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows10 = cursor10.fetchall()
    for row in rows10:
        #print(row)
        string_query = string_query + str(row) + '\n' 

    characters_to_remove = "(),'"
    clean_string_query = string_query

    # Removing specified characters
    for char in characters_to_remove:
        clean_string_query = clean_string_query.replace(char, '')

    connection.close()
    now = datetime.now()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterdayx = yesterday.strftime("%d/%m/%y")
    final_string_query = '\n' + clean_string_query + '\n' + 'Fecha de los archivos cargados: ' + yesterdayx + '\n' + 'Fecha generación de Notificación: ' + str(now)
    return final_string_query

def AR_Files_Sended_Stage_Queries_by_day(Days_before):

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()
    cursor6 = connection.cursor()
    cursor7 = connection.cursor()
    cursor8 = connection.cursor()
    cursor9 = connection.cursor()
    cursor10 = connection.cursor()

    string_query = ''
    cursor1.execute("SELECT 'AR_LINES_CO: ' || COUNT(distinct(substr(file_name,15,6))) || '/47' FROM ar_file_summary where file_name like '%PLC_ae_fa_0%' and country_code = 'CO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor2.execute("SELECT 'AR_HEADERS_CO: ' || COUNT(distinct(substr(file_name,21,6))) || '/47' FROM ar_file_summary where file_name like '%PLC%fac%' and country_code = 'CO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor3.execute("SELECT 'AR_LINES_CR: ' || COUNT(distinct(substr(file_name,15,6))) || '/14' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'CR' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor4.execute("SELECT 'AR_HEADERS_CR: ' || COUNT(distinct(substr(file_name,21,6))) || '/14' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'CR' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor5.execute("SELECT 'AR_LINES_EC: ' || COUNT(distinct(substr(file_name,15,6))) || '/20' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'EC' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor6.execute("SELECT 'AR_HEADERS_EC: ' || COUNT(distinct(substr(file_name,21,6))) || '/20' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'EC' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor7.execute("SELECT 'AR_LINES_HO: ' || COUNT(distinct(substr(file_name,15,6))) || '/10' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'HO' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor8.execute("SELECT 'AR_HEADERS_HO: ' || COUNT(distinct(substr(file_name,21,6))) || '/10' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'HO' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor9.execute("SELECT 'AR_LINES_GT: ' || COUNT(distinct(substr(file_name,15,6))) || '/10' FROM ar_file_summary where file_name like '%PCA_ae_fa_0%' and country_code = 'GT' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")
    cursor10.execute("SELECT 'AR_HEADERS_GT: ' || COUNT(distinct(substr(file_name,21,6))) || '/10' FROM ar_file_summary where file_name like '%PCA%fac%' and country_code = 'GT' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')")

    rows1 = cursor1.fetchall()
    for row in rows1:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows2 = cursor2.fetchall()
    for row in rows2:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows3 = cursor3.fetchall()
    for row in rows3:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows4 = cursor4.fetchall()
    for row in rows4:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows5 = cursor5.fetchall()
    for row in rows5:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows6 = cursor6.fetchall()
    for row in rows6:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows7 = cursor7.fetchall()
    for row in rows7:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows8 = cursor8.fetchall()
    for row in rows8:
        #print(row)
        string_query = string_query + str(row) + '\n' 
    rows9 = cursor9.fetchall()
    for row in rows9:
        #print(row)
        string_query = string_query + str(row) + '\n'
    rows10 = cursor10.fetchall()
    for row in rows10:
        #print(row)
        string_query = string_query + str(row) + '\n'    

    characters_to_remove = "(),'"
    clean_string_query = string_query

    # Removing specified characters
    for char in characters_to_remove:
        clean_string_query = clean_string_query.replace(char, '')

    connection.close()
    now = datetime.now()
    today = date.today()
    yesterday = today - timedelta(days = Days_before)
    yesterdayx = yesterday.strftime("%d/%m/%y")
    final_string_query = '\n' + clean_string_query + '\n' + 'Fecha de los archivos cargados: ' + yesterdayx + '\n' + 'Fecha generación de Notificación: ' + str(now)
    return final_string_query

def Policy_summary_headers(Server):
    if Server == 'MX':
        dsn_String = "10.32.252.28:1521/DBGLPRD"
    elif Server == 'LAS':
        dsn_String = "10.32.252.204:1521/DBGLPRD"
    elif Server == 'LAC':
        dsn_String = "10.32.252.244:1521/DBGLPRD"
    else:
        print('invalid option')
    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn = dsn_String, encoding="UTF-8")
    cursor1 = connection.cursor()
    #elif Server == 'LAC':
        #connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
        #cursor1 = connection.cursor()
    #elif Server == 'LAS':
        #connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.204:1521/DBGLPRD", encoding="UTF-8")
        #cursor1 = connection.cursor()
    #else:
        #print('invalid option')

    string_query = ''
    cursor1.execute("SELECT 'Origen: '|| country || '-' || legal_entity || ' Estatus: ' || policty_status || ' Cantidad: '|| policy_count || ' Inicio: ' || Substr(firts_policy, 1,14) || ' Duración: ' || substr(duration,12,8) FROM view1view_policy_summary_headers WHERE policy_date = TO_CHAR(SYSDATE - 1, 'DD/MM/YY')")
    
    rows1 = cursor1.fetchall()
    for row in rows1:
        #print(row)
        string_query = string_query + str(row) + '\n'

    characters_to_remove = "(),'"
    clean_string_query = string_query

    # Removing specified characters
    for char in characters_to_remove:
        clean_string_query = clean_string_query.replace(char, '')

    connection.close()
    now = datetime.now()
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterdayx = yesterday.strftime("%d/%m/%y")
    final_string_query = '\n' + clean_string_query + '\n' + 'Fecha de los archivos cargados: ' + yesterdayx + '\n' + 'Fecha generación de Notificación: ' + str(now)
    return final_string_query

def Ask_for_received_SSC(Country_code):

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()

    cursor1.execute("SELECT distinct(substr(file_name,15,6)) FROM ar_file_summary WHERE country_code = '" + str(Country_code) + "' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")
    cursor2.execute("SELECT distinct(substr(file_name,21,6)) FROM ar_file_summary WHERE country_code = '" + str(Country_code) + "' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - 1, 'YYYYMMDD')")

    headers_ssc_list = []
    lines_ssc_list = []
    
    rows1 = cursor1.fetchall()
    for row1 in rows1:
        lines_ssc_list.append(row1)

    rows2 = cursor2.fetchall()
    for row2 in rows2:
        headers_ssc_list.append(row2)

    characters_to_remove1 = "(),'"
    characters_to_remove2 = "(),'"
    headers_final_list = []
    lines_final_list = []

    for item1 in headers_ssc_list:
        cleaned_item1 = item1[0]  # Accessing the string within each tuple
        for char1 in characters_to_remove1:
            cleaned_item1 = cleaned_item1.replace(char1, '')
        headers_final_list.append(cleaned_item1)

    for item2 in lines_ssc_list:
        cleaned_item2 = item2[0]  # Accessing the string within each tuple
        for char2 in characters_to_remove2:
            cleaned_item2 = cleaned_item2.replace(char2, '')
        lines_final_list.append(cleaned_item2)

    connection.close()
    return headers_final_list, lines_final_list

def AR_Files_received_SSC(Country_code, Days_before):

    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()

    cursor1.execute("SELECT distinct(substr(file_name,15,6)) FROM ar_file_summary where country_code = '" + str(Country_code) + "' AND substr(file_name,22,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')") #lines
    cursor2.execute("SELECT distinct(substr(file_name,21,6)) FROM ar_file_summary where country_code = '" + str(Country_code) + "' AND substr(file_name,28,8) = TO_CHAR(SYSDATE - "+ str(Days_before) +", 'YYYYMMDD')") #long title (header)
    
    headers_ssc_list = []
    lines_ssc_list = []
    
    rows1 = cursor1.fetchall()
    for row1 in rows1:
        lines_ssc_list.append(row1)
        print(row1)
        print('HI')

    rows2 = cursor2.fetchall()
    for row2 in rows2:
        headers_ssc_list.append(row2)
        print(row2)

    characters_to_remove1 = "(),'"
    characters_to_remove2 = "(),'"
    headers_final_list = []
    lines_final_list = []

    for item1 in headers_ssc_list:
        cleaned_item1 = item1[0]  # Accessing the string within each tuple
        for char1 in characters_to_remove1:
            cleaned_item1 = cleaned_item1.replace(char1, '')
        headers_final_list.append(cleaned_item1)

    for item2 in lines_ssc_list:
        cleaned_item2 = item2[0]  # Accessing the string within each tuple
        for char2 in characters_to_remove2:
            cleaned_item2 = cleaned_item2.replace(char2, '')
        lines_final_list.append(cleaned_item2)

    connection.close()
    return headers_final_list, lines_final_list



def insert_into_ar_file_summary(file_name):
    # Generate current date and time
    current_datetime = datetime.now()
    file_date = current_datetime.strftime("%Y-%m-%d")
    file_hour = current_datetime.strftime("%H:%M:%S")
    
    # Extract first three characters from file_name
    file_inf = file_name[:3]
    aux1 = 'ST'
    
    if '_068_' in file_name:
        country_code = "CO"
    elif '_044_' in file_name:
        country_code = "EC"
    elif '_099_' in file_name:
        country_code = "HO"
    elif '_095_' in file_name:
        country_code = "CR"
    elif '_090_' in file_name:
        country_code = "GT"
    else:
        country_code = "UK"

    # Determine file_type based on file_name
    if '_ae_facifctl_' in file_name:
        file_type = "Header / Cabecera"
    elif '_ae_fa_' in file_name:
        file_type = "Lines / Lineas"
    else:
        file_type = "Unknown"  # Default value if no match is found
    
    # Database connection parameters
    connection = oracledb.connect(user="apps", password='pr4d1ppsrv', dsn="10.32.252.244:1521/DBGLPRD", encoding="UTF-8")
    
    try:
        cursor = connection.cursor()
        
        # Insert statement
        insert_sql = """
        INSERT INTO AR_FILE_SUMMARY (
            COUNTRY_CODE, FILE_DATE, FILE_HOUR, FILE_INF, FILE_NAME, FILE_TYPE, AUX1
        ) VALUES (
            :1, :2, :3, :4, :5, :6, :7
        )
        """
        
        # Execute the insert statement
        cursor.execute(insert_sql, (country_code, file_date, file_hour, file_inf, file_name, file_type, aux1))
        
        # Commit the transaction
        connection.commit()
        
        print("Record inserted successfully")
        
    except oracledb.DatabaseError as e:
        print(f"Database error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def Policy_summary_headers_MX():
    PS_head = Policy_summary_headers('MX')
    return PS_head

def Policy_summary_headers_LAC():
    PS_head = Policy_summary_headers('LAC')
    return PS_head

def Policy_summary_headers_LAS():
    PS_head = Policy_summary_headers('LAS')
    return PS_head

#try_string = ''
#try_string = AR_Files_Queries()
#now = datetime.now()
#print(try_string + '\n' + str(now))
try_string = AR_Files_Sended_Stage_Queries()
print(try_string)

#VIEW_POLICY_SUMMARY_HEADERS

#cc = 'CO'
#try_list1, try_list2 = Ask_for_received_SSC(cc)
#print(try_list1)
#print(try_list2)

#cc = 'EC'
#try_list1, try_list2 = AR_Files_received_SSC(cc, 1)
#print(try_list1)
#print(try_list2)
    
#try12 = Policy_summary_headers('LAS')
#print(try12)

#insert_into_ar_file_summary('JP', 'PLJ_ae_fa_068_014235_20240531')