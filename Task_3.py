def main():
  '''
  Kodunuzu buraya yazin.
  '''
  reqem = int(input('Enter 4 digit number: '))
a = reqem//1000
b = reqem//100%10
c = reqem//10%10
d = reqem%10
cem = a+b+c+d
hasil = a*b*c*d
print(f'Digits: {a} {b} {c} {d}')
print(f'Sum of digits: {a}+{b}+{c}+{d}={cem}')
print(f'Product of digits: {a}*{b}*{c}*{d}={hasil}')

if __name__ == "__main__":
  main()
