# Step 1: Use Node.js as the base image
FROM node:16 as build

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy package.json and package-lock.json files
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the entire frontend code
COPY . .

# Step 6: Build the Vite project
RUN npm run build

# Step 7: Use Nginx to serve the build files
FROM nginx:alpine

# Step 8: Copy the build files to Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Step 9: Expose port 80
EXPOSE 80
##k,k,k,

# Step 10: Start Nginx
CMD ["nginx", "-g", "daemon off;"]
