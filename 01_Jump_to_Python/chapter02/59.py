# coding: cp949
a="hobby"


print("find�� index�Լ��� ������ ��")

print(a.find('y'))
print("a.find('y')����Ϸ�")
if a.find('c'):print("���ϴ� ������� ����")
print("a.find('c'c)����Ϸ�")
print(a.index('y'))
print("a.index('c')����Ϸ�")

try:
    print(a.index('c'))
    print("a.index('c'))����Ϸ�")
except ValueError as e:
    print("���ϴ� ������� ����")
    print(e)


print("\n 12���� �������� 13���� ���Ĵ� �����")
