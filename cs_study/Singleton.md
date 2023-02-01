## singleton design pattern


디자인 패턴의 종류 중 하나

- 객체의 인스턴스가 오직 1개만 생성되는 패턴

## singleton pattern 의 이점 과 단점

이점
- 메모리 (고정적)
- 쉬운 데이터 공유


단점
- 동시 접근시 동시성 문제 발생
- 많은 코드
- 어려운 테스트 (매번 인스턴스 초기화)
- 자식 클래스 생성 불가


효율적일 수 있으나 그에따른 문제점이 많이 수반됨 (안티패턴)


ref:https://tecoble.techcourse.co.kr/post/2020-11-07-singleton/