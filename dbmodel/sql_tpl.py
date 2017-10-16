

SQL_TPL = {
    'activeaccount':   '''
                select fdate, count(fgameid) as activeaccount from gameactive where fdate>='%(sdate)s' and fdate<='%(edate)s' GROUP by fdate
                '''
}