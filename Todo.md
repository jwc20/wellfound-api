# TODO

- [x] Implement Session Cookie Authentication Feature
    - this was solved by options.add_argument("--user-data-dir=chrome-data") # save cookies

- [x] When logginng in, the api must check if the user is already logged in and if so, skip the login process.

~~- [ ] Create a way to check if the server is in captcha check page - Refactor Login class - [ ] cover all possible cases of captcha check and login~~

- [x] Create custom query method to send as javascript post request script 

- [x] Find a way to get multiple pages of data (infini scroll)

- [ ] Implement proxy server when logging in

- [ ] Store response data in namedtuples
    - [ ] Badge 
    - [ ] JobListingRemoteConfig
    - [x] JobListingSearchResult
    - [ ] StartupSearchResult

&nbsp;

- [ ] Implement Proxy Support (?)

- [ ] Create urls for the api

- [ ] Implement a way to log scraper server activity

- [ ] Make it into an actual api
