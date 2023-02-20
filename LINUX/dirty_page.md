# dirty page


### page cache
파일 I/O 가 발생할 때 page Cache를 이용해서 디스크에 있는 파일의 내용을 메모리에 저장하고 이를 필요할때마다 메모리에서 접근해서 사용 -> 메모리에 접근하는게 빠르므로 시스템 성능 향상

- Write back 방식에서 page cache는 사용자 프로세스가 읽기 또는 쓰기를 시작할 때마다 사용되며 커널은 사용자가 작업중인 파일의 사본을 찾으며 그러한 사본이없는 경우 캐시 메모리의 한 페이지를 새로 할당하고 디스크에서 읽은 해당 내용을 적재

- page cache 는 linux 에서 유동적으로 할당
- 임의적으로 disable 할 수 없다


## what is dirty page?
- 읽은 파일이 디스크에 업데이트 되지 않고 page cache 내 특정 공간에만 업데이트 되어 있는 경우가 있는데 이때 그 특정 공간을 dirty page라고 함

- 해당 메모리 영역 (page cache)에 대해서 디스크에 있는 내용과 달라졌음을 표시하는 "Dirty bit"를 켜고 이 영역을 dirty page 라고 함

- dirtypage 는 page cache 에 있는 page 중에서 write 가 이루어진 메모리


## dirty page 가 왜 문제인가?

- page cache 와 디스크 사이의 내용이 다르기 때문에 파일의 내용에 대한 정합성 깨짐
- dirty page 로 표시된 메모리들이 생성될때마다 disk 에 write 하면 I/O를 크게 일으켜 성능을 저하시킬 수 있다.
- 설정(dirty_ratio)보다 많은 dirty page를 지속적으로 사용하게 되면 linux에서는 flushing을 정상적으로 수행하지 못하는 것으로 판단하고 write를 중지. 거기에 상태 D 프로세스 증가시키며 높은 load average까지 발생시킴

- page writeback (dirty page 동기화, flushing) 를 통해 dirty page를 디스크로 동기화 해야한다


ref: 
- https://youngswooyoung.tistory.com/68
- https://17billion.github.io/linux/2017/08/10/linux_page_cache_dirty_page.html
