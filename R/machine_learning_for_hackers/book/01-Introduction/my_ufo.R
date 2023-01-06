# R은 1-based index이다!!!!

# r에서 source("script_name.R") 하면 script를 실행할 수 있다
# 이렇게 실행하는게 rscript에서 실행하는것 보다 나을 수 있다. 
# 패키지 설치같은건 rscript에서 뭔가 잘 안되서...

# library 는 해당 라이브러리를 로드하겠다는 뜻이다

library(ggplot2)    # We'll use ggplot2 for all of our visualizations
library(plyr)       # For data manipulation
library(scales)     # We'll need to fix date formats in plots

print("Loading data...")

# dataframe을 리턴한다
# dataframe 2D table 인데 matrix는 모든 element가 같은 type이어야 하는 반면
# datafrmae은 같은 column에 있는 것들이 같은 type이기만 하면 된다
# 즉 다른 column이면 다른 type이어도 상관 없다
ufo<-read.delim(file.path("data", "ufo", "ufo_awesome.tsv"),
     sep = "\t", 
     stringsAsFactors = FALSE, 
     header = FALSE, 
     na.strings="")
print("")

# sprintf는 string format 하는 함수. 즉 string을 리턴한다
# print 자체는 기능이 굉장히 제한적이다... 애초에 R이 언어인지 조차 좀 헷갈린다
print(sprintf("ufo data number of rows    = %s", nrow(ufo)))
print(sprintf("ufo data number of columns = %s", ncol(ufo)))
print("")

# 첫 6줄을 출력해 준다
print('First 6 rows of data (before)')
print(head(ufo))
print("")

# Column의 이름을 출력해 준다
print('Initial column names')
print(names(ufo))
print("")

# Column 이름을 다음과 같이 변경해 줄 수 있음
# 여기에서 c는 R vector를 만드는데 쓰인다. 근데 왜 c? 왜 v나 vector가 아닌걸까...
# 그리고 names(ufo)는 함수가 아니라 다른 OOP language의 ufo.names 의 의미에 가까운 것인듯
# 이런게 R의 특징인가...
names(ufo) <- c("DateOccurred", "DateReported",
                "Location", "ShortDescription",
                "Duration", "LongDescription")

# 적용된 column 이름을 찍어본다
print('Column names after change')
print(names(ufo))
print("")

print('First 6 rows of data (after)')
print(head(ufo))
print("")

#
# 주어진 자료는 데이터 필터링 예시를 위해 일부 날짜가 잘못 들어가 있다
# 여기에서 필터링은 날짜가 8글자로 딱 떨어지는지 여부를 체크하는 걸로 한다
# 여기에서 good.rows는 good이 object고 rows가 member인게 **아니다**
# R에서 Variable 이름은 점(.)을 포함할 수 있다! 그러니까 good.rows **전체**가
# variable 이름인 것이다
#
# column 이름을 위와 같이 정해뒀다면 $ operator를 통해서 그 column을 vector처럼 접근할 수 있다
# ifelse는 이렇게 vector를 받아 그 전체에 대해 boolean operation을 한 결과를 vector로 리턴한다
# 
good.rows <- ifelse(nchar(ufo$DateOccurred) != 8 |
                    nchar(ufo$DateReported) != 8,
                    FALSE,
                    TRUE)

# 위에서 FALSE를 리턴한 것의 row count를 찍어준다
# !good.rows하면 boolean vector가 반전되는것 같다
# which는 TRUE인 것의 index들을 가져온다. 왜 이런게 있는거지? 그리고 여기서는 함수처럼 생겼네
# R은 참 생긴게 원칙 없이 만들은 언어 같다...
# length는 vector의 length를 리턴한다 (vector.length() 같은 느낌)
print(sprintf("Invalid date row count : %s", length(which(!good.rows))))
print("")

# 위에서 만든 ufo.rows로 filtering할 수 있다
# 원래 ufo[1,] 이런식으로 하면 1번째 row를 리턴하고
# ufo[,1] 이런식으로 하면 1번째 column을 리턴한다 (0-based가 아니라 1-based index다!)
# 그리고 a = c(1,2,3) 이고 ufo[a,] 이런식으로 주면 1,2,3번째 row가 리턴된다
# 뭐 이런식으로 row와 같은 사이즈의 logical(boolean) vector가 row 지정자로 주어지면
# 그 중 TRUE인것만 필터링 해 주는 건가...보다... (이 부분이 뭔가 명확하게 잘 안나와 있다)
filtered_ufo <- ufo[good.rows, ]

print(sprintf("row count before filtering: %s", nrow(ufo)))
print(sprintf("row count after filtering:  %s", nrow(filtered_ufo)))

# as.Date는 character string을 Date구조체로 변경해 준다
filtered_ufo$DateOccurred <- as.Date(filtered_ufo$DateOccurred, format = "%Y%m%d")
filtered_ufo$DateReported <- as.Date(filtered_ufo$DateReported, format = "%Y%m%d")

# R 에서 함수 정의는 다음과 같이 할 수 있다
# tryCatch 같은걸 보면 R은 죄다 vector단위로 적용하는데 특화 되어 있다는걸 알 수 있다
# gsub은 regular expression 적용 (맨 앞의 공백 제거)
# split했는데 2개 이상의 element가 나오면 걍 NA,NA 를 리턴

# 저기에서 [[1]] 이 도대체 뭐하는 건가 하고 의문이 바로 드는데
# [[1]] 은 1번째 column을 **element**로써 리턴해라 라는 뜻이다
# [1]을 써도 1번째 column을 리턴하는건데 이 경우는 Vector로 리턴하게 된다
# 이 두개가 gsub으로 가면 서로 취급 되는게 다르다!
# [[1]] 을 쓴것은 "aaa" "bbb" 이런 식이고
# [1] 을 쓴것은 c("aaa","bbb") 이런 식이다
# 근데 웃기는건 gsub은 [1]로 리턴받은걸 "c(\"aaa\",\"bbb\")" 이런식으로 처리해서
# gsub이 제대로 안된다
# [[1]]로 리턴받은건 잘 된다
# 왜 R은 이딴 식인건가? 보면 볼수록 화가 난다
get.location <- function(l)
{
  split.location <- tryCatch(strsplit(l, ",")[[1]],
                             error = function(e) return(c(NA, NA)))
  clean.location <- gsub("^ ","",split.location)
  if (length(clean.location) > 2)
  {
    return(c(NA,NA))
  }
  else
  {
    return(clean.location)
  }
}

# 위에서 적용한 함수를 row-by-row로 적용한다
# lapply는 list-apply의 준말이다
city.state <- lapply(filtered_ufo$Location, get.location)

print(head(city.state))