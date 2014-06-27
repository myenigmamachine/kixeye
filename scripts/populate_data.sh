#! /bin/bash

for i in $(seq 1 100); do 
    NUMBER=$[ ( $RANDOM % 100 )  + 1 ];
    data="first=Danny&last=Key&nickname=$NUMBER"
    echo $data
    curl -X POST https://tools-dev2.lab.nbttech.com:3019/users \
        -d $data -uadmin:password --insecure
    sleep 1
done

for i in $(seq 1 100); do 
    NUMBER1=$[ ( $RANDOM % 100 )  + 1 ];
    NUMBER2=$[ ( $RANDOM % 100 )  + 1 ];
    NUMBER3=$[ ( $RANDOM % 100 )  + 1 ];
    DATE1=`date "+%m-%e-%YT%H:%M:%S"`
    sleep 1
    DATE2=`date "+%m-%e-%YT%H:%M:%S"`
    data="attacker=$NUMBER1&defender=$NUMBER2&winner=$NUMBER3&start=$DATE1&end=$DATE2"
    echo $data
    curl -X POST https://tools-dev2.lab.nbttech.com:3019/battles \
        -d $data \
        -uadmin:password --insecure
done
