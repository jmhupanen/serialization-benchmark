# Serialization benchmark
This program serializes and de-serializes data and compares how different formats perform against each other on python. The tested formats 
are: Pickle, XML, JSON, MessagePack and YAML. The performance metrics are speed and serialized data size.

To run the benchmark, build the docker image and run the container. After that the results should be found in the working directory on the 
host. Speed results are in 'speed.png' and size results in 'size.png'.

## How to run
To build the image use command: ```docker build -t benchmark .```

To run the container use command: ```docker run -it --rm -v ${PWD}:/benchmark benchmark```

Note that if your host is running on Windows, you have to use PowerShell so that ```${PWD}``` is recognized.
