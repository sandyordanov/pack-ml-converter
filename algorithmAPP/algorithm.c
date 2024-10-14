#include <stdio.h>
#include <stdlib.h>
#include <librdkafka/rdkafka.h>
#include <cjson/cJSON.h>

// // Function to consume messages from Kafka
// void consume_kafka_message(rd_kafka_message_t *rkmessage) {
//     if (rkmessage->err) {
//         printf("Error: %s\n", rd_kafka_message_errstr(rkmessage));
//         return;
//     }

//     // Get the message payload (JSON string)
//     const char *json_data = (char *)rkmessage->payload;

//     // Parse JSON using cJSON
//     cJSON *json = cJSON_Parse(json_data);
//     if (!json) {
//         printf("Error parsing JSON: %s\n", cJSON_GetErrorPtr());
//         return;
//     }

//     // Extract fields from the JSON object
//     cJSON *name = cJSON_GetObjectItemCaseSensitive(json, "DataEntityName");
//     cJSON *payload = cJSON_GetObjectItemCaseSensitive(json, "Payload");
//     cJSON *timestamp = cJSON_GetObjectItemCaseSensitive(json, "Timestamp");

//     // Print the extracted values
//     if (cJSON_IsString(name) && name->valuestring != NULL) {
//         printf("Name: %s\n", name->valuestring);
//     }

//     if (cJSON_IsNumber(payload)) {
//         printf("Payload: %d\n", payload->valueint);
//     }

//     if (cJSON_IsNumber(timestamp)) {
//         printf("Timestamp: %d\n", timestamp-> valueint);
//     }

//     if (cJSON_IsNumber(payload))
//     {
//         int previous_payload = 0;
//         int current_payload = payload->valueint;

//         // Check for invalid state transitions
//         if (previous_payload != -1 && current_payload == previous_payload)
//         {
//             printf("Error: Invalid transition. Payload value did not change (stayed at %d).\n", current_payload);
//         }
//         else
//         {
//             if (current_payload == 1)
//             {
//                 printf("Status: executing\n");
//             }
//             else if (current_payload == 0)
//             {
//                 printf("Status: idle\n");
//             }
//             else
//             {
//                 printf("Unknown Payload value: %d\n", payload->valueint);
//             }
//             // Update the previous payload value
//             previous_payload = current_payload;
//         }
//     }

//     // Clean up
//     cJSON_Delete(json);
// }

// int main() {
//     rd_kafka_t *rk;        // Kafka instance
//     rd_kafka_conf_t *conf;  // Kafka configuration
//     rd_kafka_topic_t *rkt;  // Kafka topic
//     char errstr[512];       // Buffer for error messages

//     const char *brokers = "localhost:9092";  // Kafka broker address
//     const char *topic = "Dummies";          // Kafka topic to subscribe to

//     // Create Kafka configuration
//     conf = rd_kafka_conf_new();

//     // Create Kafka consumer instance
//     rk = rd_kafka_new(RD_KAFKA_CONSUMER, conf, errstr, sizeof(errstr));
//     if (!rk) {
//         fprintf(stderr, "Failed to create consumer: %s\n", errstr);
//         return 1;
//     }

//     // Add Kafka brokers
//     if (rd_kafka_brokers_add(rk, brokers) == 0) {
//         fprintf(stderr, "No valid Kafka brokers specified\n");
//         return 1;
//     }

//     // Create Kafka topic object
//     rkt = rd_kafka_topic_new(rk, topic, NULL);

//     // Start consuming messages from the Kafka topic
//     rd_kafka_consume_start(rkt, 0, RD_KAFKA_OFFSET_END);

//     // Consume messages and parse JSON
//     // while (1) {
//     //     rd_kafka_message_t *rkmessage;
//     //     rkmessage = rd_kafka_consume(rkt, 0, 1000);  // 1000ms timeout
//     //     if (rkmessage) {
//     //         consume_kafka_message(rkmessage);
//     //         rd_kafka_message_destroy(rkmessage);
//     //     }
//     // }

