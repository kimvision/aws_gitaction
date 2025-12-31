import streamlit as st

st.title(" EC2 Streamlit 배포 성공!")
st.write("GitHub Actions를 통해 자동 배포된 화면입니다.")
st.write("확인")

st.sidebar.header("설정")
name = st.text_input("이름을 입력하세요", "사용자")
st.success(f"{name}님, 환영합니다!")



# from flask import Flask

# # 서비스 파일의 app:app 중 뒤의 app이 바로 이 변수 이름입니다.
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return {
#         "status": "success",
#         "message": "Hello from EC2!",
#         "deploy": "GitHub Actions is working!"
#     }

# if __name__ == '__main__':
#     # 로컬 테스트용 (gunicorn 없이 실행할 때)
#     app.run(host='0.0.0.0', port=8000)
