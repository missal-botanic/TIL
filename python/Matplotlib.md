pip install matplotlib

import matplotlib.pyplot as plt


### 라인 플롯 그리기
plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])

plt.show()


<p><img alt="" src="https://rr720.synology.me/data/matplotlib1.png"></p>


### 축 레이블 삽입하기

plt.title('test')
plt.plot([1,2,3,4],[2,4,8,6])
plt.xlabel('hours')
plt.ylabel('score')

<p><img alt="" src="https://rr720.synology.me/data/matplotlib2.png"></p>

### 라인 추가와 범례 삽입하기

plt.title('students')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student']) # 범례 삽입
plt.show()

<p><img alt="" src="https://rr720.synology.me/data/matplotlib3.png"></p>
