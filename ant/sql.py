#coding = utf-8

schema_stat = "SELECT table_schema,round(sum(data_length) / 1024 / 1024 / 1024,2) AS `data_size`,round(sum(INDEX_LENGTH) / 1024 / 1024 / 1024,2) AS `index_size`,count(table_name) AS table_count,round(sum(data_length) / 1024 / 1024 / 1024,2)+round(sum(INDEX_LENGTH) / 1024 / 1024 / 1024,2) as total FROM information_schema.TABLES WHERE table_schema NOT IN ('mysql','information_schema','performance_schema','sys') GROUP BY table_schema;"

top10_stat = "SELECT table_schema,table_name,round(data_length / 1024 / 1024 / 1024,2) AS data_size,round(table_rows / 10000, 2) rows,round(index_length / 1024 / 1024 / 1024,2) AS index_size,round(data_length / 1024 / 1024 / 1024,2)+round(INDEX_LENGTH / 1024 / 1024 / 1024,2) as total FROM information_schema.TABLES WHERE table_schema NOT IN ('mysql','information_schema','performance_schema','sys') ORDER BY total,rows DESC LIMIT 10;"

notInnodb_stat = "select table_schema,table_name,engine from information_schema.TABLES where table_schema NOT IN ('mysql','information_schema','performance_schema','sys') and (engine <> 'InnoDB');"


