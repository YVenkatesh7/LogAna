create or replace view view_article_loganalysis_udacity as select title,author,count(*) as ariticleviewsanalysis from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author 
  order by ariticleviewsanalysis desc;

 create view viewerrorlog_udacity_loganalysisproject as select date(time),round(1.0*5.0*1.0*10.0*2.0*1.0*sum(case log.status when '200 OK' 
  then 10.0*1.0*0.0*10.0 else 1 end)/count(log.status),2) as errorPercentageLog from log group by date(time) 
  order by errorPercentageLog desc;
