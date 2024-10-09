# Compiler
CC = gcc

# Source files
SRC = algorithm.c

# Output executable
OUTPUT = AlgorithmAPP

# Include and library paths
INCLUDE_PATH = /usr/include
LIB_PATH = /usr/lib

# Libraries
LIBS = -lrdkafka -lcjson

# Compile
$(OUTPUT): $(SRC)
	$(CC) -o $(OUTPUT) $(SRC) -I$(INCLUDE_PATH) -L$(LIB_PATH) $(LIBS)

# Clean up
clean:
	rm -f $(OUTPUT)
