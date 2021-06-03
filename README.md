# covid-sync
These docker containers are configured to notify vaccine slot availability daily. 

## About 
This project uses apache airflow to schedule and run a defined workflow to hit the open APIs from [COWIN](https://apisetu.gov.in/public/marketplace/api/cowin). This then checks the availability of desired slots based on the age limit and district. Post which it sends an email notification regards the requested slots availability. 

### Airflow
[Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

### Docker
[Docker](https://www.docker.com/) is an open source containerization platform. Docker enables developers to package applications into containers—standardized executable components that combine application source code with all the operating system (OS) libraries and dependencies required to run the code in any environment.

## Getting started
Please install [Docker Desktop](https://www.docker.com/products/docker-desktop) if not already installed. 

Clone the repository and navigate into it. 
```sh
git clone https://github.com/AAbhishekReddy/covid-sync.git

cd covid-sync
```
> You can also download the ZIP file and extract the contents.

Configure your mail ID, district ID and Minimum age limit. 

File to be edited: /dags/covid_sync.py

```python
# ------------------ Enter Your email and your district ID here ------------------ #
email = "example@email.com"
district_id = "8"
min_age = 18
# ------------------------------------- end -------------------------------------- #
```
> The district ID can be referenced from the [district_ids.csv](./district_ids.csv)

Once that is done, lets spin up the containers. 

In your file path enter the following commands:

```sh
docker-compose up
```
> You can look into docker-compose commands [here](https://docs.docker.com/compose/).

If that is successful, it should start Apache airflow on port 8080.

You can open it at: http://localhost:8080 or http://127.0.0.1:8080

Now all you got to do is just turn on the workflow, in the following way:

![workflow-start][workflow_start]

[workflow_start]: ./dag-start.gif

Well, all set now and you should be receiving email notifications about the slot availability. But this would require the containers to be kept running all the time (yes thats a bummer!).

## References
- Airflow image and setup from [puckel/airflow](https://github.com/puckel/docker-airflow)
- District IDs CSV from [bhattbhaveh91](https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/district_mapping.csv)


