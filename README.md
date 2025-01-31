## Prerequirements

* Make sure that python3, Chrome browser, and Firefox browser are installed on your computer
* Being in the root directory of the project, in your Terminal app, execute the following command to set up necessary python packages:

```
pip3 install -r requirements.txt
```

* On macOS, install Allure for better reporting:

```
brew install allure
```

* To work properly, the tests also require the **credentials.txt** file to be put in the root directory of the test project. It must contain the following data in JSON format:

```
{
  "email": "%your_valid_email%",
  "password": "%your_valid_password%"
}
```

where **%your_valid_email%** and **%your_valid_password%** must be replaced with actual valid email and password that will be used to login to Hudl.

## How to run tests

1. If everything is set up correctly, you can run the tests, generate and check Allure report. To do it, in the root directory of the project execute the following command:
```
pytest --alluredir=allure-results && allure serve allure-results
```

2. If you decided to go without Allure, then from the root directory of the project just run the plain python tests only:
```
pytest
```

3. By default, tests are run using Chrome browser. You can specify the browser in the command line option:
```
pytest --browser=chrome
pytest --browser=firefox
```
