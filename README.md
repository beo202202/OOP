<h1>객체 지향</h1>
<br>
<h3 data-ke-size="size23">캡슐화</h3>
<ul style="list-style-type: disc;" data-ke-list-type="disc">
<li>객체 지향 프로그래밍에서 중요한 개념 중 하나</li>
<li>객체의 내부 상태를 보호하고, 객체와 객체 간의 상호 작용을 제어하는 것을 의미</li>
<li>객체 내부에 있는 데이터나 메서드에 직접 접근하지 않고, 외부에서는 인터페이스를 통해 접근하도록 제한함으로써 캡슐화를 구현할 수 있습니다.</li>
</ul>
<h4 data-ke-size="size20">get_speed 로 캡슐화</h4>
<ul style="list-style-type: circle;" data-ke-list-type="circle">
<li>객체의 상태 중 하나인 속도(speed)를 반환하는 메서드를 의미</li>
<li>일반적으로 외부에서 객체의 속도를 확인하기 위해 사용</li>
<li>객체 내부에서 속도 값을 직접적으로 노출하지 않고, 인터페이스를 통해 접근하도록 캡슐화를 구현할 수 있습니다.</li>
<li>외부에서는 속도 값을 확인할 수 있지만, 객체 내부의 속도 값을 변경 할 수는 없습니다.</li>
</ul>
<pre>
<code>
class Car():
    def __init__(self, model, color, speed):
        self.model = "Ford"
        self.color = "red"
        self.speed = 0

    def accelerate(self, accels):
        self.speed += accels
        if (self.speed &gt; 100):
            self.speed = 100
    
    def brake(self, braks):
        self.spped -= braks
        if (self.speed &lt; 0):
            self.speed = 0
    
    def get_speed(self):
        return self.speed
</code>
</pre>
<br>
<h3 data-ke-size="size23">메서드 오버라이딩</h3>
<ul style="list-style-type: disc;" data-ke-list-type="disc">
<li>객체 지향 프로그래밍에서 중요한 개념 중 하나</li>
<li>부모 클래스에서 정의된 메서드를 자식 클래스에서 다시 정의하여, 자식 클래스에서 원하는 방식으로 동작하도록 하는 것을 의미</li>
<li>자식 클래스에서는 부모 클래스에서 정의된 메서드의 기능을 유지하면서도, 필요한 부분만 수정하여 사용할 수 있습니다.</li>
</ul>
<h4 data-ke-size="size20">speack로 메서드 오버라이딩</h4>
<ul style="list-style-type: circle;" data-ke-list-type="circle">
<li>객체 내부의 'speak' 기능을 수행하는 메서드로, 해당 객체가 갖고 있는 정보를 출력하거나 다른 객체와 상호작용할 수 있습니다.</li>
<li>자식 클래스에서 다시 정의한다면, 해당 자식 클래스에서는 원하는 대로 'speack' 기능을 구현할 수 있습니다.</li>
<li>부모 클래스에서 정의된 'speack' 기능을 유지하면서도, 자식 클래스에서 필요한 기능을 추가하거나 수정할 수 있습니다.</li>
</ul>
<pre><code>
class Animal():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(self.name + " is speaking")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def speak(self):
        print(self.name + "개 입니다.")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name,age)
        self.name = name
        self.age = age

    def speak(self):
        print(self.name + "고양이 입니다.")
</code></pre>
<br>
<h3 data-ke-size="size23">추상 클래스</h3>
<ul style="list-style-type: disc;" data-ke-list-type="disc">
<li>객체 지향 프로그래밍에서 중요한 개념 중 하나</li>
<li>구체적인 구현 없이 인터페이스만을 정의한 클래스를 의미</li>
<li>구현을 갖지 않는 메서드나 추상 메서드를 포함할 수 있습니다.</li>
<li>자식 클래스에서 구체적인 구현을 제공하기 위해 사용됩니다.</li>
</ul>
<p data-ke-size="size16">&nbsp;</p>
<h4 data-ke-size="size20">get_area(self)을 자식 클래스에서 구현</h4>
<ul style="list-style-type: circle;" data-ke-list-type="circle">
<li>추상 클래스 내부에 정의된 추상 메서드 중 하나로, 도형의 면적을 반환하는 기능을 수행</li>
<li>구현되어 있지 않으며, 추상 클래스를 상속받은 자식 클래스에서 구체적인 구현을 제공해야 합니다.</li>
<li>자식 클래스에서 구체적인 구현을 제공함으로써 코드의 재사용성과 유지보수성을 향상시킬 수 있습니다.</li>
</ul>
<pre id="code_1682686019408" class="python" data-ke-language="python" data-ke-type="codeblock"><code>class Shape():
    def get_area(self):
        pass
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height</code></pre>
