// Copyright (C) 2024 Bellande Robotics Sensors Research Innovation Center, Ronaldson Bellande

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

use reqwest;
use serde_json::{json, Value};
use std::error::Error;
use std::path::{Path, PathBuf};
use std::process::{self, Command};
use structopt::StructOpt;

#[derive(StructOpt, Debug)]
#[structopt(name = "bellande_step", about = "Bellande Step Tool")]
struct Opt {
    #[structopt(long, help = "First coordinate as JSON-formatted list")]
    node0: String,

    #[structopt(long, help = "Second coordinate as JSON-formatted list")]
    node1: String,

    #[structopt(long, help = "Limit for the algorithm")]
    limit: i32,

    #[structopt(long, help = "Number of dimensions")]
    dimensions: i32,

    #[structopt(long, help = "Use local executable instead of API")]
    use_executable: bool,
}

async fn make_bellande_step_request(
    node0: Value,
    node1: Value,
    limit: i32,
    dimensions: i32,
) -> Result<Value, Box<dyn Error>> {
    let client = reqwest::Client::new();
    let url = "https://bellande-robotics-sensors-research-innovation-center.org/api/Bellande_Step/bellande_step";

    let payload = json!({
        "node0": node0,
        "node1": node1,
        "limit": limit,
        "dimensions": dimensions,
        "auth": {
            "authorization_key": "bellande_web_api_opensource"
        }
    });

    let response = client
        .post(url)
        .header("accept", "application/json")
        .header("Content-Type", "application/json")
        .json(&payload)
        .send()
        .await?
        .json::<Value>()
        .await?;

    Ok(response)
}

fn get_executable_path() -> PathBuf {
    if cfg!(target_os = "windows") {
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("Bellande_Step.exe")
    } else {
        Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("Bellande_Step")
    }
}

fn run_bellande_step_executable(
    node0: &str,
    node1: &str,
    limit: i32,
    dimensions: i32,
) -> Result<(), Box<dyn Error>> {
    let executable_path = get_executable_path();
    let passcode = "bellande_step_executable_access_key";

    // Parse and validate input
    let node0_list: Value = serde_json::from_str(node0)?;
    let node1_list: Value = serde_json::from_str(node1)?;

    // Validate dimensions
    if let (Some(n0), Some(n1)) = (node0_list.as_array(), node1_list.as_array()) {
        if n0.len() != dimensions as usize || n1.len() != dimensions as usize {
            return Err(format!("Coordinates must have {} dimensions", dimensions).into());
        }
    }

    // Prepare and run command
    let output = Command::new(executable_path)
        .args(&[
            passcode,
            &node0,
            &node1,
            &limit.to_string(),
            &dimensions.to_string(),
        ])
        .output()?;

    if output.status.success() {
        println!("{}", String::from_utf8_lossy(&output.stdout));
        Ok(())
    } else {
        Err(format!(
            "Process failed: {}",
            String::from_utf8_lossy(&output.stderr)
        ).into())
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let opt = Opt::from_args();

    // Parse JSON strings to Values for validation
    let node0: Value = serde_json::from_str(&opt.node0)
        .map_err(|e| format!("Error parsing node0: {}", e))?;
    let node1: Value = serde_json::from_str(&opt.node1)
        .map_err(|e| format!("Error parsing node1: {}", e))?;

    if opt.use_executable {
        // Run using local executable
        if let Err(e) = run_bellande_step_executable(
            &opt.node0,
            &opt.node1,
            opt.limit,
            opt.dimensions,
        ) {
            eprintln!("Error: {}", e);
            process::exit(1);
        }
    } else {
        // Run using API
        match make_bellande_step_request(node0, node1, opt.limit, opt.dimensions).await {
            Ok(result) => {
                println!("{}", serde_json::to_string_pretty(&result)?);
            }
            Err(e) => {
                eprintln!("Error: {}", e);
                process::exit(1);
            }
        }
    }

    Ok(())
}
