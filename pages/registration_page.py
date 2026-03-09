from pygments.lexers import resource
from selene import have, command
from selene.support.shared import browser
import utils
from data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_gender(self, gender):
        if gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()

    def fill_hobbies(self, hobbies):
        if hobbies == "Sports":
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobbies == "Reading":
            browser.element('[for="hobbies-checkbox-2"]').click()
        elif hobbies == "Music":
            browser.element('[for="hobbies-checkbox-3"]').click()

    def fill_state(self, name):
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(f'{city}')
        ).click()

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        self.fill_gender(user.gender)
        browser.element('#userNumber').type(user.mobile)
        self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        browser.element('#subjectsInput').type(user.subject).press_enter()
        self.fill_hobbies(user.hobbies)
        browser.element('#uploadPicture').set_value(utils.path(user.picture))
        browser.element('#currentAddress').type(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.first_name + ' ' + user.last_name,
                user.email,
                user.gender.value,
                user.mobile,
                utils.format_date(user.year_of_birth, user.month_of_birth, user.day_of_birth),
                user.subject,
                user.hobbies.value,
                user.picture,
                user.address,
                user.state + ' ' + user.city,
            )
        )
