FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*


ENV PATH="/usr/games:/usr/local/games:${PATH}"

WORKDIR /app

# Copy script
COPY wisecow.sh .

RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["bash", "wisecow.sh"]
