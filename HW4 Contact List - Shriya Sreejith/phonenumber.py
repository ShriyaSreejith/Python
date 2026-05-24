# PROG 1403 – Spring 2026
# HW4 – Contact List, Version 2
# Team: Lilly Ye, Aditi Shashidhara, and Shriya Sreejith
# Solution by Lilly Ye, Aditi Shashidhara, and Shriya Sreejith

class PhoneNumber:
    def __init__(self, raw):
        self.digits = self._clean(raw)
        if not self._validate(self.digits):
            raise ValueError("Invalid phone number: must be 10-15 digits")

    def _clean(self, raw):
        return ''.join(filter(str.isdigit, raw))

    def _validate(self, digits):
        return 10 <= len(digits) <= 15

    def formatted(self):
        if len(self.digits) == 10:
            country = "1"
            local = self.digits
        else:
            country = self.digits[:-10]
            local = self.digits[-10:]

        area = local[:3]
        first = local[3:6]
        last = local[6:]
        return f"+{country} ({area}) {first}-{last}"