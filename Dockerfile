# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /django_map
WORKDIR /django_map

# Copy the current directory contents into the container at /django_map
COPY requirements.txt /django_map/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /django_map
COPY . /django_map/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "django_map/manage.py", "runserver", "0.0.0.0:8000"]
