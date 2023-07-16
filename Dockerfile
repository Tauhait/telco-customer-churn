# Specifies the base image
FROM python:3.9
# Sets a special Python settings for being able to see logs
ENV PYTHONUNBUFFERED=TRUE
# Installs Pipenv
RUN pip --no-cache-dir install pipenv
# Sets the working directory to /app
WORKDIR /app
#  Copies the Pipenv files
COPY ["Pipfile", "Pipfile.lock", "./"]
# Installs the dependencies from the Pipenv files
# Inside Docker, we don’t need to create a virtual
# environment — our Docker container is already isolated from the rest of the system.
# Setting  --deploy and --system parameters allows us to skip creating a virtual environment and use the system Python for installing all the dependencies.
# After installing the libraries, we clean the cache to make sure our Docker image doesn’t grow too big.
RUN pipenv install --deploy --system && \
 rm -rf /root/.cache
# Copies our code as well as the model
COPY ["/code/*.py", "/code/churn-model.bin", "./"]
# Opens the port that our web service uses
EXPOSE 9696
# Specifies how the service should be started
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"] 
