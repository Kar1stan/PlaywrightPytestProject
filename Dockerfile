ARG NODE_VERSION=18

FROM node:${NODE_VERSION}

#Create the app directory
WORKDIR /dockerimage

#Install all dependencies
COPY Pipfile ./

#Run mpm install
RUN pipenv install 

#Bundle app source
COPY . .

# Expose the port that the application listens on.
EXPOSE 8040

# Run the application.
CMD ["pytest"]
