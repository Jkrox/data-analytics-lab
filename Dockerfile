FROM python:3.10.13-alpine3.18

# Set environment variables
ENV PYTHONUNBUFFERED True

ENV APP_HOME /application

# Set the working directory in the container
WORKDIR $APP_HOME

# Copy only requirements to leverage Docker cache
COPY requirements.txt $APP_HOME/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY . ${APP_HOME}

# Expose the port
EXPOSE 8000

CMD ["streamlit", "run", "src/streamlit_app.py"]