# Step 1: Build the React application
FROM node:16 AS build

WORKDIR /app

# Copy the package.json and package-lock.json to install dependencies
COPY ./FE/package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend source code
COPY ./FE/ .

# Build the React app
RUN npm run build

# Step 2: Set up the production environment
FROM nginx:alpine

# Copy the build output from the build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port on which the app will run
EXPOSE 80
