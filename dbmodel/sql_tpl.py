

SQL_TPL = {
    'chart1':   '''
                select fdate, count(fgameid) from gameactive where fdate>='%(sdate)s' and fdate<='%(edate)s' GROUP by fdate
                '''
}