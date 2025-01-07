import streamlit as st
import os

# (화자)(감정)자막 폴더 경로 설정
COMPLETED_FOLDER = "(화자)(감정)자막"

# 스트림릿 제목 설정
st.title("동영상 자동 매칭 인터페이스")

# 원본 동영상 업로드
uploaded_file = st.file_uploader("원본 동영상을 업로드하세요.", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # 업로드된 동영상의 파일명 추출
    uploaded_filename = uploaded_file.name
    base_filename = os.path.splitext(uploaded_filename)[0]  # 확장자 제거한 파일명
    
    # 완성된 동영상 경로 설정
    completed_video_path = os.path.join(COMPLETED_FOLDER, f"{base_filename}.mp4")
    
    # 완성본 확인
    if os.path.exists(completed_video_path):
        st.success("완성된 동영상을 찾았습니다!")
        st.video(completed_video_path)
    else:
        st.error("완성된 동영상을 찾을 수 없습니다.")
