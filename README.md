# Covid-19 data from RKI Visualisation with grafana influxdb & Node-Red

As a big fan of containerised applications, I decided to fetch the latest covid api data from [RKI website](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0/api). Fetch api data from [Python](https://www.python.org/) and automate the script in the [Node-RED](https://nodered.org/) to fetch the latest data every day at 3:00 am.
Save it to [influxdb](https://www.influxdata.com/) and visualise it in the [Grafana](https://grafana.com/) dashboard.

## Installation Requirements
- [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) should be installed on the system.

## Steps to run the docker containers
- From the root of this repo you will find the file name `docker-compose.yml`. Edit this file according to your requirements and run on the host.
```
Example:
docker-compose pull
docker-compose up -d
```
- Check if the all the containers are running by executing `docker ps`.
- Open the UI of Node-RED to import the flows and run the Python script in it.
