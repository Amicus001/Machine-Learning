## 모델을 활용한 서비스 제공
## ----------------------------------------------------------
## 모듈 임포트

from joblib import *

# 전역변수
mdfile = '../model/iris_dt.pkl'

# 모델 로드
md = load(mdfile)

#로딩된 모델 확인
print(md.classes_)

# 붓꽃 정보 입력 : 4개 feature
data = input('붓꽃의 꽃받침 길이, 너비, 꽃잎 길이, 너비 순)')

if len(data):
    datalist = list(map(float, data.split(',')))
    print(datalist)

    # 입력된 정보에 해당하는 품종 알려주기
    preiris = md.predict([datalist])
    prob = md.predict_proba([datalist])
    print(f'this is {preiris} by chance of {prob}.')
else:
    print('입력된 정보가 없음')
