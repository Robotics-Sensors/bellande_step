# 📦 Bellande Step (Infinite Dimensions)

![Demo GIF](bellande_step_api_package.gif)

## Preprint
- [![Preprint](https://img.shields.io/badge/Preprint-Bellande%20Step-0099cc?style=for-the-badge)](https://dapp.orvium.io/deposits/6650ccb8afb407dc8beb0ff2/view)

# Preprint Citation
```
Bellande, R. (2024). Efficient Step Function for Infinite Multi-Dimensional Node Calculation within Model-Integrated Dimensional Space [version 1] [preprint]. Mathematics.
```


## 🧙 Organization Website
- [![Organization Website](https://img.shields.io/badge/Explore%20Our-Website-0099cc?style=for-the-badge)](https://robotics-sensors.github.io)

## 🧙 Organization Github
- [![Organization Github ](https://img.shields.io/badge/Explore%20Our-Github-0099cc?style=for-the-badge)](https://github.com/Robotics-Sensors)

# Author, Creator and Maintainer
- **Ronaldson Bellande**

## Bellande Step Executables & Models
- [![Bellande Step Models & Executables ](https://img.shields.io/badge/Bellande%20Step-Models/Executables-0099cc?style=for-the-badge)](https://github.com/Artificial-Intelligence-Computer-Vision/bellande_step_models_executables)

# API HTTP Usability (BELLANDE FORMAT)
```
# Copyright (C) 2024 Bellande Robotics Sensors Research Innovation Center, Ronaldson Bellande
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# GNU General Public License v3.0 or later

url: https://bellande-robotics-sensors-research-innovation-center.org

endpoint_path:
    bellande_step: /api/Bellande_Step/bellande_step_nd

Bellande_Framework_Access_Key: bellande_web_api_opensource
```

# API HTTP Usability (JSON FORMAT)
```
{
  "license": [
    "Copyright (C) 2024 Bellande Robotics Sensors Research Innovation Center, Ronaldson Bellande",
    "This program is free software: you can redistribute it and/or modify",
    "it under the terms of the GNU General Public License as published by",
    "the Free Software Foundation, either version 3 of the License, or",
    "(at your option) any later version.",
    "",
    "This program is distributed in the hope that it will be useful,",
    "but WITHOUT ANY WARRANTY; without even the implied warranty of",
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
    "GNU General Public License for more details.",
    "",
    "You should have received a copy of the GNU General Public License",
    "along with this program.  If not, see <https://www.gnu.org/licenses/>.",
    "GNU General Public License v3.0 or later"
  ],
  "url": "https://bellande-robotics-sensors-research-innovation-center.org",
  "endpoint_path": {
    "bellande_step": "/api/Bellande_Step/bellande_step_nd"
  },
  "Bellande_Framework_Access_Key": "bellande_web_api_opensource"
}
```

# API Payload Example
```
{
    "node0": [0, 0, 0],
    "node1": [100, 100, 100],
    "limit": 75,
    "dimensions": 3,
    "auth": {
      "authorization_key": "bellande_web_api_opensource"
    }
}
```

# 🧙 Website Bellande API Testing 
- [![Website API Testing](https://img.shields.io/badge/Bellande%20API-Testing-0099cc?style=for-the-badge)](https://bellanderoboticssensorsresearchinnovationcenterwebsite-kot42qxp.b4a.run/api/bellande_step_experiment)
  
# Quick Bellande API Testing
```
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
```

# BS(Bellande Step) Algorithm API
## Experiment 1 -- Limit = 1

| ![2D](graphs_charts/graph_charts_1/2D_Space.png) *Figure 2D* | ![3D](graphs_charts/graph_charts_1/3D_Space.png) *Figure 3D* | ![4D](graphs_charts/graph_charts_1/4D_Space.png) *Figure 4D* |
|:------------------------------------------------------------:|:------------------------------------------------------------:|:------------------------------------------------------------:|
| ![5D](graphs_charts/graph_charts_1/5D_Space.png) *Figure 5D* | ![6D](graphs_charts/graph_charts_1/6D_Space.png) *Figure 6D* | ![7D](graphs_charts/graph_charts_1/7D_Space.png) *Figure 7D* |
| ![8D](graphs_charts/graph_charts_1/8D_Space.png) *Figure 8D* | ![9D](graphs_charts/graph_charts_1/9D_Space.png) *Figure 9D* | ![10D](graphs_charts/graph_charts_1/10D_Space.png) *Figure 10D* |


## Experiment 2 -- Limit = 25

| ![2D](graphs_charts/graph_charts_25/2D_Space.png) *Figure 2D* | ![3D](graphs_charts/graph_charts_25/3D_Space.png) *Figure 3D* | ![4D](graphs_charts/graph_charts_25/4D_Space.png) *Figure 4D* |
|:-------------------------------------------------------------:|:-------------------------------------------------------------:|:-------------------------------------------------------------:|
| ![5D](graphs_charts/graph_charts_25/5D_Space.png) *Figure 5D* | ![6D](graphs_charts/graph_charts_25/6D_Space.png) *Figure 6D* | ![7D](graphs_charts/graph_charts_25/7D_Space.png) *Figure 7D* |
| ![8D](graphs_charts/graph_charts_25/8D_Space.png) *Figure 8D* | ![9D](graphs_charts/graph_charts_25/9D_Space.png) *Figure 9D* | ![10D](graphs_charts/graph_charts_25/10D_Space.png) *Figure 10D* |


## Experiment 3 -- Limit = 50

| ![2D](graphs_charts/graph_charts_50/2D_Space.png) *Figure 2D* | ![3D](graphs_charts/graph_charts_50/3D_Space.png) *Figure 3D* | ![4D](graphs_charts/graph_charts_50/4D_Space.png) *Figure 4D* |
|:-------------------------------------------------------------:|:-------------------------------------------------------------:|:-------------------------------------------------------------:|
| ![5D](graphs_charts/graph_charts_50/5D_Space.png) *Figure 5D* | ![6D](graphs_charts/graph_charts_50/6D_Space.png) *Figure 6D* | ![7D](graphs_charts/graph_charts_50/7D_Space.png) *Figure 7D* |
| ![8D](graphs_charts/graph_charts_50/8D_Space.png) *Figure 8D* | ![9D](graphs_charts/graph_charts_50/9D_Space.png) *Figure 9D* | ![10D](graphs_charts/graph_charts_50/10D_Space.png) *Figure 10D* |


## Experiment 4 -- Limit = 75

| ![2D](graphs_charts/graph_charts_75/2D_Space.png) *Figure 2D* | ![3D](graphs_charts/graph_charts_75/3D_Space.png) *Figure 3D* | ![4D](graphs_charts/graph_charts_75/4D_Space.png) *Figure 4D* |
|:-------------------------------------------------------------:|:-------------------------------------------------------------:|:-------------------------------------------------------------:|
| ![5D](graphs_charts/graph_charts_75/5D_Space.png) *Figure 5D* | ![6D](graphs_charts/graph_charts_75/6D_Space.png) *Figure 6D* | ![7D](graphs_charts/graph_charts_75/7D_Space.png) *Figure 7D* |
| ![8D](graphs_charts/graph_charts_75/8D_Space.png) *Figure 8D* | ![9D](graphs_charts/graph_charts_75/9D_Space.png) *Figure 9D* | ![10D](graphs_charts/graph_charts_75/10D_Space.png) *Figure 10D* |


## Experiment 5 -- Limit = 100

| ![2D](graphs_charts/graph_charts_100/2D_Space.png) *Figure 2D* | ![3D](graphs_charts/graph_charts_100/3D_Space.png) *Figure 3D* | ![4D](graphs_charts/graph_charts_100/4D_Space.png) *Figure 4D* |
|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:|
| ![5D](graphs_charts/graph_charts_100/5D_Space.png) *Figure 5D* | ![6D](graphs_charts/graph_charts_100/6D_Space.png) *Figure 6D* | ![7D](graphs_charts/graph_charts_100/7D_Space.png) *Figure 7D* |
| ![8D](graphs_charts/graph_charts_100/8D_Space.png) *Figure 8D* | ![9D](graphs_charts/graph_charts_100/9D_Space.png) *Figure 9D* | ![10D](graphs_charts/graph_charts_100/10D_Space.png) *Figure 10D* |

# Bellande Step Usage

## Website Crates
- https://crates.io/crates/bellande_step

### Installation
- `cargo add bellande_step`

## Website PYPI
- https://pypi.org/project/bellande_robot_step

### Installation
- `$ pip install bellande_robot_step`

### Upgrade (if not upgraded)
- `$ pip install --upgrade bellande_robot_step`

```
Name: bellande_robot_step
Version: 0.3.0
Summary: Computes the next step towards a target node
Home-page: github.com/RonaldsonBellande/bellande_robot_step
Author: Ronaldson Bellande
Author-email: ronaldsonbellande@gmail.com
License: GNU General Public License v3.0
Required-by:
```

## Published Paper
```
Coming Soon
```

## Preprint
- [![Preprint](https://img.shields.io/badge/Preprint-Bellande%20Step-0099cc?style=for-the-badge)](https://dapp.orvium.io/deposits/6650ccb8afb407dc8beb0ff2/view)


## License
This Algorithm or Models is distributed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/), see [LICENSE](https://github.com/RonaldsonBellande/bellande_step/blob/main/LICENSE) and [NOTICE](https://github.com/RonaldsonBellande/bellande_step/blob/main/LICENSE) for more information.
