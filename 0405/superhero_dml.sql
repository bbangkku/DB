-- 전체조회
-- SELECT <원하는 필드> FROM <테이블>
SELECT * FROM superhero;

-- 특정필드조회
SELECT 이름 FROM superhero;
SELECT 이름,소속회사 FROM superhero;

-- 없는 필드 : no such column 이라는 에러
SELECT 없는필드 FROM superhero;

-- 별칭 지어주기
SELECT 이름 AS 활동명
FROM superhero;

-- 콤마로 구분 지어서 여러 개 별칭 짓기
SELECT 이름 AS 활동명, 소속회사 AS 팀
FROM superhero;

-- 나이가 적은순으로 정렬하여 출력
SELECT * FROM superhero
ORDER BY 나이;

-- 나이가 많은순으로 조회하기(내림차순)
SELECT * FROM superhero
ORDER BY 나이 DESC;

-- 중복 제거하기
SELECT DISTINCT 소속회사 from superhero;

-- 여러 필드를 사용하면, 모두 동일한 데이터를 삭제
SELECT DISTINCT 나이,소속회사 FROM superhero;

-- 나이 , 소속회사가 겹치지 않는 사람들 중
-- 소속회사, 나이 순으로 정렬

SELECT DISTINCT 나이,소속회사
FROM superhero
ORDER BY 소속회사,나이 ;

-- 여러 필드로 정렬하기
-- 소속회사 별로 나이가 많은 순으로 조회하기
SELECT DISTINCT 나이
FROM superhero
GROUP BY 소속회사
ORDER BY 나이 DESC

-- 조건문
-- 직업이 악당인 사람들만 조회
SELECT * FROM superhero
WHERE 직업 = '악당';

-- 비교연산자 사용하기
-- 나이가 50살이 넘는 사람들만 조회
SELECT * FROM superhero
WHERE 나이 > 50;

-- 가입날짜가 2000년 1월 1일
-- 이전인 사람 조회(DATE 필드)

SELECT * FROM superhero
WHERE 가입날짜 < DATE('2000-01-01')

-- 소속회사가 마블 소속인 영웅만 조회
SELECT * FOR superhero
WHERE 소속회사 = '마블' 
  AND 직업 = '영웅';

-- 국적이 미국이거나 러시아인 사람들만 조회
SELECT * FROM superhero
WHERE 국적='미국' OR 국적 = '러시아';

--1. % : 글자수 제한 없이 패턴을 만족하면 조회
SELECT * FROM superhero
LIKE '%맨';

-- 2. _ : 개수 만큼 글자 수 제한하여 패턴 만족하면 조회
-- 이름 두글자인 사람 조회
SELECT * FROM superhero
LIMIT '__';

-- 특정 데이터에 포함여부(IN)
-- 마블, DC 소속의 사람들을 조회
SELECT * FROM superhero
WHERE 소속회사 IN('마블','DC')

-- between and

-- 원하는 행 개수만큼만 조회 (LIMIT)
SELECT * FROM superhero LIMIT 1;

-- 나이가 가장 적은사람 1명
SELECT * FROM superhero;
ORDER BY 나이 LIMIT 1

-- 소속회사가 마블인 사람 중 나이가 가장 적은 1명
SELECT * FROM superhero ;
WHERE 소속회사 = '마블'
ORDER BY 나이 LIMIT 1 

-- 나이가 많은 10명
SELECT * FROM superhero ;
ORDER BY 나이 DESC LIMIT 10


-- N번째 데이터부터 조회 - 기준점을 변경(OFFSET)
-- 나이가 10번쨰로 많은 사람
SELECT * FROM superhero ;
ORDER BY 나이 DESC
LIMIT 1 OFFSET 9;
-- 검색 기준점 : OFFSET + 1 부터
-- 10번째 데이터부터 조회를 작해서
-- LIMIT 1 이기 때문에 -> 10번째 데이터를 반환
-- OFFSET10이면 11번째부터잡는다는듯

-- 전체 데이터 수를 구하여라
SELECT COUNT(*) AS COUNT
FROM superhero;

SELECT * AVG(나이) AS 평균나이
FROM superhero ;


SELECT 소속회사, AVG(나이) AS 평균나이
 FROM superhero 
 WHERE 소속회사 = '마블'

-- 그룹별계싼
-- 각 소속회사의 평균 나이를 구하여라
SELECT 소속회사, AVG(나이) AS 평균나이
 FROM superhero
 GROUP BY 소속회사;

