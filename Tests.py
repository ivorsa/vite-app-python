from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select    
import time

driver = webdriver.Chrome()
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # because of "Bluetooth: bluetooth_adapter_winrt.cc:1072 Getting Default Adapter failed" error
driver.maximize_window()
driver.implicitly_wait(3)
# test data
base_url="http://localhost:3000/"
keysBase = "Baseprice"
keys1 = "Alloy surcharge"
keys2 = "Scrap surcharge"
keys3 = "Internal surcharge"
keys4 = "External surcharge"
keys5 = "Storage surcharge"
keys5New = "T"
valueBase = 5
value1 = "2.15"
value1New = "1.79"
value2 = "3.14"
value2New = "-2.15"
value3 = "0.7658"
value4 = "1"
value5 = "0.3"

driver.get(base_url)
assert "Vite App" in driver.title
# test case 1
time.sleep(1)
baseLabel = driver.find_element_by_xpath('//*[@id="BasePrice"]/div[2]/span')
#baseCheckBtn = driver.find_element_by_id("base-trash-icon")
baseLabel.click()
driver.find_element_by_id("base-edit-icon").click()
baseValue = driver.find_element_by_id('base-value-input')
baseValue.send_keys(Keys.CONTROL + "a")
baseValue.send_keys(Keys.DELETE)
baseValue.send_keys(valueBase)
driver.find_element_by_id("base-check-icon").click()
# check sum
sumValue = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/span')
sumValueText = sumValue.text
valueBaseCheck = format(float(valueBase), '.2f')
assert sumValueText == valueBaseCheck, sumValueText + ' != ' + valueBaseCheck
print (keysBase + ' entered value: ' + valueBaseCheck + ' | Sum value: ' + sumValueText)

#test case 2
emptyLabelInput = driver.find_element_by_id("ghost-label-input")
emptyValueInput = driver.find_element_by_id("ghost-value-input")
emptyCheckIcon = driver.find_element_by_id("ghost-check-icon")
# add first component
emptyLabelInput.send_keys(Keys.CONTROL + "a")
emptyLabelInput.send_keys(Keys.DELETE)
emptyLabelInput.send_keys(keys1)
emptyValueInput.send_keys(value1)
emptyCheckIcon.click()
# check value 1
componentValues = driver.find_element_by_xpath('//*[text()="' + keys1 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value1), '.2f')
assert componentValueText == valueComponentCheck, componentValueText + ' != ' + valueComponentCheck
print (keys1 + ' entered value: ' + value1 + ' | Saved value: ' + str(valueComponentCheck))

# add second component
emptyLabelInput.send_keys(Keys.CONTROL + "a")
emptyLabelInput.send_keys(Keys.DELETE)
emptyLabelInput.send_keys(keys2)
emptyValueInput.send_keys(value2)
emptyCheckIcon.click()
# check value 2
componentValues = driver.find_element_by_xpath('//*[text()="' + keys2 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value2), '.2f')
assert componentValueText == valueComponentCheck, componentValueText + ' != ' + valueComponentCheck
print (keys2 + ' entered value: ' + value2 + ' | Saved value: ' + str(valueComponentCheck))

# add third component
emptyLabelInput.send_keys(Keys.CONTROL + "a")
emptyLabelInput.send_keys(Keys.DELETE)
emptyLabelInput.send_keys(keys3)
emptyValueInput.send_keys(value3)
emptyCheckIcon.click()
# check value 3
componentValues = driver.find_element_by_xpath('//*[text()="' + keys3 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value3), '.2f')
assert componentValueText == valueComponentCheck, componentValueText + ' != ' + valueComponentCheck
print (keys3 + ' entered value: ' + value3 + ' | Saved value: ' + str(valueComponentCheck))

# add forth component
emptyLabelInput.send_keys(Keys.CONTROL + "a")
emptyLabelInput.send_keys(Keys.DELETE)
emptyLabelInput.send_keys(keys4)
emptyValueInput.send_keys(value4)
emptyCheckIcon.click()
# check value 4
componentValues = driver.find_element_by_xpath('//*[text()="' + keys4 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value4), '.1f')
assert componentValueText == valueComponentCheck, componentValueText + ' != ' + valueComponentCheck
print (keys4 + ' entered value: ' + value4 + ' | Saved value: ' + str(valueComponentCheck))

# add fifth component
emptyLabelInput.send_keys(Keys.CONTROL + "a")
emptyLabelInput.send_keys(Keys.DELETE)
emptyLabelInput.send_keys(keys5)
emptyValueInput.send_keys(value5)
emptyCheckIcon.click()
# check value 5
componentValues = driver.find_element_by_xpath('//*[text()="' + keys5 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value5), '.1f')
assert componentValueText == valueComponentCheck, componentValueText + ' != ' + valueComponentCheck
print (keys5 + ' entered value: ' + value5 + ' | Saved value: ' + str(valueComponentCheck))

