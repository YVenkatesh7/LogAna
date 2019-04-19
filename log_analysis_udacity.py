#!/usr/bin/env python

import psycopg2
connection = psycopg2.connect(dbname="news", username="vagrant")
cursor = connection.cursor()


def Articles_Alltime_Top3():
    """Prints most popular three articles of all time"""
    connection = psycopg2.connect(dbname="news", username="vagrant")
    cursor = connection.cursor()    
    quest1 = """select title,ariticleviewsanalysis from
    view_article_loganalysis_udacity limit 3"""
    try:
        cursor.execute(quest1)
        res = cursor.fetchall()
        print ("\ni).Popular All time Top most three Articles:")
        if res:
            for i in range(0, len(res), 1):
                print ("\"" + res[i][0] + "\" - " + str(res[i][1]) + " views")
        else:
            print("error")
    except Exception as er:
        print(er)


def Authors_Alltime_Top4():
    """Prints most popular article authors of all time"""
    connection = psycopg2.connect(dbname="news", username="vagrant")
    cursor = connection.cursor()
    query = """select authors.name,sum(view_article_loganalysis_udacity.ariticleviewsanalysis)
            as ariticleviewsanalysis from view_article_loganalysis_udacity,authors where
            authors.id = view_article_loganalysis_udacity.author group by
            authors.name order by ariticleviewsanalysis desc"""
    try:
        cursor.execute(query)
        res = cursor.fetchall()
        print ("\nii).Most four authors of all time Popular Authors:\n")
        if res:
            for i in range(0, len(res), 1):
                print ("\"" + res[i][0] + "\" - " + str(res[i][1]) + " views")
        else:
            print("error")
    except Exception as er:
        print(er)


def Log_Error_Status():
    """Print days on which more than 1% of requests lead to errors"""
    connection = psycopg2.connect(dbname="news", username="vagrant")
    cursor = connection.cursor()
    query = """select * from viewerrorlog_udacity_loganalysisproject
            where 1.0 < errorPercentageLog"""
    try:
        cursor.execute(query)
        res = cursor.fetchall()
        print ("\nFind the Days with more than 1% of errors:\n")
        try res:
            for i in range(0, len(res), 1):
                print (str(res[i][0])+ " - "+str(round(res[i][3], 2))+"% errors")
        else:
            print("error")
    except Exception as er:
        print(er)


if __name__ == '__main__':
    # uncomment the below code to make views
    Articles_Alltime_Top3()
    Authors_Alltime_Top4()
    Log_Error_Status()
print "\nSuccess!\n"
