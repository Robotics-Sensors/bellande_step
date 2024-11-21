# Copyright (C) 2024 Bellande Robotics Sensors Research Innovation Center, Ronaldson Bellande

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

import requests
import argparse
import json
import sys

def make_bellande_step_request(node0, node1, limit, dimensions):
    url = "https://bellande-robotics-sensors-research-innovation-center.org/api/Bellande_Step/bellande_step_nd"
    
    # Convert string inputs to lists if they're strings
    if isinstance(node0, str):
        node0 = json.loads(node0)
    if isinstance(node1, str):
        node1 = json.loads(node1)
    
    payload = {
        "node0": node0,
        "node1": node1,
        "limit": limit,
        "dimensions": dimensions,
        "auth": {
            "authorization_key": "bellande_web_api_opensource"
        }
    }
    
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error making request: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Run Bellande Step API")
    parser.add_argument("--node0", required=True, help="First coordinate as JSON-formatted list")
    parser.add_argument("--node1", required=True, help="Second coordinate as JSON-formatted list")
    parser.add_argument("--limit", type=int, required=True, help="Limit for the algorithm")
    parser.add_argument("--dimensions", type=int, required=True, help="Number of dimensions")
    
    args = parser.parse_args()
    
    try:
        result = make_bellande_step_request(
            args.node0,
            args.node1,
            args.limit,
            args.dimensions
        )
        
        print(json.dumps(result, indent=2))
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in coordinates - {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
