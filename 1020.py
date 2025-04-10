idade = int(input())

def calc_id(a):
    if a < 30:
        print(f"""0 ano(s)
0 mes(es)
{a} dia(s)""")
    elif a > 30 and a < 365:
        print(f"""0 ano(s)
{a//30} mes(es)
{a%30} dia(s)""")
    else:
        print(f"""{a//365} ano(s)
{(a%365)//30} mes(es)
{(a%365)%30} dia(s)""")

calc_id(idade)