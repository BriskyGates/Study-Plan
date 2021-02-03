

class Company:
    """
    组合模式也叫作部分-整体模式，其定义如下：将对象组合成树形结构以表示“部分”和“整体”的层次结构，
    使得用户对单个对象和组合对象的使用具有一致性。  <无论是公司还是部分,都是利用抽象的Company 类实现>

    在该例中，公司结构抽象仅考虑公司（ConcreteCompany）和部门（Department），
    公司有子公司的可能性，公司也有自己的部门，部门是最终的叶子结点。

    可以简化介绍:
        每一个公司都有自己的组织结构，越是大型的企业，其组织结构就会越复杂。
        大多数情况下，公司喜欢用“树形”结构来组织复杂的公司部门关系和公司和子公司的结构关系。

    组合模式的缺点
        由于公司和部门直接使用了Company类，而不使用抽象类，这大大限制了接口的影响范围；若Company接口发生变更，对系统造成的风险会比较大。


    """
    name = ''

    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def listDuty(self):
        pass


class ConcreteCompany(Company):
    childrenCompany = None

    def __init__(self, name):
        Company.__init__(self, name)
        self.childrenCompany = []

    def add(self, company):  # 添加子公司
        self.childrenCompany.append(company)

    def remove(self, company):
        self.childrenCompany.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)  # 此时应该如何打印树状结构
        for component in self.childrenCompany:  # 子公司和母公司的层级多了一层
            component.display(depth + 1)

    def listDuty(self):
        for component in self.childrenCompany:  # 列举子公司的职责, 此处可能展示的是部门的职责
            component.listDuty()


class HRDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def listDuty(self):  # 履行职责
        print('%s\t Enrolling & Transfering management.' % self.name)


class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print("-" * depth + self.name)

    def listDuty(self):  # 履行职责
        print('%s\tFinance Management.' % self.name)


class RdDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):  # 层数咋还需要靠传入参数
        print("-" * depth + self.name)

    def listDuty(self):
        print("%s\tResearch & Development." % self.name)


if __name__ == "__main__":
    root = ConcreteCompany('HeadQuarter')
    # 添加总部的三个部门
    root.add(HRDepartment('HQ HR'))
    root.add(FinanceDepartment('HQ Finance'))
    root.add(RdDepartment("HQ R&D"))

    comp = ConcreteCompany('East Branch')
    comp.add(HRDepartment('East.Br HR'))
    comp.add(FinanceDepartment('East.Br Finance'))
    comp.add(RdDepartment("East.Br R&D"))
    root.add(comp)  # 把当前分公司添加入总部

    comp1 = ConcreteCompany('Northast Branch')
    comp1.add(HRDepartment('Northeast.Br HR'))
    comp1.add(FinanceDepartment('Northeast.Br Finance'))
    comp1.add(RdDepartment("Northeast.Br R&D"))
    comp.add(comp1)

    comp2 = ConcreteCompany('Southeast Branch')
    comp2.add(HRDepartment('Southeast.Br HR'))
    comp2.add(FinanceDepartment('Southeast.Br Finance'))
    comp2.add(RdDepartment("Southeast.Br R&D"))
    comp.add(comp2)

    root.display(1)

    root.listDuty()
