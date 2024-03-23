# TODO

- [x] Implement Session Cookie Authentication Feature

  - Enable the scraper to use session cookies for authentication. The api will obtain a session cookie by logging into the wellfound website and then provide this cookie to the server. To avoid security measures like CAPTCHA and login blocks.
  Note that this was solved by options.add_argument("--user-data-dir=chrome-data") # save cookies

- [x] When logginng in, the api must check if the user is already logged in and if so, skip the login process.
- [ ] Create a way to check if the server is in captcha check page
 

&nbsp;
- [ ] Implement Proxy Support (?)

- [ ] Create urls for the api

- [ ] scrape

- [ ] Implement a way to log scraper server activity
