# Covid-19 data from RKI Visualisation with grafana influxdb & Node-Red

## Basic Concept

![image](https://user-images.githubusercontent.com/57041349/176417595-d5e1d4e4-8376-49a1-9642-15d89f2eaba7.png)

As a big fan of containerised applications, I decided to fetch the latest covid api data from [RKI (Robert Koch Institute) website](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0/api). Fetch api data from [Python](https://www.python.org/) and automate the script in the [Node-RED](https://nodered.org/) to fetch the latest data every day at 3:00 am.
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
- Open the UI of Node-RED to import the flow  from the file `nodered_flow.json` in order to run the Python script in it.
- See Example below:![Screenshot from 2022-06-13 02-29-33](https://user-images.githubusercontent.com/57041349/173260178-8deead4c-621d-4b85-8693-a27a388ab178.png)

- Import the grafana dashboard model from the file `grafana_dashboard_model.json` in the grafana UI.
- Visualisation example of Covid Dashboard see below:
![Screenshot from 2022-06-13 02-12-17](https://user-images.githubusercontent.com/57041349/173259503-6ff00ae1-b5c2-4b24-b53f-fc625f69d5ea.png)



## Demo
![vid1](https://user-images.githubusercontent.com/57041349/175115171-01493555-8989-4802-a612-effe40a5511a.gif)



