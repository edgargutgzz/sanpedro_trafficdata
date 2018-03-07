## Traffic in San Pedro 

This python script fetches data from several highways in the city using [Google Maps Distance Matrix API.](https://developers.google.com/maps/documentation/distance-matrix/)

**Installation**

1. Install Python 3.6 with [Anaconda.](https://www.anaconda.com/download)

**Setup**

1. Create a new environment and install the packages pandas and numpy.
	- conda create --name env_name pandas numpy

2. Install the Google Maps package.
	- conda install -c conda-forge googlemaps

3. Create a database file in the projects directory.
	- File name: "database_name.db"

4. Create the "routes" and "traffic" tables for "database_name.db".
	- Run "tables.py" inside the newly created environment. 

**Production**

1. Create the cron job that runs "traffic.py" every 10 minutes.
	- */10 * * * * cd /Users/user/projects_directory/ && /Users/user/anaconda3/envs/env_name/bin/python traffic.py 
