# PlaywrightPython

* https://journaldev.com/14036/python-data-types  -> Follow this to learn for more python data types
* Download PyCharm : https://www.jetbrains.com/pycharm/download/?section=mac

* To run any file in PcCharm tool -> Right click on file -> Select Run,
                                  -> If MAC user -> ctrl + Shift + R 
                                         -> Use the above command in blank line to run all methods
                                         -> If used above command on lone where code is written then it will run that particular
                                            method only
                                  -> pytest "filename" ---> pytest test_PyTestValidation.py -> command to run a partivular test file
                                  -> pytest "filename"::"methodName" ---> pytest test_PyTestValidation.py::test_initialCheck2
                                  -> pytest "filename"::"methodName" ---> pytest test_PyTestValidation.py::test_initialCheck2 -s -> provides log also
* Download python : https://www.python.org/downloads/
* Unlike java in class, methods here braces are not used to specifying scope instead indentation are determined. Refer Class.py
* Open terminal -> give command -> pytest -s -> This will run all pytests under pytest folder
* Add lanchain, pytest, openai, ragas, ragas in Pythn Interpreter

* * If tests are present in another directory then move to that directory first from terminal -> cd directory/folder name I.e cd playwright -> then give command to run the test  -> pytest test_playwrightBasics.py::test_playwrightShortCut - -headed
* pip3 install pytest-playwright   -> Command to download pytest playwright
* https://playwright.dev/python/docs/intro
* https://pypi.org/project/pytest-html/
* pip3 install pytest-html  —> Command to install html report
* pytest -n 3 - -html=report.html -> A report.html file will be created on project label
* https://playwright.dev/docs/trace-viewer  -> For taking screenshots 
* pytest - -browser_name chrome -n 3 - -tracing on - -html=report.html  -> Running test on chrome in parallel, logging report 
* playwright codegen https://rahulshettyacademy.com/loginpagePractise/   -> command from terminal, which will generate the code and will show the locators after the url is launched 
* pytest “fileName.py” - -browser_name firefox 
* pytest -k web_api  —> This command runs all the pytests which include web_api as it’s name I.e  def test_e2e_web_api(playwright:Playwright)
* pytest -m smoke —> This command runs all the pytests which include smoke as tag name I.e @pytest.mark.smoke
* pip3 install pytest-xdist -> For installing the pytest-xdist
* pytest-xdist —> The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution:
* pytest -n 3 -> n, stands for no of threads it want to open parallel
* pytest - -browser_name chrome -n 3 - -tracing on - -html=report.html  -> Running test on chrome in parallel, logging report   -> In this case project is present in path '/Users/abinash/Documents/Personal/Code Worspace/Playwright/PytestPython'    -> So inn MAC IntelliJ terminal first move inside project by giving command cd playwright    -> Then give the above command to execute the script    -> Refer the image below for reference    ￼
* https://trace.playwright.dev  -> Upload the zip file in test-results folder I.e '/Users/abinash/Documents/Personal/Code Worspace/Playwright/PytestPython/playwright/test-results/test-morevalidations-py-test-uichecks-chromium/trace.zip' 
* pip3 install pytest-bdd
