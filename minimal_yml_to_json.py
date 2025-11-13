#!/usr/bin/env python3
"""
Minimal YAML Parser
The simplest possible implementation to parse YAML files
"""

import yaml
import sys
import json

def parse_yaml(file_path):
    """Parse a YAML file and return the data"""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

if __name__ == "__main__":
    # Get file path from command line argument
    if len(sys.argv) != 2:
        print("Usage: python minimal_yml_to_json.py <yaml_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        # Parse the YAML file
        parsed_data = parse_yaml(file_path)
        
        # Convert to proper JSON format
        print(json.dumps(parsed_data))
    except Exception as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
