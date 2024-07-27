FROM python:3.11-slim

RUN <<EOT
python -m pip install --upgrade build
EOT

WORKDIR /var/app/

COPY --link . .

CMD [ "bash" ]
