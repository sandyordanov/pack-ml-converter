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
        measurement = "machine_status"
        tags = {
            "name": data.get("name"),
            "UnitModeCurrent": data["status"].get("UnitModeCurrent"),
            "StateCurrent": data["status"].get("StateCurrent")
        }
        fields = {
            "ExecuteTime": data["status"].get("ExecuteTime"),
            "MachSpeed": data["status"].get("MachSpeed"),
            "CurMachSpeed": data["status"].get("CurMachSpeed"),
            "blocked": data["status"]["EquipmentInterlock"].get("blocked"),
            "starved": data["status"]["EquipmentInterlock"].get("starved"),
            "StopReasonID": data["admin"].get("StopReason.ID"),
            "ProdProcessedCount": data["admin"]["ProdProcessedCount"].get("count"),
            "ProdDefectiveCount": data["admin"]["ProdDefectiveCount"].get("count"),
            "UnitModeCommand": data["command"].get("UnitMode"),
            "UnitModeChangeRequest": data["command"].get("UnitModeChangeRequest"),
            "MachSpeedCommand": data["command"].get("MachSpeed"),
            "CntrlCmd": data["command"].get("CntrlCmd"),
            "CmdChangeRequest": data["command"].get("CmdChangeRequest"),
        }
        timestamp = data["admin"].get("MessageTimestamp")
        dt = datetime.datetime.fromisoformat(timestamp)
        nanoseconds = int(dt.timestamp() * 1e9)


        # Create a Point object
        point = Point(measurement)
        for tag_key, tag_value in tags.items():
            if tag_value is not None:
                point.tag(tag_key, tag_value)
        for field_key, field_value in fields.items():
            if field_value is not None:
                point.field(field_key, field_value)
        point.time(nanoseconds)

        # Write to InfluxDB
        write_api.write(bucket="packTag_bucket", org=org, record=point)

        # Close the client
        client.close()
        print("Data written successfully!")
