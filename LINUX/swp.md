## swp file

- 갑자기 시스템이 꺼지거나, ssh 도중 인터넷이 끊겨버릴때 저장 안한것 다 날아가나?

- 그것을 대비해 만들어놓은것이 .swp file 이다
  - swap file 스왑파일 이라고 한다

- 그것을 복구하는 것이 "-r" 옵션이다


vi 작업하다가 터미널을 종료한경우 .swp 파일 자동 생성

```
ls -a
.          ..         .test2.swp     test2
```

```
vim -r test2

```
- 복구하면 저장은 되지 않은 상태
- :wq 로 저장을 해주어야한다



### Attention

- -r 옵션없이 복구하는 방법
- 중단된 파일을 열어보면
- Attention 이 뜸



![img src](https://lh3.googleusercontent.com/-1bHPl-4M0rA/YHwOZQLdhJI/AAAAAAAAGQs/cKe--TkJiJg6l2Y2EhK5gBj6VIHhmUrQwCLcBGAsYHQ/36.png)

- 밑에 옵션대로 작업을 수행하면된다


### vi -r

- 파일명 없이 명령어를 칠경우

```
vi -r
스왑 파일을 찾았음:
   현재 디렉토리에:
1.    .test2.swp
          소유자: kylekim1223   날짜: 금  3 03 13:27:45 2023
         파일 이름: ~kylekim1223/myspace/TIL/testin/test2
          수정: 예
         사용자 이름: kylekim1223  호스트 이름: kylekim1223ui-MacBookPro.local
        프로세스 ID: 77731
   In directory ~/tmp:
      -- 없음 --
   In directory /var/tmp:
      -- 없음 --
   In directory /tmp:
      -- 없음 --
```

### vi -p[숫자]

- 한번에 여러개를 만듬

### ATTENTION 페이지에서 quit 과 abort 차이
- 여러개의 페이지가 있을때 quit 은 그 한페이지를 닫는것
- abort 는 전체를 닫아버림
- 엑셀의 스프레드 시트 하나를 닫는것과, 엑셀 파일 전체를 닫는것과 같다고 보면 된다

---

