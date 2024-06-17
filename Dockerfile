# Use the official Python image as base
FROM python:3.10

# Установка русской локали
#RUN apt-get update && apt-get install -y locales && \
#    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
#    locale-gen

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the Python script
CMD ["python", "bot/main.py"]
