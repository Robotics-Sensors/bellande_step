curl -X 'POST' \
  'https://bellande-robotics-sensors-research-innovation-center.org/api/Bellande_Step/bellande_step_nd' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "node0": [0, 0, 0],
    "node1": [100, 100, 100],
    "limit": 75,
    "dimensions": 3,
    "auth": {
      "authorization_key": "bellande_web_api_opensource"
    }
  }'

echo ""
