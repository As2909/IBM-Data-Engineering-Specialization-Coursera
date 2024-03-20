## Project Description
In this project, you will act as a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like

- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city

More information about [tasks](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/Task.pdf)
### Objectives
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard

### Data
The Data Warehouse have to be designed to fit with the sample data below:\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/solid-waste-trips-new.png)\
Note that the Data Warehouse should be in snowflake schema for write-efficient.

## Tasks and Solutions
- Task 1: Design the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/1-MyDimDate.png)

- Task 2: Design the dimension table MyDimWaste (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/2-MyDimWaste.png)

- Task 3: Design the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/3-MyDimZone.png")

- Task 4: Design the fact table MyFactTrips (2 pts) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/4-MyFactTrips.png)

- Task 5: Create the dimension table MyDimDate (2 pts) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/5-MyDimDate.png)

- Task 6: Create the dimension table MyDimWaste  (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/6-MyDimWaste.png)

- Task 7: Create the dimension table MyDimZone (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/7-MyDimZone.png)

- Task 8: Create the fact table MyFactTrips (2 pts) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/8-MyFactTrips.png)

- Task 9: Load data into the dimension table DimDate (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/9-DimDate.png)\

- Task 10: Load data into the dimension table DimTruck (1 pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/10-DimTruck.png)\

- Task 11: Load data into the dimension table DimStation (1 pt)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/11-DimStation.png)\

- Task 12: Load data into the fact table FactTrips (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/12-FactTrips.png)\

- Task 13: Create a grouping sets query (2 pts) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/13-GroupingSets.png)

- Task 14: Create a rollup query (2 pts ) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/14-rollup.png)

- Task 15: Create a cube query using the columns year, city, station, average waste collected (2 pts ) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/15-cube.png)

- Task 16: Create an MQT named max_waste_per_station using the columns city, station, trucktype, max waste collected  (2 pts)\
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/16-mqt.png)

- Task 17: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/17-pie.png)

- Task 18: Create a bar chart in the dashboard (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/18-bar.png)

- Task 19: Create a line chart in the dashboard (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/19-line.png)

- Task 20: Create a pie chart in the dashboard (1 pt) \
![alt text](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/20-pie.png)

The full version of the dashboard is [here](https://github.com/As2909/IBM-Data-Engineering-Specialization-Coursera/blob/main/Course%2009%20Getting%20Started%20with%20Data%20Warehousing%20and%20BI%20Analytics/Week%204/Report.pdf)
