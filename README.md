## 프로젝트 소개

KMU의 가상 퀴즈 웹서비스 프로젝트입니다.

## 실행 방법

1. 프로젝트 클론하기:

   ```
   git clone https://github.com/dandacompany/kmu_quiz.git
   cd kmu_quiz
   ```

2. 가상환경 설치 (conda 사용)

   ```
   conda create --prefix ./.conda python=3.12
   conda activate ./.conda
   ```

3. 필요한 패키지 설치:

   ```
   pip install -r requirements.txt
   ```

3. 애플리케이션 실행:

   ```
   python manage.py runserver
   ```

4. 웹 브라우저에서 다음 주소로 접속:

   ```
   http://localhost:8000
   ```

5. 퀴즈 데이터 추가:

   ```
   - dataset 폴더에 json 파일을 생성합니다.

   - json 파일은 다음과 같은 형식으로 작성합니다.

   ```

   {
       "title": "퀴즈 제목",
       "description": "퀴즈 설명",
       "questions": [
           {
               "content": "퀴즈 내용",

               "selections": [
                   {
                       "content": "선택지 내용",
                       "is_correct": true,
                       "index": 1
                   },
                   {
                       "content": "선택지 내용",
                       "is_correct": false,
                       "index": 2
                   },
                   {
                       "content": "선택지 내용",
                       "is_correct": false,
                       "index": 3
                   },
                   {
                       "content": "선택지 내용",
                       "is_correct": false,
                       "index": 4
                   }
               ]
           },
           ...
       ]
   }

   ```

   - 프로젝트 루트 폴더에 있는 data-generating.py 파일을 실행합니다.

   ```

   python data-generating.py

   ```

   - 퀴즈 데이터가 추가됩니다.
