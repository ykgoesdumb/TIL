## No Space Left On Device

### 삭제시 로컬에 저장된 모든 이미지가 날아간다

- 재시동시 다시 생성됨 (지워도 무방하다)
```
 rm -rf ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2
```

### 주기적으로 볼륨제거 필요하다

```
# 볼륨제거
echo "remote volumn"
docker volume rm $(docker volume ls -qf dangling=true)

# 이미지 제거
echo "remote docker images"
docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
docker images -a | sed '1 d' | awk '{print $3}' | xargs -L1 docker rmi -f
```


## REF
https://www.hahwul.com/2018/08/16/docker-no-space-left-on-device-in-macos/