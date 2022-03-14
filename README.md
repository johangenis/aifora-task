# Aifora take-home task.

1. Write a Python Rest-Service which takes input requests of the form "test\_request.json":

`{`
`    "groups": [`
`        {`
`            "groupKey": "option1",`
`            "sourceLocations": [`
`                {`
`                    "locationKey": "wh1",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "maxQuantity": 12`
`                        }`
`                    ]`
`                }`
`            ],`
`            "sinkLocations": [`
`                {`
`                    "locationKey": "loc1",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 1,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                },`
`                {`
`                    "locationKey": "loc2",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 2,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                },`
`                {`
`                    "locationKey": "loc3",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 3,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                }`
`            ]`
`        }`
`    ]`
`}`

And yields responses of the form "test\_response.json":

`{`
`  "groups": [`
`    {`
`      "groupKey": "option1",`
`      "movements": [`
`        {`
`          "allocationQuantity": 1,`
`          "sinkLocationKey": "loc1",`
`          "skuKey": "sku1",`
`          "sourceLocationKey": "wh1"`
`        },`
`        {`
`          "allocationQuantity": 2,`
`          "sinkLocationKey": "loc2",`
`          "skuKey": "sku1",`
`          "sourceLocationKey": "wh1"`
`        },`
`        {`
`          "allocationQuantity": 3,`
`          "sinkLocationKey": "loc3",`
`          "skuKey": "sku1",`
`          "sourceLocationKey": "wh1"`
`        },`
`        {`
`          "allocationQuantity": 6,`
`          "sinkLocationKey": "wh1",`
`          "skuKey": "sku1",`
`          "sourceLocationKey": "wh1"`
`        }`
`      ]`
`    }`
`  ]`
`}`

Provide a suitable way to start the service locally.

The task is succesfully completed if the provided curl request:

`curl -X 'POST' \`
`  '`[`http://127.0.0.1:8000/optimize`](http://127.0.0.1:8000/optimize)`' \`
`  -H 'accept: application/json' \`
`  -H 'Content-Type: application/json' \`
`  -d '{`
`    "groups": [`
`        {`
`            "groupKey": "option1",`
`            "sourceLocations": [`
`                {`
`                    "locationKey": "wh1",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "maxQuantity": 12`
`                        }`
`                    ]`
`                }`
`            ],`
`            "sinkLocations": [`
`                {`
`                    "locationKey": "loc1",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 1,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                },`
`                {`
`                    "locationKey": "loc2",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 2,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                },`
`                {`
`                    "locationKey": "loc3",`
`                    "skus": [`
`                        {`
`                            "skuKey": "sku1",`
`                            "demandFactor": 3,`
`                            "maxQuantity": 100,`
`                            "minQuantity": 0`
`                        }`
`                    ]`
`                }`
`            ]`
`        }`
`    ]`
`}'`
yields a valid response. The actual optimization logic is not important
for this task and all short cuts are allowed.

## Local Setup

1. `pip install poetry`
2. Install dependencies: `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. Run the FastAPI server via poetry `poetry run ./run.sh`
4. Open http://localhost:8001/docs
5. Click the 'POST' buttons to send POST requests to the API
6. Click the 'GET' buttons to send GET requests to the API
7. Use the supplied test\_response.json and test\_reply.json as request body inputs to the requests
8. It is noted that curl\_request.txt returned a valid response when tested
