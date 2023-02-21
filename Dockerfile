# select default OS image
FROM python:3.10


# #  tell what you want to do
#RUN apk add py3-pip
#RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# # Configure a software
# # Defining working directory
#WORKDIR /

# # Copy everything which is present in my docker directory to working (/app)
COPY /requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ["main.py","MongoAPI.py","Config.ini", "./"]

# Exposing an internal port
EXPOSE 8000


# set default commands
# These are permanent commands i.e even if user will provide come commands those will be considered as argunemts of this command
#ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
#CMD ["main.py"]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
