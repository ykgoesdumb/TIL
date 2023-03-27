## MIME

multipurpose internet mail extensions
- 파일변환
- 웹을 통하여 여러 형태이 파일을 전달하는데 사용됨

## 왜 MIME 을 사용하는가?
- 택스트만 보내던 시절 ASCII 로 보내면 문제가 없었으나 점차 음악,이미지 (바이너리 파일) 다양한 형태의 파일이 네트워크 상에서 오감
- 바이너리 파일들을 전달하기 위해 텍스트 파일로 endcoding 이 필요함

## content-type
- MIME 으로 encoding 을 하게 된다면 content-type 을 앞에 붙임
- HTTP 헤더에 보내지는 자원의 content-type 을 포함시킴
- MIME 으로 인코딩한 파일은 content-type 정보를 담게되며 content-type은 여러가지 타입이 있다.


## content-type 종류

1. Multipart Related MIME 타입
- Content-Type : Multipart/Related (기본형태)
- Content-Type : Application/X-FixedRecord


2. XML Media 타입
- Content-Type : text/xml
- Content-Type : Application/xml
- Content-Type : Application/xml-external-parsed-entity
- Content-Type : Application/xml-dtd
- Content-Type : Application/mathtml+xml
- Content-Type : Application/xslt+xml


3. Application 타입
4. 오디오 타입
5. Multipart 타입
6. Text 타입
7. file 타입






ref:https://zzandoli.tistory.com/60