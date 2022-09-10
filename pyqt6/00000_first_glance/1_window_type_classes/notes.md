# Qt Window type classes
- QMainWindow
    - Default layout이 처음부터 존재함
        - 예: statusBar, menuBar 같은거

- QDialog
    - Short term task / brief communication에 유리
    - 그냥 간단한 메시지나 보여주거나 간단한 인풋 받는 정도로 쓰기 좋다 정도인듯
    - 그냥 이렇게 쓰기 만만한 템플릿으로 만들어 둔건가 봄

- QWidget
    - 설명에 따르면 QWidget이 모든 Window의 base class가 된다. 사실 고급 개발을 할거면 QWidget에서 시작해야 할 것 같다