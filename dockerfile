# Use the base image with Python 3
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire 'utils' directory into the container
COPY utils /app/utils

# Copy all other files from the current directory into the container
COPY . .

# Expose the port the application will run on
EXPOSE 80

# Define the command to run the application
CMD ["python", "app.py"]
