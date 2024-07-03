ARG NODE_VERSION=18

FROM node:${NODE_VERSION}

#Create the app directory
WORKDIR /dockerimage

#Install all dependencies
COPY package.json ./

#Run mpm install
RUN npm install 

#Bundle app source
COPY . .

# Expose the port that the application listens on.
EXPOSE 8040

# Run the application.
CMD ["Url=PROD_UR","npm","run","testchrome"]