//     const char *test_json_1 = "{\"DataEntityName\": \"Line1\", \"Payload\": 1, \"Timestamp\": 1697289000}";
//     const char *test_json_2 = "{\"DataEntityName\": \"Line1\", \"Payload\": 1, \"Timestamp\": 1697289001}"; // Invalid transition
//     const char *test_json_3 = "{\"DataEntityName\": \"Line1\", \"Payload\": 0, \"Timestamp\": 1697289002}"; // Valid transition
//     const char *test_json_4 = "{\"DataEntityName\": \"Line1\", \"Payload\": 0, \"Timestamp\": 1697289003}"; // Invalid transition

//     // Simulate consuming messages
//     printf("Testing with payload 1 (should be executing):\n");
//     consume_kafka_message(test_json_1);

//     printf("\nTesting with payload 1 again (should show error):\n");
//     consume_kafka_message(test_json_2);

//     printf("\nTesting with payload 0 (should be idle):\n");
//     consume_kafka_message(test_json_3);

//     printf("\nTesting with payload 0 again (should show error):\n");
//     consume_kafka_message(test_json_4);

//     // Clean up
//     rd_kafka_consume_stop(rkt, 0);
//     rd_kafka_topic_destroy(rkt);
//     rd_kafka_destroy(rk);

//     return 0;
// }

int previous_payload = -1; // Start with -1 to indicate no previous value

// Function to simulate consuming messages from Kafka
void consume_kafka_message_simulated(const char *json_data)
{
    // Parse JSON using cJSON
    cJSON *json = cJSON_Parse(json_data);
    if (!json)
    {
        printf("Error parsing JSON: %s\n", cJSON_GetErrorPtr());
        return;
    }

    // Extract fields from the JSON object
    cJSON *name = cJSON_GetObjectItemCaseSensitive(json, "DataEntityName");
    cJSON *payload = cJSON_GetObjectItemCaseSensitive(json, "Payload");
    cJSON *timestamp = cJSON_GetObjectItemCaseSensitive(json, "Timestamp");

    // Print the extracted values
    if (cJSON_IsString(name) && name->valuestring != NULL)
    {
        printf("Name: %s\n", name->valuestring);
    }

    if (cJSON_IsNumber(payload))
    {
        printf("Payload: %d\n", payload->valueint);
    }

    if (cJSON_IsNumber(timestamp))
    {
        printf("Timestamp: %d\n", timestamp->valueint);
    }

    if (cJSON_IsNumber(payload))
    {
        int current_payload = payload->valueint;

        // Check for invalid state transitions
        if (previous_payload != -1 && current_payload == previous_payload)
        {
            printf("Error: Invalid transition. Payload value did not change (stayed at %d).\n", current_payload);
        }
        else
        {
            if (current_payload == 1)
            {
                printf("Status: executing\n");
            }
            else if (current_payload == 0)
            {
                printf("Status: idle\n");
            }
            else
            {
                printf("Unknown Payload value: %d\n", payload->valueint);
            }
            // Update the previous payload value
            previous_payload = current_payload;
        }
    }

    // Clean up
    cJSON_Delete(json);
}

int main()
{
    // Simulated test JSON data
    const char *test_json_1 = "{\"DataEntityName\": \"Line1\", \"Payload\": 1, \"Timestamp\": 1697289000}";
    const char *test_json_2 = "{\"DataEntityName\": \"Line1\", \"Payload\": 1, \"Timestamp\": 1697289001}"; // Invalid transition
    const char *test_json_3 = "{\"DataEntityName\": \"Line1\", \"Payload\": 0, \"Timestamp\": 1697289002}"; // Valid transition
    const char *test_json_4 = "{\"DataEntityName\": \"Line1\", \"Payload\": 0, \"Timestamp\": 1697289003}"; // Invalid transition

    // Simulate consuming messages
    printf("Testing with payload 1 (should be executing):\n");
    consume_kafka_message_simulated(test_json_1);

    printf("\nTesting with payload 1 again (should show error):\n");
    consume_kafka_message_simulated(test_json_2);

    printf("\nTesting with payload 0 (should be idle):\n");
    consume_kafka_message_simulated(test_json_3);

    printf("\nTesting with payload 0 again (should show error):\n");
    consume_kafka_message_simulated(test_json_4);

    return 0;
}
