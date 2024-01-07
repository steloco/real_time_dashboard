A simple tutorial real-time dashboard using Kafka and Pinot.

To Run

Set-up env:
```
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Set-up infra:
```
docker-compose up -d
```

Create Pinot table:
```
docker exec -it pinot-controller-wiki bin/pinot-admin.sh AddTable \
    -tableConfigFile /config/table.json \
    -schemaFile /config/schema.json \
    -exec
```


Start fake events producer:
```
python producer.py
```

Start dashboard:
```
streamlit run streamlit/app.py
```

Navigate to localhost:8501 to view dashboard. Navigate to localhost:9001 to view Pinot controller.

