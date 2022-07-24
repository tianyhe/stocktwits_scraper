# Stocktwits Most Recent Twits Scraper

Scrape the most recent messages of a query tag (e.g. ETH.X) from stocktwits.com.

Scraped messages details includes:

- The message ID
- The body of the message
- The timestamp of the message
- The user info of the sender
- The info of all tags in the message
- the sentiment tag of the message (if any)

Scraped user details includes:
- The associated message ID
- The sentiment tag of the message (if any)
- The user id
- The username
- The join date of the user
- The country of the user
- The number of followers of the user
- The number of following of the user
- The number of posts sent by the user
- The number of likes given by the user
- The watchlist count of the user
- The platform of the user (if any)

More details of the information will be stored as a json file for further parsing. 

---

## Output

All historical scraped data up to the new scrape time will be stored in two separate json files. - `./data/message.json` and `./data/user.json`
  * new scraped message data will be added to the 'message.json' file
  * new scraped user data will be added/updated to the 'user.json' file (no duplicates will be added)

The selected thumbnails will be stored in two separate csv files for further analysis. - `./data/message.csv` and `./data/user.csv`

Data from each scrape will be stored in the `./data/scrape_data` folder name by the scraped date.

The message details and the user details can be associated with the message ID.

### Example of the message json output file:

```json
[
  {
    "id": 469773959,
    "body": "$BTC.X $ETH.X something fishy is going on",
    "created_at": "2022-07-03T05:30:53Z",
    "user": {
      "id": 642622,
      "username": "TheMainCharacter",
      "name": "Andy Dufresne",
      "avatar_url": "https://avatars.stocktwits.com/production/642622/thumb-1620064587.png",
      "avatar_url_ssl": "https://avatars.stocktwits.com/production/642622/thumb-1620064587.png",
      "join_date": "2015-11-29",
      "official": false,
      "identity": "User",
      "classification": ["verified"],
      "home_country": "US",
      "search_country": "US",
      "followers": 55,
      "following": 118,
      "ideas": 4885,
      "watchlist_stocks_count": 28,
      "like_count": 1403,
      "plus_tier": "",
      "premium_room": "",
      "trade_app": false,
      "portfolio": "public",
      "portfolio_status": "public",
      "trade_status": null
    },
    "source": {
      "id": 1149,
      "title": "StockTwits for iOS",
      "url": "http://www.stocktwits.com/mobile"
    },
    "symbols": [
      {
        "id": 11418,
        "symbol": "BTC.X",
        "title": "Bitcoin BTC/USD",
        "aliases": ["BTCUSD"],
        "is_following": false,
        "watchlist_count": 493820,
        "has_pricing": true
      },
      {
        "id": 13016,
        "symbol": "ETH.X",
        "title": "Ethereum",
        "aliases": ["ETHUSD"],
        "is_following": false,
        "watchlist_count": 257068,
        "has_pricing": true
      }
    ],
    "mentioned_users": [],
    "entities": {
      "giphy": {
        "id": "uuGH77xktFciInXxOG",
        "ratio": 1.7740740740740741
      },
      "sentiment": {
        "basic": "Bearish"
      }
    }
  }
]
```

### Example of the user info json output file

```json
{
  "1037324": {
    "username": "StockTraderCapital",
    "join_date": "2017-04-24",
    "country": "US",
    "followers": 582,
    "following": 52,
    "posts_count": 35717,
    "likes_count": 14606,
    "watchlist_count": 32,
    "platform": "Android"
  },
  "1505519": {
    "username": "Billionaireclubcollc",
    "join_date": "2018-05-26",
    "country": "US",
    "followers": 8479,
    "following": 3,
    "posts_count": 169697,
    "likes_count": 21811,
    "watchlist_count": 296,
    "platform": "Web"
  },
  "3719725": {
    "username": "ThePoleTrader",
    "join_date": "2020-07-01",
    "country": "US",
    "followers": 11,
    "following": 16,
    "posts_count": 1756,
    "likes_count": 2448,
    "watchlist_count": 37,
    "platform": "iOS"
  }
}
```

### Example of csv output file:

#### Example of csv output file for the message details:

```csv
num,id,created_at,tag,username,likes,platform,body

0,472205476,2022-07-18T00:17:28Z,Bearish,EIon__Musk,5335932,5,Android,$SPY short this market with both hands  $BTC.X $ETH.X $NVDA

1,472205225,2022-07-18T00:13:42Z,NULL,Billionaireclubcollc,1505519,0,Web,"Lightspeed Venture Launches a Blockchain-Focused Team, Multicoin Capital Raises $430M https://www.billionaireclubcollc.com/lightspeed-venture-launches-a-blockchain-focused-team-multicoin-capital-raises-430m/ $BTC.X $ETC.X $ETH.X $DOGE.X $MITH.X"

2,472205020,2022-07-18T00:10:52Z,Bullish,staydowngetdown,5455336,0,iOS,$ETH.X yes sir!!!!!!
```

#### Example of csv output file for the user details:

```csv
num,message_id,tag,user_id,username,join_date,country,followers,following,posts_count,likes_counts,watchlist_counts,platform

0,472206234,NULL,1037324,StockTraderCapital,2017-04-24,US,582,52,35381,14481,31,Android

1,472205691,NULL,1505519,Billionaireclubcollc,2018-05-26,US,8449,3,167850,21811,296,Web

2,472205675,NULL,3719725,ThePoleTrader,2020-07-01,US,11,16,1755,2448,37,iOS
```


---

## Run Script

**Parameters for the scrape**
| Argument | type | note |
| ------------- | ------------- | ------------- |
| query_symbol | string | the tag to search for (e.g. "ETH.X", "BTC.X") |
| num_twits | int | the number of twits to scrape (default to 1000 entries of the most recent twits) |

---

## Updates
- 2022-07-03: Initial release
- 2022-07-18: Add the function to get the user characteristics
- 2022-07-24: Fix duplicate users in the user info output
- 2022-07-24: Add the function to store all historical data in json file

---

## Future Improvements

- Only support scraping the most recent twits on a single query tag at the moment
- possibly change to use API once its available (API now down for maintenance)
- Export database (probably after I take some classes on it)
