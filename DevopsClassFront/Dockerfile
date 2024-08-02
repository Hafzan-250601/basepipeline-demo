# Use the official Node.js image as the base image
FROM node:latest

# Install Apache HTTP Server
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

COPY contrast_security.yaml /app/contrast_security.yaml

# Copy package.json and package-lock.json
COPY package*.json ./

# Clear npm cache and install Node.js dependencies
RUN npm cache clean --force && npm install --omit=dev @contrast/agent

# Copy your application files to the container
# Assuming your application files are in the 'app' directory
COPY ./dist /var/www/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Apache in the foreground and startup command to preload Contrast agent
CMD ["apachectl", "-D", "FOREGROUND", "node", "-r", "@contrast/agent", "build/app"]

