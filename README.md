# Green Feet

## Introduction
Commuting to and from work is important both from an environmental perspective and a health
perspective. Even before Covid-19 increasing longevity of the UK population meant that a healthy
lifestyle becomes more important. In the new Covid-19 world it is even more important to
organise transport and travel efficiently using information technology to it's full potential. 
It is an employer’s duty to act to safeguard their employees well being.

**The purpose of the app is therefore to give employers a simple way of appraising
which employees should be encouraged to use what type of transport to get to and from work**

In order for this to be measurable, it is possible to calculate an index uses variables like:

| Variable | explanation | mandatory | unit | range | weight
|:---|:---|:---:|:---:|:---:|---:|
| *PH* | postcode for home | Y | postcode |
| *PW* | postcode for workplace | Y | postcode |
| *C* | how critical to the organisation's business is this employee | N | subjective | ~0-100? | 1 |
| *N* | number of passengers | N |  people | ~0-100 | <1 |
| *S* | number of seats in vehicle |  N |seats | 0-10? |    <1 |
| *P* | does employee need to pick up dependants | N | boolean | 0-1 |    <1 |
| *DB* | does the employee have a disability | N | boolean | 0-1 |    <1 |

Giving a formula like so:

if `D = distance between *PH* and *PW*`

`D * (S / N) * (1 + P)`

### Example 1.
An employee that lives 4 km from workplace and drives his private car by himself to work and
doesn't need to pick up dependants. `4 km * (1 / 4) * (1+0) = 1`

### Example 2.
An employee that lives 16 km away, picks up two children from school.
`16 km * (3 / 4) * (1+1) = 12`

There are more variables that can be taken into account. Whether it is rush hour.
If the index is low then recommend green alternatives; cycling or bus, to using vehicle
(provided it's a fossil fuel vehicle), it is also possible to use park and ride.

## Functionality
This is most useful for large businesses, with 100+ employees where coordination can be tricky.

Such an employer could submit an excel sheet with a row per employee. 

### Required inputs

## Further reading
* [Government launches £2 billion bid to turn England into nation of cyclists and walkers
to reduce spread of coronavirus on public transport](https://www.standard.co.uk/news/uk/public-transport-coronavirus-grant-shapps-2-billion-a4436311.html)
* [Coronavirus: No 'single leap to freedom', minister warns](https://www.bbc.com/news/amp/uk-52600708)
* [Back to work: 'capacity of transport network will be down by 90%'](https://www.theguardian.com/world/2020/may/09/back-to-work-capacity-of-transport-network-will-be-down-by-90)
* [UK government unveils £2bn cycle and walk to work plan for COVID-19](https://www.youtube.com/watch?v=UlteeyvX-3g)

## Installation
$ pip install -U googlemaps

