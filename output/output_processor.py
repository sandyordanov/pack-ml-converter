import os
from input.input import Input
#from faststream import FastStream
#from faststream.kafka import KafkaBroker
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import datetime
"""
Created by Dion van der Broek
Summary: Class in charge of outputting JSON object to selected output destination
Reviewed & Edited by Aga Henriquez
"""
# Created by Dion
class OutputProcessor:
    def __init__(self, broker=None):
        self.broker = broker  # Optional broker (used for Kafka if available)

    def write_to_console(self, data):
        # Output to console
        print(f"Converted JSON PackTag: {data}")

    def write_to_file(self, pack_tag_data):  # Writes packtag to a specific file
        """
        Write JSON data to a file (pretty-printed).
        """
        output_file_path = './testData/output.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Write the JSON data to the file
        with open(output_file_path, 'w') as output_file:
            # Pretty print JSON data
            json.dump(pack_tag_data, output_file, indent=4)

    #written by Aleksandar Yordanov
    def write_to_file_append(self, pack_tag_data):
        """
        Append JSON data to a file (pretty-printed).
        """
        output_file_path = './testData/output.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Append the JSON data to the file
        with open(output_file_path, 'a') as output_file:
            # Add a separator for clarity between JSON objects if needed
            if os.path.getsize(output_file_path) > 0:  # Check if file is not empty
                output_file.write("\n")  # Add a newline for separation
            # Pretty print JSON data and append it
            json.dump(pack_tag_data, output_file, indent=4)

    def write_runtime_data_to_file(self, pack_tag_data):  # Writes packtag to a runtime file
        """
        Write runtime JSON data to a different file (pretty-printed).
        """
        output_file_path = './testData/runtime.txt'

        # Ensure the directory exists before writing
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w') as output_file:
            # Pretty print JSON data
            json.dump(pack_tag_data, output_file, indent=4)

    async def write_to_kafka(self, topic, data):
        """
        Publish the data to a Kafka topic.
        """
        try:
            if not self.broker:
                print("Kafka broker is not initialized.")
                return

            # Ensure data is JSON-formatted
            message = json.dumps(data)

            # Publish the message to the Kafka topic
            await self.broker.publish(topic, message)

            print(f"Message successfully published to topic '{topic}'")

        except Exception as e:
            print(f"Error publishing message to Kafka: {e}")

    # written by Aleksandar Yordanov
    def write_to_database(self, data):
        token = "cN_-DaTc83j5HdJEKxZPuFUD-0GXsf-O8kaWa-Ab-Agi9qyKijncQOurGWTNF5hF_gzJ0i2o8ZtgWxmMMtaO-g=="
        org = "my_org"
        url = "http://192.168.2.127:8086"

        # Initialize InfluxDB client
        client = InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        # Parse the JSON data
        state_measurement = "machine_status"
        execution_time_measurement = "execution_time"

        tags = {
            "name": data.get("name"),
        }
        state = data["status"].get("StateCurrent")
        execute_time = data["status"].get("ExecuteTime")

        timestamp = data["admin"].get("MessageTimestamp")
        dt = datetime.datetime.fromisoformat(timestamp)
        nanoseconds = int(dt.timestamp() * 1e9)

        # Write StateCurrent to "machine_status" measurement
        if state:
            state_point = Point(state_measurement)
            for tag_key, tag_value in tags.items():
                if tag_value is not None:
                    state_point.tag(tag_key, tag_value)
            state_point.field("StateCurrent", state)
            state_point.time(nanoseconds)
            write_api.write(bucket="new_bucket", org=org, record=[state_point])

        # Write ExecuteTime to "execution_time" measurement if state is COMPLETE
        if state == "COMPLETE" and execute_time is not None:
            execution_point = Point(execution_time_measurement)
            for tag_key, tag_value in tags.items():
                if tag_value is not None:
                    execution_point.tag(tag_key, tag_value)
            execution_point.field("ExecuteTime", float(execute_time))
            execution_point.time(nanoseconds)
            write_api.write(bucket="new_bucket", org=org, record=[execution_point])

        # Close the client
        client.close()
        print("Data written successfully!")

    def write_to_database2(self, data):
        token = "cN_-DaTc83j5HdJEKxZPuFUD-0GXsf-O8kaWa-Ab-Agi9qyKijncQOurGWTNF5hF_gzJ0i2o8ZtgWxmMMtaO-g=="
        org = "my_org"
        url = "http://192.168.2.127:8086"

        # Initialize InfluxDB client
        client = InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        # Parse the JSON data
        measurement = "status_and_time"

        tags = {
            "name": data.get("name"),  # Tag
        }
        fields = {
            "StateCurrent": data["status"].get("StateCurrent"),  # Field 1
            "ExecuteTime": float(data["status"].get("ExecuteTime")),  # Field 2
        }
        timestamp = data["admin"].get("MessageTimestamp")
        dt = datetime.datetime.fromisoformat(timestamp)
        nanoseconds = int(dt.timestamp() * 1e9)  # Convert to nanoseconds

        # Create a single Point object with multiple fields
        point = Point(measurement).time(nanoseconds)

        # Add tags
        for tag_key, tag_value in tags.items():
            if tag_value is not None:
                point.tag(tag_key, tag_value)

        # Add fields
        for field_key, field_value in fields.items():
            if field_value is not None:
                point.field(field_key, field_value)

        # Write to InfluxDB
        write_api.write(bucket="gBucket", org=org, record=point)

        # Close the client
        client.close()
        print("Data written successfully!")