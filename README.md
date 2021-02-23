# coronavirus-tracker-api

<a href="https://www.buymeacoffee.com/mikedido" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/v2/default-green.png" alt="Buy Me A Coffee" width="217" height="60" ></a>


![python](https://img.shields.io/badge/v3.7-Python3-green)
![flask](https://img.shields.io/badge/v1.1-flask-green)


## About

An API to analysis data about the corona virus / COVID-19  by giving the number of deaths, confirmed, active and recovered person on the world. 

The app give a detailed information for each country from the JHU and INSEE resources.

## Screenshot


## Features
* __Data__: Shows the most recent data automatically.
* __Country__:
   * __information__ detailed information about the country (population, recovered, confirmed, ...deaths per million, recovered per million,...case fatality).
   * __provinces_list__ add province list of a country with the detailled information for each province.
   * __Confirmed chart__ for all countries.
   * __Deaths chart__ for all countries.
   * __Recovered chart__ for all country.
   * __Confirmed Histogramme__ the number of confirmed by day and by country
   * __Deaths Histogramme__ the number of deaths by day and by country
   * __Recovered Histogramme__ the number of recovered by day and by country 

## How to Use
#### Build from source code
```
1. Clone/Download the repo.
2. Install the requiremenet : `make install`
2. Execute & run! : `make run`
3. Visit your browser : http://localhost:5000
4. Enjoy ;)
```
#### Runing tests
```
make test
```

#### Runing linter
```
make lint
```

## TODO

* __Search__ for countries & cities.
* __Cities__ add détails of the cities.

 ## Data
 The data of coronavirus are retrieve from the api of the github project : https://github.com/ExpDev07/coronavirus-tracker-api

 This API used the data from : JHU - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).


## Contribute
Please feel free to contribute pull requests or create issues for bugs and feature requests.

## License
The API is available for personal/non-commercial use. It's not allowed to publish, distribute, or use the app in a commercial way.

## Author
Mahdi Gueffaz (mahdi.gueffaz@gmail.com)