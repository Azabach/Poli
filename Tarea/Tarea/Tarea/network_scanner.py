from greynoise import GreyNoise
api_client = GreyNoise(api_key=<api_key>, timeout=<timeout_in_seconds>)

api_client.ip('58.220.219.247')
{
  "ip": "58.220.219.247",
  "seen": true,
  "classification": "malicious",
  "first_seen": "2019-04-04",
  "last_seen": "2019-08-21",
  "actor": "unknown",
  "tags": [
    "MSSQL Bruteforcer",
    "MSSQL Scanner",
    "RDP Scanner"
  ],
  "metadata": {
    "country": "China",
    "country_code": "CN",
    "city": "Kunshan",
    "organization": "CHINANET jiangsu province network",
    "asn": "AS4134",
    "tor": false,
    "os": "Windows 7/8",
    "category": "isp"
  },
  "raw_data": {
    "scan": [
      {
        "port": 1433,
        "protocol": "TCP"
      },
      {
        "port": 3389,
        "protocol": "TCP"
      },
      {
        "port": 65529,
        "protocol": "TCP"
      }
    ],
    "web": {
      "paths": [],
      "useragents": []
    },
    "ja3": []
  }