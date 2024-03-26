import time
import json
import sys
from .utils import *
from collections import namedtuple
from pprintpp import pprint
from datetime import datetime


now = datetime.now()
date_time_format = now.strftime("%Y-%m-%d_%H-%M-%S")

# Badge = namedtuple('Badge', ['id', 'label', 'name'])
# JobListingRemoteConfig = namedtuple('JobListingRemoteConfig', ['id', 'kind'])
JobListingSearchResult = namedtuple(
    "JobListingSearchResult",
    [
        "typename",
        "atsSource",
        "autoPosted",
        "currentUserApplied",
        "description",
        "id",
        "jobType",
        "lastRespondedAt",
        "liveStartAt",
        "primaryRoleTitle",
        "remote",
        "reposted",
        "slug",
        "title",
        "compensation",
        "usesEstimatedSalary",
    ],
)
# StartupSearchResult = namedtuple('StartupSearchResult', ['id', 'startupId', 'name', 'companySize', 'highConcept', 'locationTaggings', 'logoUrl', 'highlightedJobListings', 'badges'])


class Companies:
    def __init__(self, query=[], **kwargs):
        self.query = query
        # self.companies = kwargs.get("companies", [])
        # self.data = self.get_companies()

    def make_companies_url(self, query):
        return

    def get_companies(self, query):
        # soup = BeautifulSoup(self.driver.page_source, "lxml")
        # pprint(soup.prettify())

        for i in range(1, 100):  # TODO: 100 pages, change this later
            # JavaScript code to execute a POST request
            js_script = (
                """
            var callback = arguments[0];
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'https://wellfound.com/graphql?fallbackAOR=talent', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.setRequestHeader('Accept', '*/*');
            xhr.setRequestHeader('Accept-Encoding', 'gzip, deflate, br, zstd');
            xhr.setRequestHeader('Accept-Language', 'en-US,en;q=0.9');
            xhr.setRequestHeader('Apollographql-Client-Name', 'talent-web');
            xhr.setRequestHeader('Origin', 'https://wellfound.com');
            xhr.setRequestHeader('Referer', 'https://wellfound.com/jobs');
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4) {
                    if (xhr.status == 200) {
                        callback(xhr.responseText);
                    } else {
                        console.error("Error with status code:", xhr.status);
                        callback("Error: " + xhr.statusText);
                    }
                }
            };
            xhr.send(JSON.stringify({
                "operationName": "JobSearchResultsX",
                "variables": {
                    "filterConfigurationInput": {
                    "page": """
                + str(i)
                + """,
                    "remoteCompanyLocationTagIds": [
                        "1692", 
                        "1693"
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
                    "keywords": [
                        "entry",
                        "junior",
                    ],
                    "excludedKeywords": [
                        "web3",
                        "crypto",
                        "cryptocurrency"
                    ],
                    "jobTypes": [
                        "full_time"
                    ],
                    "remotePreference": "NO_REMOTE", // "REMOTE_OPEN" or "NO_REMOTE"
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
            }));
            """
            )

            # Execute the JavaScript
            response = self.driver.execute_async_script(js_script)

            time.sleep(5)
            # pprint(response)

            # Parse the JSON response
            response = json.loads(response)

            # store to named tuples with the defined structure above for easy access

            job_listings = []
            startups = response["data"]["talent"]["jobSearchResults"]["startups"][
                "edges"
            ]
            for i in range(0, len(startups)):
                startup_info = startups[i]["node"]
                startup_job_listings = startup_info["highlightedJobListings"]
                # store to JobListingSearchResult named tuple
                # job_listings = [JobListingSearchResult(**job) for job in startup_job_listings]

                for job in startup_job_listings:
                    job_listings.append(
                        JobListingSearchResult(
                            job["__typename"],
                            job["atsSource"],
                            job["autoPosted"],
                            job["currentUserApplied"],
                            job["description"],
                            job["id"],
                            job["jobType"],
                            job["lastRespondedAt"],
                            job["liveStartAt"],
                            job["primaryRoleTitle"],
                            job["remote"],
                            job["reposted"],
                            job["slug"],
                            job["title"],
                            job["compensation"],
                            job["usesEstimatedSalary"],
                        )
                    )

            for job in job_listings:
                print(f"{job.title} | {job.compensation} | {job.id}")

            response_json = json.dumps(response, indent=4)

            # save the response to a file
            # with open(f"response_{date_time_format}.json", "w") as file:
            with open(f"response_{date_time_format}_page_{i}.json", "w") as file:
                print("writing to file...")
                file.write(response_json)

            has_next_page = response["data"]["talent"]["jobSearchResults"][
                "hasNextPage"
            ]
            # print("has_next_page:", has_next_page)
            if not has_next_page:
                break

        # time.sleep(10000)

        # save the soup to a file
        # with open(f"companies_{date_time_format}.html", "w") as file:
        #     print("writing to file...")
        #     file.write(soup.prettify())

        # print("sleeping for 10 seconds...")
        # time.sleep(10)
        for remaining in range(10, 0, -1):
            sys.stdout.write("\rsleeping in {:2d} seconds...".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rComplete!                       \n")

        # results = self._scrape_companies(soup)

        # return self.companies
