FROM node:16

WORKDIR /app
COPY signaling-server.js package.json ./
RUN npm install

CMD ["node", "signaling-server.js"]