#include <stdio.h>
#include <stdlib.h>
#include <librdkafka/rdkafka.h>
#include <cjson/cJSON.h>
#include <string.h>


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

#define MAX_ENTITIES 100

// Structure to hold the state of each DataEntity
typedef struct
{
    char name[50];    // Adjust size as needed
    int currentValue; // 1 for executing, 0 for idle
    int timestamp;    // Store the timestamp
} DataEntity;

// Array to hold the states of entities
DataEntity entities[MAX_ENTITIES];
int entityCount = 0;

// Function to find an entity by name
DataEntity *find_entity(const char *name)
{
    for (int i = 0; i < entityCount; i++)
    {
        if (strcmp(entities[i].name, name) == 0)
        {
            return &entities[i];
        }
    }
    return NULL; // Not found
}

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

    // Ensure name is a string and payload/timestamp are numbers
    if (!cJSON_IsString(name) || !cJSON_IsNumber(payload) || !cJSON_IsNumber(timestamp))
    {
        printf("Invalid data format\n");
        cJSON_Delete(json);
        return;
    }

    // Find the entity in the list
    DataEntity *entity = find_entity(name->valuestring);

    if (entity)
    {
        // Entity already exists, check its current value
        int current_payload = payload->valueint;

        // Check for invalid state transitions
        if (current_payload == entity->currentValue)
        { // Check if the current payload is the same as the previous
            printf("Error: %s already has the value %d\n", name->valuestring, entity->currentValue);
        }
        else
        {
            // Update the entity's current value and timestamp
            entity->currentValue = current_payload;
            entity->timestamp = timestamp->valueint; // Update the timestamp
            printf("Name: %s, Status: %s, Timestamp: %d\n", name->valuestring,
                   (current_payload == 1) ? "executing" : "idle", entity->timestamp);
        }
    }
    else
    {
        // New entity, add it to the list
        if (entityCount < MAX_ENTITIES)
        {
            strcpy(entities[entityCount].name, name->valuestring);
            entities[entityCount].currentValue = payload->valueint;
            entities[entityCount].timestamp = timestamp->valueint; // Set timestamp for new entity
            printf("Name: %s, Status: %s, Timestamp: %d\n", name->valuestring,
                   (payload->valueint == 1) ? "executing" : "idle", entities[entityCount].timestamp);
            entityCount++;
        }
        else
        {
            printf("Error: Maximum entity limit reached\n");
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
