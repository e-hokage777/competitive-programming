class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """

        if "@" not in s:
            return self.mask_phone(s)

        return self.mask_email(s)

    
    def mask_email(self, email):
        email = email.lower()
        name, rest = email.split("@")
        first_letter = name[0]
        last_letter = name[-1]

        masked_name = "".join([first_letter, "*****", last_letter])

        return masked_name + "@" + rest

    def mask_phone(self, number):
        digits = [char for char in number if char in "0123456789"]

        country_code = "*" * (len(digits) - 10)

        country_code = "+"  + country_code + "-" if country_code else ""

        return country_code + "***-***-" + "".join(digits[-4:])

        