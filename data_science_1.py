import pandas as pd
import seaborn as sns

#seaborn으로 내장 되어 있는 mpg 데이터셋 불러오기 
#sns.load_dataset("mpg")
#print(sns.load_dataset("mpg"))

#pandas로 깃헙에서 csv파일 불러오기 재사용을 위해 변수로 저장
#csv를 읽어오는 과정에서 파일의 끝이 \n, \r등으로 끝나서 오류 발생 sep과 lineterminator로 오류 제거 
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")


print(df)

#행과 열 shape
print(df.shape)

#index 값만 보고 싶다 index
print(df.index)

#내가 값만 보고싶다 values
print(df.values)

#데이터의 타입만 보고싶다 dtypes
print(df.dtypes)

#head를 통해 일부만 가져오기 head의 default는 5이다
print(df.head())
print(df.head(20))

#tail을 통해 뒤에서부터 일부만 가져오기 tail의 default는 5이다
print(df.tail())
print(df.tail(2))

#sample을 통해 무작위로 일부만 가져오기 default는 1이다
#random_state라는 기능으로 무작위로 나오는 값을 고정시킬수 있는데 약간 난수의 개념 같다. 다시 실행시켜도 결과는 같음 
print(df.sample(2))
print(df.sample(2, random_state=42))


#info를 통해 요약정보 보기
df.info()


#결측치 수 확인 null로 저장된 값 확인인듯 insull, isna True가 결측치임
print(df.isnull())
print(df.isna())

#python에서는 True를 1, False를 0으로 계산한다(연산시) 이것을 이용해 결측치를 쉽게 확인할 수 있다. 
print(df.isnull().sum())

#결측치 비율 확인
print(df.isnull().mean())
#백분위 값
print(df.isnull().mean()*100)


#describe를 이용하여 기술통계 구하기 ex) std = standard division 표준편차
print(df.describe())

#describe는 수치값만 기술통계가 가능하다. string 형식의 데이터에 적용시키기 include이용
#unique는 중복 제거, top은 최빈값, freq은 top 해당 값의 빈도수
print(df.describe(include='object'))


#mpg column을 pandas의 series 형태, 벡터 형식으로 가져오기
print(df["mpg"])
#type으로 확인해보기 <class 'pandas.core.series.Series'>
print(type(df["mpg"]))


#일정 column만 series형태로 인덱싱
print(df["origin"])
print(df["name"])


#만약 여러개의 column을 가져오고 싶다 두 개이상의 열을 가져올 땐, list형식으로 묶어야한다. 안그러면 keyerror 발생
#묶어서 가져오게 되면 series가 아닌 dataframe형식으로 가져온다.
print(df[["name","origin"]])


#행 인덱싱 loc을 이용(locate)
print(df.loc[0])
#두 개 이상시 loc은 column 인덱싱과 같이 list 형식으로 가져와야한다. dataframe형식으로 나온다.
print(df.loc[[0,1]])


#loc으로 행과 열 둘 다 가져올 수 있다. 0의 name만 가져오기
print(df.loc[0,"name"])

# 여러개의 행과 열을 가져오기
print(df.loc[[0,1],["name","origin"]])
















