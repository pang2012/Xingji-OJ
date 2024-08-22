# Python runtime
FROM python:3.8-slim
 
# Install pip and any additional needed packages
RUN apt-get update && apt-get install -y --no-install-recommends python-pip gcc libpq-dev python-dev
 
# Copy the current directory's contents into the container at /app
ADD . /app
 
# Change directory so that our commands run in that directory
WORKDIR /app
 
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
 
# Make port 80 available to the world outside this container
EXPOSE 80
 
# Define environment variable
ENV PORT 80
 
# Run app.py when the container launches
CMD ["python", "index.py"]
