FROM oven/bun:latest
# Installing libvips-dev for sharp Compatability

# where our Strapi app will live
RUN mkdir -p /app

# Set /app as the working directory
WORKDIR /app

# Copy package.json and package-lock.json
# to the /app working directory
COPY ./package*.json ./bun.lockb /app/


COPY ./.env /app/

ENV PATH /app/node_modules/.bin:$PATH

# Install dependencies in /app
RUN bun i

# Copy the rest of our Strapi folder into /app
COPY ./backend /app

EXPOSE 1337

# Build Strapi admin
RUN bun build

# Run yarn dev, as we would via the command line
CMD ["bun", "start"]
