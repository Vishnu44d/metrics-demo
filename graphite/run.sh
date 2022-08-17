sudo docker build -t go-graphite:lts -f Dockerfile .


sudo docker run -p 8080:80 -p 8081:8081 -p 2003-2004:2003-2004 go-graphite:lts

