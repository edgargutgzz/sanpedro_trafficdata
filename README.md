## Traffic in San Pedro, México

This python script fetches traffic data (distance, duration in traffic) from several highways in the city using [Google Maps Distance Matrix API.](https://developers.google.com/maps/documentation/distance-matrix/) 

**Installation**

1. Install Python 3.6 with [Anaconda.](https://www.anaconda.com/download)
	- Anaconda will automatically install several packages along with python.
	- You can see the packages installed running "conda list"

**Setup**

You can create different environments with Conda in order to work with different python versions or install different packages. To run this script we'll first create a new environment. You can see the environments currently created running "conda info --envs"

1. Create a new environment called "env_name" and install the packages pandas and numpy.
	- Run "conda create --name env_name pandas numpy"

Make sure you are working on the newly created environment for the remaining steps. Run "conda info --envs" and look for the asterisk beside the enviroment name. 

2. Install the Google Maps package.
	- conda install -c conda-forge googlemaps

3. Create an sqlite3 database with two tables in it, "routes" and "traffic". 
	- SQlite is one of the packages previously installed with Anaconda.
	- Run "python tables.py".

**Production**

1. Create the cron job that runs "traffic.py" every 10 minutes.
	- Run "crontab -e"
	- Insert the following cronjob:
		*/10 * * * * cd /Users/user/projects_directory/ && /Users/user/anaconda3/envs/env_name/bin/python traffic.py 
	- To make sure the cron job was created you can run "crontab -l".
