# Use the official Node.js image as the base image
FROM node:latest

# Install Apache HTTP Server
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your application files to the container
# Assuming your application files are in the 'app' directory
COPY ./dist /var/www/html

# Add in the Contrast agent
RUN npm install --production @contrast/agent

# Expose port 80 to the outside world
EXPOSE 80

# Start Apache in the foreground and startup command to preload Contrast agent
CMD ["apachectl", "-D", "FOREGROUND", "node", "-r", "@contrast/agent", "build/app"]

