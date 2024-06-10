CC = g++
CFLAGS = -Wall -o
TARGETS = hw2_1 hw2_2 hw2_3 hw2_4 hw2_5 hw2_6

all: $(TARGETS)
hw2_1: hw2.1.cpp
	$(CC) $(CFLAGS) hw2.1 hw2.1.cpp
hw2_2: hw2.2.cpp
	$(CC) $(CFLAGS) hw2.2 hw2.2.cpp
hw2_3: hw2_3/testWindGauge.cpp hw2_3/WindGauge.h hw2_3/WindGauge.cpp
	$(CC) $(CFLAGS) hw2.3 hw2_3/testWindGauge.cpp hw2_3/WindGauge.cpp hw2_3/WindGauge.h
hw2_4: hw2.4.cpp
	$(CC) $(CFLAGS) hw2.4 hw2.4.cpp
hw2_5: hw2.5.cpp
	$(CC) $(CFLAGS) hw2.5 hw2.5.cpp
hw2_6: hw2.6.cpp
	$(CC) $(CFLAGS) hw2.6 hw2.6.cpp

clean:
	rm $(TARGETS)