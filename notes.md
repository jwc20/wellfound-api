- Use id to get the job url


Request url (post request)
- https://wellfound.com/graphql?fallbackAOR=talent


Request payload:

```
{
  "operationName": "JobSearchResultsX",
  "variables": {
    "filterConfigurationInput": {
      "page": 1,
      "locationTagIds": [
        "1693"
      ],
      "remoteCompanyLocationTagIds": [
        "1665"
      ],
      "roleTagIds": [
        "14726"
      ],
      "skillTagIds": [
        "14775",
        "139914",
        "17000"
      ],
      "equity": {
        "min": null,
        "max": null
      },
      "excludedKeywords": [
        "web3",
        "crypto",
        "cryptocurrency"
      ],
      "jobTypes": [
        "full_time"
      ],
      "keywords": [
        "entry",
        "junior"
      ],
      "remotePreference": "NO_REMOTE",
      "salary": {
        "min": null,
        "max": null
      },
      "yearsExperience": {
        "max": 2,
        "min": null
      }
    }
  },
  "extensions": {
    "operationId": "tfe/b898ee628dd3385e1b8c467e464a0261ad66c478eda6e21e10566b0ca4ccf1e9"
  }
}
```





