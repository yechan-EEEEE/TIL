# 📚Django N:M 관계

## **1. N:M 관계가 필요한 이유 (왜 중개 모델이 생길까요?)**

N:M 관계란, 서로 다른 두 모델(테이블)이 **서로에게 다수(N)로 연결될 수 있는** 관계를 말합니다.

**예시: 의사와 환자의 예약 시스템**

* **1명의 의사**는 **여러 명의 환자**를 진료할 수 있습니다.  
* **1명의 환자**는 **여러 명의 의사**에게 예약할 수 있습니다.

이처럼 의사(Doctor)와 환자(Patient) 모델을 직접 연결하려고 하면, **데이터베이스에 무한한 연결 고리**가 생기게 됩니다. 데이터베이스는 이런 복잡한 연결을 직접 처리할 수 없으므로, 두 모델 사이에 **'중개자'** 가 필요합니다.

## **2. 중개 모델(Through Model)을 이용한 N:M 관계 구현**

### **2-1. N:1 관계의 한계 (N:M을 직접 연결하면 생기는 문제)**

만약 N:M 관계를 만들기 위해 두 모델을 N:1 관계로 만들면 어떻게 될까요?

**예시: N:1 관계 설정 (실패 사례)**

* **환자 테이블 (Patient)** 에 **담당 의사 ID (Doctor_id)** 를 추가 (N:1)  
  * Patient1은 Doctor_A에게만 예약 가능 (한 명의 의사에게만 연결 가능) -> 환자가 여러 의사에게 예약할 수 없으므로 N:M 관계를 충족 못함.  
* **의사 테이블 (Doctor)** 에 **환자 ID (Patient_id)** 를 추가 (N:1)  
  * Doctor_A는 Patient_1에게만 예약 가능 -> 의사가 여러 환자를 진료할 수 없으므로 N:M 관계를 충족 못함.

이처럼 N:1 구조로는 N:M 관계를 만들 수 없으며, 예약 시간, 진료 기록 등 **'연결 자체'에 대한 정보**를 저장할 공간도 없습니다.

### **2-2. 중개 모델의 등장 (예약 테이블)**

Django는 이 문제를 해결하기 위해 **'중개 모델(Through Model)'** 을 사용합니다. 이는 두 모델을 연결해주는 **별도의 테이블(모델)** 을 생성하는 방식입니다.

* **중개 모델 역할:** 의사와 환자의 '예약(Reservation)'이라는 행위 자체를 하나의 모델로 만듭니다.  
* **구성:** 이 모델은 의사 모델에 대한 N:1 관계(FK)와 환자 모델에 대한 N:1 관계(FK)를 가집니다.

**코드 예시 (models.py):**
```
# 1. 의사 모델 (Doctor)  
class Doctor(models.Model):  
    name = models.TextField()

# 2. 환자 모델 (Patient)  
class Patient(models.Model):  
    name = models.TextField()

# 3. 중개 모델 (Reservation) - 핵심!  
class Reservation(models.Model):  
    # 의사 FK: 한 명의 의사는 여러 개의 예약을 가질 수 있음  
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    # 환자 FK: 한 명의 환자는 여러 개의 예약을 가질 수 있음  
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    # 예약 시점, 증상 등 연결에 대한 추가 정보  
    reserved_at = models.DateTimeField(auto_now_add=True)  
    symptom = models.TextField()

    def __str__(self):  
        # 예시: 1번 의사에게 예약한 1번 환자  
        return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'
```
이렇게 하면, '예약(Reservation)' 모델을 통해 의사와 환자가 **다 대 다**로 연결되며, 예약 시간이나 증상 등 **연결에 대한 세부 정보**까지 깔끔하게 저장할 수 있습니다.

## **3. Django의 ManyToManyField 사용 (더 쉽게 N:M 구현)**

중개 모델을 직접 만드는 것이 기본 원리이지만, Django는 이를 더 편리하게 구현할 수 있도록 ManyToManyField를 제공합니다.

### **3-1. ManyToManyField의 정의**

ManyToManyField는 N:M 관계를 선언하는 필드입니다.

* **특징:** 이 필드를 모델에 추가하면, Django가 내부적으로 **별도의 중개 테이블(모델)**을 자동으로 생성하여 관리해 줍니다. 개발자가 직접 중개 모델을 만들 필요가 없습니다.  
* **사용법:** 두 모델 중 **어느 한쪽에만** 필드를 정의해도 양방향 관계가 자동으로 설정됩니다.

**코드 예시 (models.py):**
```
# Article 모델 (게시글)  
class Article(models.Model):  
    title = models.CharField(max_length=100)  
    content = models.TextField()  
    # '좋아요' 기능 구현 시: Article과 User를 N:M 관계로 연결  
    # 이 필드를 추가하면 Django가 'article_likes'와 같은 중개 테이블을 자동으로 생성함  
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL)

# User 모델 (사용자) - 별도 정의 불필요  
# likes 필드를 통해 User는 Article과 N:M 관계를 맺음
```
### **3-2. ManyToManyField의 조작 메서드**

ManyToManyField로 관계를 설정하면, 연결된 인스턴스에 접근하고 조작할 수 있는 편리한 메서드들이 자동으로 생성됩니다.

| 메서드 | 역할 | 예시 |
| :---- | :---- | :---- |
| **.add()** | 관계 추가 (중개 테이블에 데이터 삽입) | article.likes.add(user1) |
| **.remove()** | 관계 삭제 (중개 테이블에서 데이터 삭제) | article.likes.remove(user1) |
| **.clear()** | 모든 관계 삭제 | article.likes.clear() |
| **.all()** | 연결된 모든 인스턴스 조회 | article.likes.all() |

