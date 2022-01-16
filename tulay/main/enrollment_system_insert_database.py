import mysql.connector
def enrollment_page_one_obj(
        self,
        student_status,
        last_name,
        first_name,
        middle_name,
        gender_result,
        date_of_birth,
        place_of_birth,
        nationality_value,
        religion_result,
        complete_address_line_one,
        complete_address_line_two,
        city_line_one,
        province_line_one,
        complete_address_line_one_completed,
        complete_address_line_two_completed,
        city_line_two_completed,
        province_line_two_completed,
        contact_number,
        email_address
        ):
        self.student_status  = student_status
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.gender_result = gender_result
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.nationality_value = nationality_value
        self.religion_result = religion_result
        self.complete_address_line_one = complete_address_line_one
        self.complete_address_line_two = complete_address_line_two
        self.city_line_one = city_line_one
        self.province_line_one = province_line_one
        self.complete_address_line_one_completed = complete_address_line_one_completed
        self.complete_address_line_two_completed = complete_address_line_two_completed
        self.city_line_two_completed = city_line_two_completed
        self.province_line_two_completed = province_line_two_completed
        self.contact_number = contact_number
        self.email_address = email_address
        return (student_status,
        last_name,
        first_name,
        middle_name,
        gender_result,
        date_of_birth,
        place_of_birth,
        nationality_value,
        religion_result,
        complete_address_line_one,
        complete_address_line_two,
        city_line_one,
        province_line_one,
        complete_address_line_one_completed,
        complete_address_line_two_completed,
        city_line_two_completed,
        province_line_two_completed,
        contact_number,
        email_address)
  