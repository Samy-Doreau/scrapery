FROM python:3.11-slim

WORKDIR /usr/src/app

COPY ../requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code for runtime inside container (mounted at runtime via compose too)
COPY ../src ./src

ENV PYTHONPATH=/usr/src/app/src
CMD ["bash"] 