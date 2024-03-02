# API Usage Examples

## Python Example:
```python

import requests

# Input variables
x1 = 1
y1 = 1
x2 = 5
y2 = 5
limit = 50

# Make POST request
response = requests.post('https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d', json={"node0": {"x": x1, "y": y1}, "node1": {"x": x2, "y": y2}, "limit": limit})
data = response.json()
next_step = data.get('next_step')
print(next_step)
```

## C++ Example
```c++

#include <iostream>
#include <cpprest/http_client.h>
#include <cpprest/json.h>

using namespace web;
using namespace web::http;
using namespace web::http::client;

int main() {
    // Input variables
    int x1 = 1;
    int y1 = 1;
    int x2 = 5;
    int y2 = 5;
    int limit = 50;

    // Create JSON objects
    json::value node0;
    node0[U("x")] = json::value::number(x1);
    node0[U("y")] = json::value::number(y1);
    json::value node1;
    node1[U("x")] = json::value::number(x2);
    node1[U("y")] = json::value::number(y2);

    // Create JSON object for request body
    json::value request_body;
    request_body[U("node0")] = node0;
    request_body[U("node1")] = node1;
    request_body[U("limit")] = json::value::number(limit);

    // Make POST request
    http_client client(U("https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d"));
    http_response response = client.request(methods::POST, U("/step"), request_body.serialize(), U("application/json")).get();
    
    // Parse response
    if (response.status_code() == status_codes::OK) {
        json::value response_body = response.extract_json().get();
        json::value next_step = response_body[U("next_step")];
        std::wcout << next_step.serialize() << std::endl;
    } else {
        std::cerr << "Error: " << response.status_code() << std::endl;
    }

    return 0;
}

```

## Java Example

```java

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        try {
            // Input variables
            int x1 = 1;
            int y1 = 1;
            int x2 = 5;
            int y2 = 5;
            int limit = 50;

            // Create JSON objects
            String node0 = "{\"x\": " + x1 + ", \"y\": " + y1 + "}";
            String node1 = "{\"x\": " + x2 + ", \"y\": " + y2 + "}";

            // Create request body
            String requestBody = "{\"node0\": " + node0 + ", \"node1\": " + node1 + ", \"limit\": " + limit + "}";

            // Make POST request
            URL url = new URL("https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);

            try (OutputStream outputStream = connection.getOutputStream()) {
                byte[] input = requestBody.getBytes("utf-8");
                outputStream.write(input, 0, input.length);
            }

            try (BufferedReader responseReader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = responseReader.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println(response.toString());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## Javascript Example

```javascript

// Example using fetch API
let x1 = 1;
let y1 = 1;
let x2 = 5;
let y2 = 5;
let limit = 50;

fetch('https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    node0: { x: x1, y: y1 },
    node1: { x: x2, y: y2 },
    limit: limit
  })
})
.then(response => response.json())
.then(data => console.log(data.next_step))
.catch(error => console.error('Error:', error));
```

## Rust Example

```rust

use reqwest::blocking::Client;
use serde_json::json;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Input variables
    let x1 = 1;
    let y1 = 1;
    let x2 = 5;
    let y2 = 5;
    let limit = 50;

    // Create JSON objects
    let node0 = json!({"x": x1, "y": y1});
    let node1 = json!({"x": x2, "y": y2});

    // Create JSON object for request body
    let request_body = json!({"node0": node0, "node1": node1, "limit": limit});

    // Make POST request
    let client = Client::new();
    let response = client.post("https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d")
        .json(&request_body)
        .send()?;
    
    let data: serde_json::Value = response.json()?;
    println!("{}", data["next_step"]);

    Ok(())
}
```

## Go Example

```go

package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	// Input variables
	x1 := 1
	y1 := 1
	x2 := 5
	y2 := 5
	limit := 50

	// Create request body
	node0 := map[string]int{"x": x1, "y": y1}
	node1 := map[string]int{"x": x2, "y": y2}
	requestBody := map[string]interface{}{"node0": node0, "node1": node1, "limit": limit}

	// Marshal JSON
	jsonBody, err := json.Marshal(requestBody)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	// Make POST request
	resp, err := http.Post("https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d", "application/json", bytes.NewBuffer(jsonBody))
	if err != nil {
		fmt.Println("Error making request:", err)
		return
	}
	defer resp.Body.Close()

	// Read response body
	var response map[string]interface{}
	err = json.NewDecoder(resp.Body).Decode(&response)
	if err != nil {
		fmt.Println("Error decoding response:", err)
		return
	}

	// Print next_step
	fmt.Println(response["next_step"])
}
```

## Swift Example

```swift
import Foundation

// Define input variables
let x1 = 1
let y1 = 1
let x2 = 5
let y2 = 5
let limit = 50

// Create JSON request body
let requestBody: [String: Any] = [
    "node0": ["x": x1, "y": y1],
    "node1": ["x": x2, "y": y2],
    "limit": limit
]

// Convert request body to Data
let jsonData = try! JSONSerialization.data(withJSONObject: requestBody)

// Create HTTP request
var request = URLRequest(url: URL(string: "https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d")!)
request.httpMethod = "POST"
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = jsonData

// Send HTTP request
let task = URLSession.shared.dataTask(with: request) { data, response, error in
    guard let data = data, error == nil else {
        print("Error: \(error?.localizedDescription ?? "Unknown error")")
        return
    }
    
    // Parse response JSON
    do {
        if let json = try JSONSerialization.jsonObject(with: data) as? [String: Any] {
            if let nextStep = json["next_step"] {
                print(nextStep)
            }
        }
    } catch {
        print("Error decoding response: \(error.localizedDescription)")
    }
}
task.resume()
```

## C# Example

```c#

using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    static async Task Main(string[] args)
    {
        // Input variables
        int x1 = 1;
        int y1 = 1;
        int x2 = 5;
        int y2 = 5;
        int limit = 50;

        // Create JSON request body
        var requestBody = new
        {
            node0 = new { x = x1, y = y1 },
            node1 = new { x = x2, y = y2 },
            limit = limit
        };

        // Convert request body to JSON string
        var jsonBody = JsonConvert.SerializeObject(requestBody);

        // Create HttpClient
        using (var client = new HttpClient())
        {
            // Set base address of API
            client.BaseAddress = new Uri("https://bellanderoboticssensorsresearchinnovationcenterapi-7xm5pkao.b4a.run/Bellande_Step/bellande_step_2d");

            // Set headers
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

            // Make POST request
            var response = await client.PostAsync("", new StringContent(jsonBody, System.Text.Encoding.UTF8, "application/json"));

            // Check if request was successful
            if (response.IsSuccessStatusCode)
            {
                // Read response content
                var responseContent = await response.Content.ReadAsStringAsync();

                // Deserialize JSON response
                dynamic responseData = JsonConvert.DeserializeObject(responseContent);

                // Get next_step from response
                var nextStep = responseData.next_step;

                // Print next_step
                Console.WriteLine(nextStep);
            }
            else
            {
                // Print error message
                Console.WriteLine($"Error: {response.StatusCode}");
            }
        }
    }
}
```
