class Calories:

    @staticmethod
    def cacl_voz(age, weight, gender):
        result = 0
        if gender == 'man':
            if age <= 30:
                result = (0.063 * float(weight) + 2.896) * 240
            elif 31 <= age <= 60:
                result = (0.484 * float(weight) + 3.653) * 240
            elif age > 60:
                result = (0.491 * float(weight) + 2.459) * 240
        else:
            if age <= 30:
                result = (0.062 * float(weight) + 2.036) * 240
            elif 31 <= age <= 60:
                result = (0.034 * float(weight) + 3.538) * 240
            elif age > 60:
                result = (0.038 * float(weight) + 2.755) * 240
        return result

    @staticmethod
    def calc_harrison(gender, age, weight, height):
        if gender == 'man':
            result = (66.5 + (13.75 * float(weight)) + (5.003 * float(height)) - (6.775 * float(age)))
        else:
            result = (655.1 + (9.563 * float(weight)) + (1.85 * float(height)) - (4.676 * float(age)))
        return result

    @staticmethod
    def calc_mifflin(gender, age, weight, height):
        if gender == 'man':
            result = (10 * float(weight) + 6.25 * float(height) - 5 * int(age) + 5)
        else:
            result = (10 * float(weight) + 6.25 * float(height) - 5 * int(age) - 161)
        return result