## **4. 'through' argument: 중개 모델에 추가 정보가 필요할 때**

### **4-1. 'through'를 사용하는 경우**

위의 ManyToManyField 방식은 연결에 대한 **추가 정보(예: 예약 시간, 증상 등)**를 저장할 필요가 없을 때 사용합니다.

하지만 만약 **'예약'처럼 연결 자체에 필요한 필드**가 있다면, 우리는 2번에서 했던 것처럼 **중개 모델을 직접 만들고** ManyToManyField에 through 인자를 사용해 그 중개 모델을 명시해 줘야 합니다.

**예시: Reservation 중개 모델을 명시하는 Doctor 모델**
```
# Reservation 모델은 위 2-2와 동일하게 직접 정의  
class Reservation(models.Model):  
    # ... Doctor FK, Patient FK, symptom 필드 등 ...  
    pass

# Doctor 모델 (의사)  
class Doctor(models.Model):  
    name = models.TextField()  
    # 환자(Patient)와의 N:M 관계를 'Reservation' 모델을 통해 설정  
    patients = models.ManyToManyField(Patient, through='Reservation')  
    # ManyToManyField에 through='중개모델명'을 명시

# Patient 모델 (환자)  
class Patient(models.Model):  
    name = models.TextField()  
    # 의사(Doctor)와의 N:M 관계를 'Reservation' 모델을 통해 설정  
    doctors = models.ManyToManyField(Doctor, through='Reservation')
```
### **4-2. 'through'를 사용할 때의 .add(), .remove()**

through를 사용하면, 관계를 추가/삭제할 때 중개 모델의 인스턴스를 직접 다루거나, 중개 모델의 필드에 대한 추가 정보를 전달해야 합니다.

* **.add() 시 추가 데이터 전달:**  
  * 중개 모델이 symptom 필드를 가진 경우, add() 메서드에 해당 데이터를 전달해야 합니다.
```
doctor.patients.add(patient, through_defaults={'symptom': '두통'})
```
* **.remove()는 동일:**  
  * remove()는 중개 테이블에서 관계만 끊으므로 인스턴스만 전달합니다.
```
doctor.patients.remove(patient)
```
## **5. Reverse Access Name (역참조 이름) 충돌 해결: related_name**

### **5-1. 역참조란?**

Django에서 N:1 또는 N:M 관계를 설정하면, 반대편 모델에서 현재 모델을 참조할 수 있는 필드(역참조 필드)가 자동으로 생성됩니다.

**예시:**
```
# Article 모델에 likes = ManyToManyField(User)가 있을 때  
user = User.objects.get(id=1)  
# user.article_set.all() 을 통해 이 user가 '좋아요' 한 모든 Article을 가져올 수 있습니다.
```
여기서 article_set이 역참조 이름입니다.

### **5-2. related_name 사용 이유 (충돌 방지)**

만약 **하나의 모델**이 **다른 하나의 모델**을 여러 번 참조하는 경우, 기본 역참조 이름(모델명_set)이 충돌하게 됩니다.

**예시: 게시글(Article) 모델이 사용자(User)를 두 번 참조하는 경우**

1. user = models.ForeignKey(AUTH_USER_MODEL): 게시글 작성자  
2. likes = models.ManyToManyField(AUTH_USER_MODEL): 좋아요 누른 사용자

이 경우, 두 관계 모두 기본 역참조 이름은 user_set이 되어 충돌합니다.

이때 **related_name**을 사용하여 충돌을 방지하고, 직관적인 이름으로 역참조 이름을 바꿔줍니다.

**코드 예시 (models.py):**
```
class Article(models.Model):  
    # 1. 작성자 (N:1 관계)  
    # 역참조 이름이 'article_set'이 아닌 'written_articles'가 됨  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='written_articles')

    # 2. 좋아요 (N:M 관계)  
    # 역참조 이름이 'article_set'이 아닌 'liked_articles'가 됨  
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles')

# 사용 예시:  
# user1이 작성한 모든 글: user1.written_articles.all()  
# user1이 좋아요 누른 모든 글: user1.liked_articles.all()
```
related_name은 역참조 시에 사용되는 '관리자 이름(Manager Name)'을 변경하는 핵심적인 인자입니다.

## **6. 핵심 요약 및 마무리**

| 개념 | 설명 | 언제 사용? |
| :---- | :---- | :---- |
| **중개 모델** | N:M 관계를 풀어서 N:1 + N:1로 만드는 별도의 테이블. | 관계 자체에 시간, 내용 등 **추가 데이터**를 저장해야 할 때. |
| **ManyToManyField** | Django가 자동으로 중개 모델을 생성하여 N:M 관계를 설정해주는 편리한 필드. | 관계에 대한 **추가 정보 없이** 단순히 연결만 필요할 때 (예: 좋아요 기능, 태그 기능). |
| **through 인자** | ManyToManyField에 직접 만든 중개 모델을 명시하여, Django에게 "이 모델을 중개자로 사용해!"라고 알려주는 설정. | ManyToManyField를 사용하고 싶지만, 관계에 대한 **추가 데이터**도 저장해야 할 때. |
| **related_name** | 역참조(반대편에서 참조)할 때 사용하는 이름을 변경하는 인자. | 하나의 모델이 다른 모델을 여러 번 참조하여 **역참조 이름 충돌**이 발생할 때. |

