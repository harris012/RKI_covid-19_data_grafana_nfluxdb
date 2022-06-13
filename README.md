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
- Open the UI of Node-RED to import the flow `nodered_flow.json` in order to run the Python script in it.





Visualise example of Covid Dashboard see below:
![Screenshot from 2022-06-13 02-12-17](https://user-images.githubusercontent.com/57041349/173259503-6ff00ae1-b5c2-4b24-b53f-fc625f69d5ea.png)

State and City can be selected by the variables on the pannel see Examples below
![Screenshot from 2022-06-13 02-06-06](https://user-images.githubusercontent.com/57041349/173259743-ab00b9b9-5148-46ae-97b6-6384a3f48d26.png) ![Screenshot from 2022-06-13 02-06-53](https://user-images.githubusercontent.com/57041349/173259748-56ba9943-576b-45c8-b163-96bf97300bde.png)

