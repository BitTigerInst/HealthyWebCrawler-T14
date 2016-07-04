
Mongo Connector Settings
------------------------

1) start mongo: mongod --replSet myDevReplSet
2) then in mongo shell: rs.initiate()
3) start ES: elasticsearch 
4) mongo-connector -m localhost:27017 -t localhost:9200 -d elastic2_doc_manager
5) Test connection: curl http://localhost:9200
6) list existing ES index: curl 'localhost:9200/_cat/indices?v'
7) Search apps with rating 10:curl http://localhost:9200/scrapy/_search/?rating=10
8)ES search documents: https://www.elastic.co/guide/en/elasticsearch/reference/1.4/_executing_searches.html
<br>
Debugging: Setting /data/db ownership right––Note: use your own user name, not "evah"!!!! http://www.mkyong.com/mongodb/how-to-install-mongodb-on-mac-os-x/ 
```
 $ sudo mkdir -p /data/db 
 $ whoami 
 evah 
 $ sudo chown evah /data/db
```
