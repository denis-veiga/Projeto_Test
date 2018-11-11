import json
from selenium import webdriver


class NextelTest:

    def search(self):
        browser = webdriver.Firefox()
        browser.get("http://www.google.com.br")
        my_dict = {}
        for i in self.json_response():
            if i == "Nextel":
                browser.find_element_by_id("lst-ib").send_keys(i)
                browser.find_element_by_name("btnK").click()
                flag = 1
                words = []
                while flag <= 3:
                    element = browser.find_element_by_css_selector("#rso > div:nth-child(5) > div > div:nth-child(" + str(flag) + ") > div > div > div.r > a > h3").text
                    words.append(element)
                    flag += 1
                my_dict["Nextel"] = words
            elif i == "telefonia do futuro":
                browser.find_element_by_id("lst-ib").send_keys(i)
                browser.find_element_by_name("btnK").click()
                flag = 1
                words_two = []
                while flag <= 3:
                    element = browser.find_element_by_css_selector("#rso > div:nth-child(1) > div > div:nth-child(" + str(flag) + ") > div > div > div.r > a > h3").text
                    words_two.append(element)
                    flag += 1
                my_dict["telefonia do futuro"] = words_two
            elif i == "selenium python":
                browser.find_element_by_id("lst-ib").send_keys(i)
                browser.find_element_by_name("btnK").click()
                flag = 1
                words_three = []
                while flag <= 3:
                    element = browser.find_element_by_css_selector("#rso > div:nth-child(1) > div > div:nth-child(" + str(flag) + ") > div > div > div.r > a:nth-child(1) > h3").text
                    words_three.append(element)
                    flag += 1
                my_dict["selenium python"] = words_three
            data = {}
            data["NextelTest"] = []
            data["NextelTest"].append(my_dict)
            dir = 'C:\\Users\\Denis\\Documents\\test'
            file_name = 'data.json'
            dir_file = dir + '\\' + file_name

            with open(dir_file, 'w') as outfile:
                json.dump(data, outfile)
            browser.get("http://www.google.com.br")
        print(my_dict)

    def json_response(self):
        with open('data.json') as data_file:
            data = json.load(data_file)
            array = []
            for i in data['google-me']:
                array.append(i)
            return array


if __name__=="__main__":
    run = NextelTest()
    run.search()
    run.json_response()


