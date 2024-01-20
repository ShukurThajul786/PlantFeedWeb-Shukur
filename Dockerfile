FROM python:3.11.7

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container image
COPY . /app

# Create a virtual environment and activate it
RUN python -m venv venv
RUN . venv/bin/activate

# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which the Django development server will run
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]