

CREATE TABLE superhero (
  id INTEGER PRIMARY KEY,
  이름 TEXT NOT NULL,
  직업 TEXT,
  능력 TEXT,
  국적 TEXT,
  소속회사 TEXT,
  나이 INTEGER,
  가입날짜 DATE
);

-- power 테이블 생성
CREATE TABLE power (
  id INTEGER PRIMARY KEY,
  hero_id INTEGER,
  능력 TEXT,
  -- 외래키 등록 방법
  -- FOREIGN KEY (<필드명>) REFERENCES <테이블명>(<해달테이블PK>)
  -- 사실 지금은 hero 테이블이 없어서 아래 문장에 오류가 있음
  FOREIGN KEY (hero_id) REFERENCES hero(id)
)

-- job 테이블 생성
CREATE TABLE job (
  id INTEGER PRIMARY KEY,
  직업 TEXT
)

-- country 테이블 생성
CREATE TABLE country (
  id INTEGER PRIMARY KEY,
  국적 TEXT
)

-- company 테이블 생성
CREATE TABLE company (
  id INTEGER PRIMARY KEY,
  소속회사 TEXT
)


-- hero 테이블 생성
CREATE TABLE hero(
  id INTEGER PRIMARY KEY,
  이름 TEXT NOT NULL,
  나이 INTEGER,
  가입날짜 DATE,
  job_id INTEGER,
  country_id INTEGER,
  company_id INTEGER,
  FOREIGN KEY (job_id) REFERENCES job(id),
  FOREIGN KEY (country_id) REFERENCES country(id),
  FOREIGN KEY (company_id) REFERENCES company(id)
)

-- 기존 데이터를 새로운 테이블로 이동
-- 데이터 삽입
-- INSERT INTO 테이블(필드1,필드2...)
-- VALUES(필드1, 필드2 ...)

-- 직업 데이터 삽입하기
-- 기본키가 AUTOINCREMENT를 포함하므로
-- 직업데이터만 넣어주면 된다.
-- VALUES 대신 SELECT 로 기존 데이터를 가져옴
INSERT INTO job(직업)
SELECT DISTINCT 직업
FROM superhero;

INSERT INTO country(국적)
SELECT DISTINCT 국적
FROM superhero;

INSERT INTO company(소속회사)
SELECT DISTINCT 소속회사
FROM superhero;

INSERT INTO hero (id, 이름, 나이, 가입날짜,
                job_id, country_id, company_id)
SELECT sh.id, sh.이름, sh.나이, sh.가입날짜,
    CASE
        WHEN sh.직업 = '영웅' THEN 1 ELSE 2
    END AS job_id,
    CASE
        WHEN sh.국적 = '미국' THEN 1
        WHEN sh.국적 = '아스가르드' THEN 2
        WHEN sh.국적 = '러시아' THEN 3
        WHEN sh.국적 = '왜곡의 나라 와칸다' THEN 4
        WHEN sh.국적 = '아틀란티스' THEN 5
        WHEN sh.국적 = '아마조니아' THEN 6
        WHEN sh.국적 = '크립톤' THEN 7
        WHEN sh.국적 = '영국' THEN 8
        WHEN sh.국적 = '애포콜립스' THEN 9
        WHEN sh.국적 = '아즈라엘' THEN 10
        WHEN sh.국적 = '카하지아' THEN 11
        WHEN sh.국적 = '잉글랜드' THEN 12
        WHEN sh.국적 = '스페인' THEN 13
        WHEN sh.국적 = '독일' THEN 14
        WHEN sh.국적 = '캐나다' THEN 15
        WHEN sh.국적 = '완다' THEN 16
        WHEN sh.국적 = '그리스' THEN 17
        WHEN sh.국적 = '케냐' THEN 18
    END AS country_id,
    CASE
        WHEN sh.소속회사 = '마블' THEN 1
        WHEN sh.소속회사 = 'DC' THEN 2
        WHEN sh.소속회사 = '저스티스 리그' THEN 3
    END AS company_id
FROM superhero AS sh;
