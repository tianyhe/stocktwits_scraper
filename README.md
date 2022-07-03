# Stocktwits Most Recent Twits Scraper

Scrape the most recent messages of a query tag (e.g. ETH.X) from stocktwits.com.

Scraped messages details includes:

- The message ID
- The body of the message
- The timestamp of the message
- The user info of the sender
- The info of all tags in the message
- the sentiment tag of the message (if any)

More details of the information will be stored as a json file for further parsing. The selected thumbnails will be stored in a csv file for further analysis.

---

## Output

**Example of json out file:**

```
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
        "classification": [
            "verified"
        ],
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
            "aliases": [
                "BTCUSD"
            ],
            "is_following": false,
            "watchlist_count": 493820,
            "has_pricing": true
        },
        {
            "id": 13016,
            "symbol": "ETH.X",
            "title": "Ethereum",
            "aliases": [
                "ETHUSD"
            ],
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
},
...
```

**Example of csv output file:**

```
num,id,created_at,username,tag,body

0,469773959,2022-07-03T05:30:53Z,Bearish,TheMainCharacter,$BTC.X $ETH.X something fishy is going on

1,469773887,2022-07-03T05:28:41Z,Bullish,james2344,today bullish market $ETH.X

2,469773863,2022-07-03T05:28:09Z,NULL,OptionsTrigger,$BTC.X how did this 15 min candle close green!!! Lmao. Brokers really wanted to trigger all the leveraged SLs. Crypto TA is a myth.  $ETH.X $SOL.X


...
```

---

## Script

**Parameters for the scrape**
| Argument | type | note |
| ------------- | ------------- | ------------- |
| query_symbol | string | the tag to search for (e.g. "ETH.X", "BTC.X") |
| num_twits | int | the number of twits to scrape (default to 1000 entries of the most recent twits) |

---

## Future Improvements

- Only support scraping the most recent twits on a single query tag at the moment
- possibly change to use API once its available (API now down for maintenance)
- Export database (probably after I take some classes on it)
