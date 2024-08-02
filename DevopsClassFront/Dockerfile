FROM httpd:latest

COPY ./dist/ /usr/local/apache2/htdocs/

#Install npm
RUN curl -fsSL https://fnm.vercel.app/install | bash 
RUN source ~/.bashrc
RUN fnm use --install-if-missing 20

# Add in the Contrast agent
RUN npm install --production @contrast/agent

# Change the startup command to preload Contrast agent
CMD ["node", "-r", "@contrast/agent", "build/app"]