#check sum
sumValue2 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/span')
sumValueText2 = sumValue2.text
sumValue2 = format(float(valueBase), '.2f')
sumOfAllValues = float(valueBase) + float(value1) + float(value2) + float(value3) + float(value4) + float(value5)
sumOfAllValues2 = format(float(sumOfAllValues), '.2f')
print ('TC 2 - Sum of Elements: ' +  str(sumOfAllValues2) + ' | Sum value: ' + sumValueText2)

# test case 3
driver.find_element_by_xpath('//*[text()="' + keys3 + '"]').click()
driver.find_element_by_xpath("//span[contains(@id,'thrash-icon') and not(contains(@style,'display: none'))]").click()
sumValue3 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/span')
sumValueText3 = sumValue3.text
sumValue3 = format(float(valueBase), '.2f')
sumOfAllValues = float(valueBase) + float(value1) + float(value2)  + float(value4) + float(value5)
sumOfAllValues2 = format(float(sumOfAllValues), '.2f')
print ('TC 3 - Sum of Elements after deletetion of ' + keys3 +': ' +  str(sumOfAllValues2) + ' | Sum value: ' + sumValueText3)

# test case 4
driver.find_element_by_xpath('//*[text()="' + keys5 + '"]').click()
driver.find_element_by_xpath("//span[contains(@id,'edit-icon') and not(contains(@style,'display: none'))]").click()
labelInput5 = driver.find_element_by_xpath("//*[contains(@id,'label-input')]")
labelInput5.send_keys(Keys.CONTROL + "a")
labelInput5.send_keys(Keys.DELETE)
labelInput5.send_keys(keys5New)
#error message
errorMessage = driver.find_element_by_xpath('//*[text()=" This label is too short! "]')# if it does not find the element tests stop
errorMessageText = errorMessage.text
#assert errorMessage, 'element not displayed!' 
print('TC 4 - Error message: ' + errorMessageText)
driver.find_element_by_xpath("//span[contains(@id,'check-icon') and not(contains(@style,'display: none'))]").click()
# check label
labelText = driver.find_element_by_xpath('//*[text()="' + keys5 + '"]/parent::*/parent::*/div[2]/span')
labelText = labelText.text
print ('TC 4 - ' + keys5 + ' entered label: ' + keys5New + ' | Saved label: ' + labelText)

# test case 5
driver.find_element_by_xpath('//*[text()="' + keys2 + '"]').click()
driver.find_element_by_xpath("//span[contains(@id,'edit-icon') and not(contains(@style,'display: none'))]").click()
valueInput2 = driver.find_element_by_xpath("//*[contains(@id,'value-input')]")
valueInput2.send_keys(Keys.CONTROL + "a")
valueInput2.send_keys(Keys.DELETE)
valueInput2.send_keys(value2New)
#error message
errorMessage = driver.find_element_by_xpath('//*[text()=" Cannot be negative! "]')# if it does not find the element tests stop
errorMessageText = errorMessage.text
#assert errorMessage, 'element not displayed!' 
print('TC 5 - Error message: ' + errorMessageText)
driver.find_element_by_xpath("//span[contains(@id,'check-icon') and not(contains(@style,'display: none'))]").click()
componentValues = driver.find_element_by_xpath('//*[text()="' + keys4 + '"]/parent::*/parent::*/div[3]/div')
componentValueText = componentValues.text
valueComponentCheck = format(float(value4), '.1f')
# check value
valueText = driver.find_element_by_xpath('//*[text()="' + keys2 + '"]/parent::*/parent::*/div[3]/div')
valueText = valueText.text
print ('TC 5 - ' + keys2 + ' entered value: ' + value2New + ' | Saved value: ' + valueText)

# test case 6
driver.find_element_by_xpath('//*[text()="' + keys1 + '"]').click()
driver.find_element_by_xpath("//span[contains(@id,'edit-icon') and not(contains(@style,'display: none'))]").click()
valueInput5 = driver.find_element_by_xpath("//*[contains(@id,'value-input')]")
valueInput5.send_keys(Keys.CONTROL + "a")
valueInput5.send_keys(Keys.DELETE)
valueInput5.send_keys(value1New)
driver.find_element_by_xpath("//span[contains(@id,'check-icon') and not(contains(@style,'display: none'))]").click()
# check value
valueText = driver.find_element_by_xpath('//*[text()="' + keys1 + '"]/parent::*/parent::*/div[3]/div')
valueText = valueText.text
print ('TC 6 - Editing: '+ keys1 + ' entered value: ' + value1New + ' | Saved value: ' + valueText)
#check sum
sumValue2 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/span')
sumValueText2 = sumValue2.text
sumValue2 = format(float(valueBase), '.2f')
sumOfAllValues = float(valueBase) + float(value1New) + float(value2) + float(value4) + float(value5)
sumOfAllValues2 = format(float(sumOfAllValues), '.2f')
print ('TC 6 - Sum of Elements after editing of ' + keys1 + ' ' +  str(sumOfAllValues2) + ' | Sum value: ' + sumValueText2)

#time.sleep(2)
driver.close()