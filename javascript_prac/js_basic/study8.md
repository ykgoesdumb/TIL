## 객체

만약 인덱스를 문자로 사용하고 싶다면 dictionary 를 사용해야한다

```js
//객체 만드는 방법
//1
var power = {'kyle': 10, 'sunny': 50, 'zonnastrong': 90};

//2
var power = {};
power['kyle'] = 10;
power['sunny'] = 50;
power['zonnastrong'] = 90;

//3
var power = new Object();
power['kyle'] = 10;
power['sunny'] = 50;
power['zonnastrong'] = 90;


//만들어진 객체에 접근하는 방법
//1
alert(power['kyle'])
//2
alert(power.kyle)


//반복문
for(key in power){
    database.write("key : " +key +" value : " +power[key] )
}                    // power.key 로 변경하면 작동하지 않는다


//함수도 혼합적으로 담을 수 있으며 객체 안에 객체도 담을 수 있다
var grades = {
    'list': {'egoing': 10, 'k8805': 6, 'sorialgi': 80},
    'show' : function(){
        for(var name in this.list){
            document.write(name+':'+this.list[name]+"<br />");
        }
    }
};
grades.show();
```