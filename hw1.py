class Home:
    def new(self, int_number):
        try:
            int_number = int(int_number)
            print(f'{int_number} - введенное целое число!')
        except ValueError:
            print('ValueError!')

num = Home()
num.new(789)
num.new('какое то слово')