# Qt Designer 파일 결과를 py로 변환하기>

- Qt Designer에서 저장한다. 그럼 .ui파일이 생성된다

- pyuic6을 이용해 다음과 같이 py 로 변환한다
	- pyuic6 -x qd_result.ui -o converted_py.py

# .ui파일을 읽기
- uic 모듈을 이용해서 ui파일을 읽는 식으로 ui를 설정할 수도 있다
