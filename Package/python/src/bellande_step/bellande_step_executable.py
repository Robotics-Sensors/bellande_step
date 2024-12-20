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

import subprocess
import argparse
import json
import os
import sys

def get_executable_path():
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(application_path, 'Bellande_Step')

def run_bellande_step(node0, node1, limit, dimensions):
    executable_path = get_executable_path()
    passcode = "bellande_step_executable_access_key"

    # Convert string representations of coordinates to actual lists
    node0_list = json.loads(node0)
    node1_list = json.loads(node1)

    # Validate input
    if len(node1_list) != dimensions or len(node0_list) != dimensions:
        raise ValueError(f"Coordinates must have {dimensions} dimensions")

    # Prepare the command
    command = [
        executable_path,
        passcode,
        json.dumps(node0_list),
        json.dumps(node1_list),
        str(limit),
        str(dimensions)
    ]

    # Run the command
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)
        print("Error output:", e.stderr)

def main():
    parser = argparse.ArgumentParser(description="Run Bellande Step Executable")
    parser.add_argument("--node0", help="First coordinate as a JSON-formatted list")
    parser.add_argument("--node1", help="Second coordinate as a JSON-formatted list")
    parser.add_argument("--limit", type=int, help="Limit for the algorithm")
    parser.add_argument("--dimensions", type=int, help="Number of dimensions")
    
    args = parser.parse_args()

    run_bellande_step(
        args.node0,
        args.node1,
        args.limit,
        args.dimensions
    )

if __name__ == "__main__":
    main()
