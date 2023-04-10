-- id, 이름, 직업, 능력, 국적, 소속회사, 나이, 가입날짜

-- sql문 작성시 주의사항
-- 세미콜론(;) 기준으로 하나의 SQL문을 판별

-- 새로운 테이블을 생성하기

-- 기본키 : 레코드를 판별(식별)하는 데 사용
-- 테이블당 하나만 존재가능, 중복x

CREATE TABLE superheroes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  이름 TEXT NOT NULL,
  직업 TEXT NOT NULL,
  능력 TEXT,
  국적 TEXT,
  소속회사 TEXT,
  나이 INTEGER
);

-- 테이블명 변경하기
ALTER TABLE superheroes RENAME TO superhero;

-- 새로운 컬럼 추가
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE;

-- 임시 컬럼 추가 후 이름 변경
ALTER TABLE superhero
ADD COLUMN 임시 TEXT;

ALTER TABLE superhero
RENAME COLUMN 임시 TO 곧삭제;

-- 컬럼 지우기
ALTER TABLE superhero
DROP COLUMN 곧삭제;

