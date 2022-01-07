# Store RESTAPI WAL

## Description

The application run two APIs:

- Store
- Point of Interest

### Store

The **Store Model** capture the attibutes of a store using the following structure:

```
id = models.AutoField(primary_key=True)
name = models.CharField(max_length=255)
address = models.CharField(max_length=255)
city = models.CharField(max_length=100)
postcode = models.IntegerField()
geom = models.PointField()
```

### POINT OF INTEREST

The **POI Model** capture the attibutes of a point of interest using the following structure:

```
id = models.AutoField(primary_key=True)
name = models.CharField(max_length=255)
bussines_status = models.CharField(max_length=255)
rate = models.CharField(max_length=100)
type = models.CharField(max_length=100)
geom = models.PointField()
distance= models.DecimalField(max_digits=10,decimal_places=2)
store = models.ForeignKey(Store, on_delete=models.CASCADE)
```

This model is feeded once a new store is added. The application make a _Nearby search_ using **google place API**

## Docker Setup

The application is config to be run in the Docker container

```
docker-compose build --no-cache
docker-compose up
```

this will build and create the docker containers for the Postgres Application and Django Application

## Issues

#### Migrations

WHen it comes to rest_api migrations is always tricky. Here some commands are useful in this application in case the models and structure are change:

```
# Delete all the migrations
docker-compose exec web python manage.py migrate store zero

# Show all the migrations made
docker-compose exec web python manage.py showmigrations

# Make and migrate the changes
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

As an additional step, it might be useful to delete the migrations files on the migration folder

#### Env Variables

As the application use Google Place API, a token is required. This key can be setup in your local enviroment using:

```
export ggl_place_key={SECRET_KEY}
```

For this project the variable is set in docker under:

```
ENV ggl_place_key={SECRET_KEY}
```

and use in use in `store/store_seeker.py` file on line 16 and 17:

```
secret_key = os.getenv("ggl_place_key")  # secret key
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&key={secret_key}"
```

## Examples

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data-raw $'{\n    "name": "La Tienda 2",\n    "address": "Steinfurter str. 2",\n    "city": "Berlin",\n    "postcode": 49562,\n    "geom": "POINT(151.1957362 -33.8670522)"\n}'\
  http://localhost:8000/store/
```

**Body**

```
{
    "name": "La Tienda 2",
    "address": "Steinfurter str. 2",
    "city": "Berlin",
    "postcode": 49562,
    "geom": "POINT(151.1957362 -33.8670522)"
}
```

## Test

To run some test just excecute:

```
docker-compose exec web python manage.py test
```
