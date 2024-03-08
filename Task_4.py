def main():
  '''
  Kodunuzu buraya yazin.
  '''
  import math
sd1 = float(input("Side 1: "))
sd2 = float(input("Side 2: "))
sd3 = float(input("Side 3: "))
s = (sd1+sd2+sd3)/2
area = math.sqrt(s*(s-sd1)*(s-sd2)*(s-sd3))
print(f'Area of triangle: {area:.2f}')

if __name__ == "__main__":
  main()
