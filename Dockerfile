# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Expose a port (optional, if the application serves on a specific port)
# EXPOSE 5000  # Uncomment if you're creating a web API later (e.g., Flask)

# Command to run the main Python script
CMD ["python", "src/diabetes_model.py"]
