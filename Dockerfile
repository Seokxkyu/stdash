FROM python:3.11

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade git+https://github.com/Seokxkyu/stdash.git@0.1.1
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "src/stdash/app.py"]
