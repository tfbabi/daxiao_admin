
from common.DbUtils import Model


today=datetime.now().strftime('%Y-%m-%d')


employee = DbUtils.Model()
dbsql = "SELECT * from sync_news where news_type='2' and news_publish_time >{0}".format(today)
apm_db_list = employee.fetchall(dbsql)