FROM node:18-bullseye
WORKDIR /DevopsTestPipeline
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 5000
CMD python main.py