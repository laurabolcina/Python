# coding=utf-8
__author__ = "Laura Bolčina"

def percent_share(total, youth):
    result = youth / total * 100
    return result

def main():
    print percent_share(120, 30.0)
    print percent_share(250, 15.0)
    print percent_share(50, 35.0)

if __name__ == "__main__":
    main()