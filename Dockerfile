# select default OS image
FROM alpine


# #  tell what you want to do
RUN apk add py3-pip
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# # Configure a software
# # Defining working directory
WORKDIR ./

# # Copy everything which is present in my docker directory to working (/app)
COPY /requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ["__init__.py","MongoAPI.py","Config.ini", "./"]

# Exposing an internal port
EXPOSE 5001


# set default commands
# These are permanent commands i.e even if user will provide come commands those will be considered as argunemts of this command
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD ["__init__.py"]
