## text editor

linux 에서 주로 사용하는 텍스트 에디터는 아래와 같다

- vi
  - (visual editor)는 파일의 내용을 보여줌과 동시에 파일의 내용을 편집할 수 있게 해주는 프로그램)
- vim
  - (vi improved)이란 영어의 줄임말로 말 그대로 vi의 업그레이드 버젼, 색상으로 구분됨
- gedit
  - (GNOME Editor) 은 현재 리눅스 GUI환경에서 사용하는 텍스트 에디터(글들을 수정할 때 쓰는 프로그램) 윈도우의 메모장 같은 것

---

### mode

솔직히 별것 없다 아래와 같이 구분되어있다.

- 명령 모드(command mode) 
- 입력 모드(insert mode)
- 마지막 행 모드(Last line mode)


### command mode

- vi에서 키보드로 입력하는 것이 모두문자가 아닌, 어떤 기능을 가진 단축기로서 실행되는 모드
- 명령모드에선 키보드 "i" 를 눌렀을 때 실제 문자 'i'가 적히는게 아니라 vi의 "입력모드로 바뀌는 단축키 i(inset mode)"가 실행된다는 것
- 다시 돌아오려면 ESC 누르면 된다


### insert mode

- 입력모드이기 때문에 저희가 어떤 문자가 있는 키보드 키를 눌러도 모두 글자로 취급

### Last line mode
- CLI환경처럼 화면 맨 밑(마지막 행에) 명령어를 칠 수 있는 줄이 나오는 모드라
- : 를 누르면 맨 밑에 명령어 칠수 있는 줄이 나옴

![img src](https://2.bp.blogspot.com/-ced3DlsGZ0w/XYuTID8o7jI/AAAAAAAABjo/UpGYv2G8spA--00aiCUepEkWpW3m6FytQCK4BGAYYCw/s640/%25EB%25AA%2585%25EB%25A0%25B9%25EB%25AA%25A8%25EB%2593%259C%252C%2B%25EC%259E%2585%25EB%25A0%25A5%25EB%25AA%25A8%25EB%2593%259C%252C%2B%25EB%259D%25BC%25EC%259D%25B8%25EB%25AA%25A8%25EB%2593%259C.png)

---
## 쓸만한 단축키와 명령어들


### command mode

- yy(yank yank)
  - 한줄 저장 한줄에 대한 ctrl + c (buffer 에 저장함, p 로 붙이기 가능)

- p(paste)
  - yy 로 저장한거 붙여넣는다

- d(delete)
  - d"를 누르고 "←→"를 누르면 그 방향의 글자를 하나 지우고 "↑↓"를 누르면 커서가 있는 현재 줄과 그 방향 한 줄을 지워버림
  - 헷갈리므로 dd 를 선호한다

- dd(delete delete)
  - 커서가 있는 한줄 날린다

- u(undo) : 전에 했던 행위를 복구

- [번호] + shift + g : 입력한 번호의 행 시작부분으로 커서가 이동


### last line mode

- :set nu 
  - 파일 행에 번호 생성
- :set nonu
  - 파일 행 번호 삭제

- :! 명령어
  - 텍스트 에디터 임시로 나가서 터미널 커맨드 수행할 수 있음 enter 치면 다시 되돌아옴

- :/[찾을 문자]
  - 찾을 문자에 들어간 문자를 찾아줌
  - n 을 눌러서 아래방향으로 다음 찾을 문자로 넘어갈 수 있음
  
- :?[찾을문자]
  - /와 동일하나 방향이 위로
