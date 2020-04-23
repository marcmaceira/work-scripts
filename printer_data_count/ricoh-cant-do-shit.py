import sys
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

# Set browser
driver = Chrome()

# Verify if printer IP argument was provided
try:
    sys.argv[1]
except IndexError:
    print("Printer IP was not provided")
else:
    printerIp = sys.argv[1]
    print("IP: %s" % printerIp)

# Verify if username argument was provided
try:
    sys.argv[2]
except IndexError:
    print("Username not provided")
else:
    username = sys.argv[2]
    print("Username: %s" % username)

# Verify if password argument was provided
try:
    sys.argv[3]
except IndexError:
    print("Password was not provided.\n")
else:
    password = sys.argv[3]
    print("Password: %s" % password)

# Points to Unification Counter for the given IP
url = "http://{}/web/guest/en/websys/status/getUnificationCounter.cgi".format(printerIp)
print(url)

# Open browser
driver.get(url)

# Wait 10 seconds for content to load
driver.implicitly_wait(10)

# Store values
totalOutput = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[4]").text
copierTotal = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[3]/tbody/tr/td[4]").text
printerTotal = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/table[3]/tbody/tr/td[2]/table[5]/tbody/tr/td[4]").text

print("Total: %s\nCopier Total: %s\nPrinter Total: %s\n" % (totalOutput, copierTotal, printerTotal))

# Close browser
driver.quit()
