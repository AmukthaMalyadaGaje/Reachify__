# Step 1: Use Node.js image to build the frontend
FROM node:16 AS build

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json (if exists)
COPY ./fe/package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the entire frontend code
COPY ./FE/ .

# Step 6: Build the Vite project
RUN npm run build

# Step 7: Use NGINX to serve the frontend files
FROM nginx:alpine

# Step 8: Copy the built frontend files from the build container
COPY --from=build /app/dist /usr/share/nginx/html

# Step 9: Expose the port that NGINX will use
EXPOSE 80

# Step 10: Start NGINX to serve the frontend
CMD ["nginx", "-g", "daemon off;"]
