

## docker compose

docker compose 구성중 postgres 를 두개를 띄우는 상황이였음
<br>

아래의 db 들이 postgres 를 사용
- metastore-db
- airflow-db

라이브러리 이슈로 둘이 다른 버전을 사용해야했음
- 문제는 둘다 container port 가 5432 로 지정되어있었음
- 하나의 postgres db container 에 두가지 서비스가 동작 안함

### 해결방법
- expose 후
- expose 한  포트 선언
- command 추가
  - -p (port-number)

```yaml
version: "3.7"
x-airflow-image: &airflow_image my-image
services:
  postgres:
    image: postgres:11
    restart: always
    container_name: postgres
    environment:
      - POSTGRES_USER=airflow
      - POSTGRES_PASSWORD=airflow
      - POSTGRES_DB=airflow
    expose:
      - "6000"
    ports:
      - "6000:6000"
    command: -p 6000

  metastore-db:
    image: postgres:15.1
    restart: always
    container_name: metastore-db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
      POSTGRES_DB: metastore
    ports:
      - "5432:5432"
```
- postgres(airflow-db)를 6000 번으로 빼주고 command 로 6000번 포트를 선언한 모습


