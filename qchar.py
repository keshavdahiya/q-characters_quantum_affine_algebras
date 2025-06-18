class node:
   def __init__(self, num, sub, sup):
      self.num = num
      self.sub = sub
      self.sup = sup
   def __str__ (self):
      if self.sup == 0:
         return f""
      elif self.sup == 1:
         return f"\\mr{{{self.num}}}_{{{self.sub}}}"
      else:
         return f"\\mr{{{self.num}}}_{{{self.sub}}}^{{{self.sup}}}"

class monomial:
   def __init__ (self, nodes):
      self.nodes = [] 
      for x in nodes:
         self.nodes.append(node(x.num,x.sub,x.sup))
   def __str__ (self):
      out = ''
      boo = True
      for x in self.nodes:
         out = out + str(x)
         if x.sup !=0:
            boo = False
      if boo:
         out = "1"
      return out

class term:
   def __init__ (self, coeff, monom):
      self.coeff = coeff
      self.monom = monomial(monom.nodes)
   def __str__ (self):
      if abs(self.coeff) == 1:
         out = str(self.monom)
      else:
         out = str(abs(self.coeff)) + '.' + str(self.monom)
      return out

class qterm:
   def __init__ (self, ter, col, num):
      self.term = term(ter.coeff, ter.monom)
      self.color = []
      for x in col:
         self.color.append(x)
      self.level = num
   def __str__ (self):
      out = str(self.term) + ' ['
      for x in self.color:
         out = out + str(x) + ' '
      out = out + '] ' + str(self.level)
      return out

class polynomial:
   def __init__ (self, terms):
      self.terms = []
      for x in terms:
         self.terms.append(term(x.coeff, x.monom))
   def __str__ (self):
      if len(self.terms) == 0:
         return ''
      x = self.terms[0]
      if x.coeff < 0:
         out = '-' + str(x)
      else:
         out = str(x)
      for x in self.terms[1:]:
         if x.coeff < 0:
            out = out + ' - ' + str(x)
         else:
            out = out + ' + ' + str(x)
      return out

def lie (s):
   li = []
   if s == 'A2':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1)]))
   if s == 'A3':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1)]))
   if s == 'A4':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1)]))
   if s == 'B2':
      li.append(monomial([node(1,2,1),node(1,-2,1),node(2,1,-1),node(2,-1,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1)]))
   if s == 'B3':
      li.append(monomial([node(1,2,1),node(1,-2,1),node(2,0,-1)]))
      li.append(monomial([node(2,2,1),node(2,-2,1),node(1,0,-1),node(3,1,-1),node(3,-1,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1)]))
   if s == 'B4':
      li.append(monomial([node(1,2,1),node(1,-2,1),node(2,0,-1)]))
      li.append(monomial([node(2,2,1),node(2,-2,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,2,1),node(3,-2,1),node(2,0,-1),node(4,1,-1),node(4,-1,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1)]))
   if s == 'B5':
      li.append(monomial([node(1,2,1),node(1,-2,1),node(2,0,-1)]))
      li.append(monomial([node(2,2,1),node(2,-2,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,2,1),node(3,-2,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,2,1),node(4,-2,1),node(3,0,-1),node(5,1,-1),node(5,-1,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1)]))
   if s == 'C2':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,2,1),node(2,-2,1),node(1,1,-1),node(1,-1,-1)]))
   if s == 'C3':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,2,1),node(3,-2,1),node(2,1,-1),node(2,-1,-1)]))
   if s == 'C4':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,2,1),node(4,-2,1),node(3,1,-1),node(3,-1,-1)]))
   if s == 'C5':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1)]))
      li.append(monomial([node(5,2,1),node(5,-2,1),node(4,1,-1),node(4,-1,-1)]))
   if s == 'D4':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1),node(4,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(2,0,-1)]))
   if s == 'D5':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1),node(5,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(3,0,-1)]))
   if s == 'D6':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1),node(6,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1)]))
      li.append(monomial([node(6,1,1),node(6,-1,1),node(4,0,-1)]))
   if s == 'D7':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1),node(6,0,-1),node(7,0,-1)]))
      li.append(monomial([node(6,1,1),node(6,-1,1),node(5,0,-1)]))
      li.append(monomial([node(7,1,1),node(7,-1,1),node(5,0,-1)]))
   if s == 'E6':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1),node(6,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1)]))
      li.append(monomial([node(6,1,1),node(6,-1,1),node(3,0,-1)]))
   if s == 'E7':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1),node(7,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1),node(6,0,-1)]))
      li.append(monomial([node(6,1,1),node(6,-1,1),node(5,0,-1)]))
      li.append(monomial([node(7,1,1),node(7,-1,1),node(4,0,-1)]))
   if s == 'E8':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,1,1),node(3,-1,1),node(2,0,-1),node(4,0,-1)]))
      li.append(monomial([node(4,1,1),node(4,-1,1),node(3,0,-1),node(5,0,-1)]))
      li.append(monomial([node(5,1,1),node(5,-1,1),node(4,0,-1),node(6,0,-1),node(8,0,-1)]))
      li.append(monomial([node(6,1,1),node(6,-1,1),node(5,0,-1),node(7,0,-1)]))
      li.append(monomial([node(7,1,1),node(7,-1,1),node(6,0,-1)]))
      li.append(monomial([node(8,1,1),node(8,-1,1),node(5,0,-1)]))
   if s == 'F4':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,1,1),node(2,-1,1),node(1,0,-1),node(3,0,-1)]))
      li.append(monomial([node(3,2,1),node(3,-2,1),node(2,1,-1),node(2,-1,-1),node(4,0,-1)]))
      li.append(monomial([node(4,2,1),node(4,-2,1),node(3,0,-1)]))
   if s == 'G2':
      li.append(monomial([node(1,1,1),node(1,-1,1),node(2,0,-1)]))
      li.append(monomial([node(2,3,1),node(2,-3,1),node(1,2,-1),node(1,0,-1),node(1,-2,-1)]))
   return li

def sortkey (n):
   if n.sup < 0:
      return 10000*n.num+n.sub-1000
   return 10000*n.num+n.sub

def levelsort(q):
   return q.level

def shift (mono, n):
   m = monomial(mono.nodes)
   for x in m.nodes:
      x.sub = x.sub + n
   return m

def weight (mono, n):
   w = []
   i = 0
   while i< n:
      w.append(0)
   for x in mono.nodes:
      w[x.num-1] = w[x.num-1] + x.sup
   return w

def div (m1, m2):
   m = []
   cancel = []
   for x in m1.nodes:
      boo = True
      for y in m2.nodes:
         if x.num == y.num and x.sub == y.sub:
            if x.sup != y.sup:
               m.append(node(x.num, x.sub, x.sup-y.sup))
            cancel.append(m2.nodes.index(y))
            boo = False
      if boo:
         m.append(node(x.num, x.sub, x.sup))
   for y in m2.nodes:
      boo = True
      for i in cancel:
         if m2.nodes.index(y) == i:
            boo = False
      if boo:
         m.append(node(y.num, y.sub, -y.sup))
   m.sort(key = sortkey)
   return monomial(m)

def dominant (mono, li):
   length = {}
   for x in li:
      length.update({x.nodes[0].num:x.nodes[0].sub-x.nodes[1].sub})
   m = []
   for x in mono.nodes:
      if x.sup > 0:
         m.append(x)
   mm = monomial(m)
   doms = []
   while len(mm.nodes) != 0:
      dom = []
      i = 0
      x = mm.nodes[i]
      dom.append(x)
      i = i + 1
      if i < len(mm.nodes):
         y = mm.nodes[i]
      while i < len(mm.nodes) and y.num == x.num:
         if y.sub == x.sub + length[y.num]:
            dom.append(y)
            x = y
         i = i + 1
         if i < len(mm.nodes):
            y = mm.nodes[i]
      doms.append(monomial(dom))
      mm = div (mm, monomial(dom))
   return doms

def square (mono):
   boo = False
   for x in mono.nodes:
      if x.sup > 1 or x.sup < -1:
         boo = True
   return boo

def perfectsq (mono):
   boo = True
   for x in mono.nodes:
      if abs(x.sup) < 2:
         boo = False
   return boo

def sqfreedom (mono, li):
   out = []
   m = monomial([])
   for x in mono.nodes:
      m.nodes.append(node(x.num,x.sub,1))
   out.append(m)
   m = div(mono, m)
   doms = dominant (m, li)
   while len(doms) != 0:
      m = monomial([])
      for x in doms[0].nodes:
         m.nodes.append(node(x.num,x.sub,1))
      out.append(m)
      m = div(doms[0], m)
      temp = dominant(m, li)
      for x in temp:
         doms.append(x)
      doms.pop(0)
   return out

def length (poly):
   n = 0
   for x in poly.terms:
      n = n + x.coeff
   return n

def check (mono, poly):
   for x in poly.terms:
      y = div (mono, x.monom)
      boo = True
      for z in y.nodes:
         if z.sup != 0:
            boo = False
      if boo:
         return poly.terms.index(x)
   return -1

def mult (p1, p2):
   p = polynomial([])
   for x in p1.terms:
      for y in p2.terms:
         m  = monomial(y.monom.nodes)
         for i in m.nodes:
            i.sup = -i.sup
         t = div(x.monom, m)
         i = check(t, p)
         if i >= 0:
            p.terms[i].coeff += x.coeff*y.coeff
         else:
            p.terms.append(term(x.coeff*y.coeff, t))
   return p

def sub (p1, p2):
   p = polynomial(p1.terms)
   for x in p2.terms:
      i = check(x.monom, p)
      if i < 0:
         p.terms.append(term(-x.coeff, x.monom))
      else:
         if p.terms[i].coeff == x.coeff:
            p.terms.pop(i)
         else:
            p.terms[i].coeff -= x.coeff
   return p

def add (p1, p2):
   t = polynomial(p2.terms)
   for x in t.terms:
      x.coeff = -x.coeff
   return sub(p1, t)

def squares (poly):
   sq = 0
   for x in poly.terms:
      if square(x.monom):
         sq = sq + 1
   return sq

def qchardom (qm, li):
   qout = [qterm(qm.term, qm.color, qm.level)]
   x = monomial(qm.term.monom.nodes)
   mono = monomial(qm.term.monom.nodes)
   l = qm.level
   while len(x.nodes) != 0:
      nod = x.nodes[-1]
      sft = nod.sub-li[nod.num-1].nodes[1].sub
      mono = div(mono, shift(li[nod.num-1], sft))
      l = l + 1
      qout.append(qterm(term(1,mono), [], l))
      x.nodes.pop()
   return qout

def qmult(qp1, qp2):
   qp = []
   p = polynomial([])
   for x in qp1:
      for y in qp2:
         m  = monomial(y.term.monom.nodes)
         for i in m.nodes:
            i.sup = -i.sup
         t = div(x.term.monom, m)
         i = check(t, p)
         if i >= 0:
            p.terms[i].coeff += x.term.coeff*y.term.coeff
            qp[i].term.coeff += x.term.coeff*y.term.coeff
         else:
            p.terms.append(term(x.term.coeff*y.term.coeff, t))
            qp.append(qterm(term(x.term.coeff*y.term.coeff,t),[],x.level+y.level))
   return qp

def qcheck(qm, qp):
   p = polynomial([])
   for x in qp:
      p.terms.append(x.term)
   return check(qm.term.monom, p)

def sl2dom (m, li):
   out = []
   d = dominant(m, li)
   for x in d:
      temp = sqfreedom(x, li)
      for y in temp:
         out.append(y)
   return out

def sl2qchar(qm, n, li):
   tmp = []
   for x in qm.term.monom.nodes:
      if x.num == n:
         tmp.append(x)
   boo = False
   for x in tmp:
      if x.sup < 0:
         boo = True
   if boo:
      Inadmissible.append(str(monomial(tmp)) + ' # ' + str(qm.term))
   if len(tmp) == 0 or boo:
      return None
   tmono = monomial(tmp)
   print(str(tmono) + ' # ' + str(qm.term))
   tp = div(qm.term.monom, tmono)
   doms = sl2dom(tmono, li)
   qpoly = [qterm(term(1,tp),[], qm.level)]
   for x in doms:
      qtmp = qchardom(qterm(term(1,x),[],0), li)
      qpoly = qmult(qpoly, qtmp)
   return qpoly

def qchar (m, li):
   qpoly = []
   actives = []
   qmono = qterm(term(1,m), [], 0)
   for i in range(len(li)):
      qmono.color.append(0)
   actives.append(qmono)
   qpoly.append(qmono)
   while len(actives) != 0:
      qmono = actives[0]
      for i in range(len(qmono.color)):
         if qmono.color[i] < qmono.term.coeff:
            qtemp = sl2qchar(qmono, i+1, li)
            if qtemp != None:
               for x in qtemp:
                  j = qcheck(x, qpoly)
                  ja = qcheck(x, actives)
                  if j < 0:
                     c = x.term.coeff*(qmono.term.coeff-qmono.color[i])
                     y = qterm(term(c, x.term.monom), [], x.level)
                     for k in range(len(li)):
                        if k == i:
                           y.color.append(c)
                        else:
                           y.color.append(0)
                     actives.append(y)
                     qpoly.append(y)
                  if ja > 0:
                     c = qpoly[j].color[i] + x.term.coeff*(qmono.term.coeff-qmono.color[i])
                     if c > qpoly[j].term.coeff:
                        qpoly[j].term.coeff = c
                     qpoly[j].color[i] = c
      actives.pop(0)
      actives.sort(key = levelsort)
   poly = polynomial([])
   for x in qpoly:
      poly.terms.append(x.term)
   return poly

Inadmissible = []

mo = monomial([node(1,0,1)])
s = 'E8'
qpol = qchar(mo, lie(s))
print('')
print('qchar of ' + str(mo) + ' for ' + s + ':-')
print(qpol)
print('')
print('Length of qchar = ' + str(length(qpol)))
print('')
print('Number of higher degree monomials = ' + str(squares(qpol)))
print('')
print('Dominant monomials:-')
temp = []
for x in qpol.terms:
   boo = True
   for y in x.monom.nodes:
      if y.sup < 0:
         boo = False
   if boo:
      temp.append(x)
for x in temp:
   print(x)
print('')
print('Inadmissible monomials:-')
for x in Inadmissible:
   print(x)
print('')

out = []
i = 0
while i < 120:
   out.append(qpol.terms[i].monom)
   i = i + 1
while i < 135:
   out.append(qpol.terms[i].monom)
   i = i + 2
i = 121
while i < 135:
   out.append(qpol.terms[i].monom)
   i = i + 2
while i < 248:
   out.append(qpol.terms[i].monom)
   i = i + 1
#i = 0
#while i < 120:
#   print('$$+ ' + str(out[i]) + ' + ' + str(out[i+1]) + ' + ' + str(out[i+2]) + ' + ' + str(out[i+3]) + ' + ' + str(out[i+4]) + ' + ' + str(out[i+5]) + '$$')
#   i = i + 6
#print('$$+ ' + str(out[i]) + ' + ' + str(out[i+1]) + ' + ' + str(out[i+2]) + ' + ' + str(out[i+3]) + ' + ' + str(out[i+4]) + ' + ' + str(out[i+5]) + ' + ' + str(out[i+6]) + ' + ' + str(out[i+7]) + '$$')
#i = i + 8
#while i < 248:
#   print('$$+ ' + str(out[i]) + ' + ' + str(out[i+1]) + ' + ' + str(out[i+2]) + ' + ' + str(out[i+3]) + ' + ' + str(out[i+4]) + ' + ' + str(out[i+5]) + '$$')
#   i = i + 6

def E8KEF (inp):
   stK = ''
   stE = ''
   stF = ''
   li = lie('E8')
   K = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
   E = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
   F = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
   for x in inp:
      tmp = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
      for y in x.nodes:
         tmp[y.num] = tmp[y.num] + y.sup
      for i in range(1,9):
         K[i].append(tmp[i])
         for z in inp:
            temp = div(x,z)
            tem = []
            for yy in temp.nodes:
               if yy.num == i:
                  tem.append(yy.sub)
            if len(tem) > 0:
               tem.sort()
               kk = tem[-1] - li[i-1].nodes[0].sub
               tl = []
               for yyy in li[i-1].nodes:
                  tl.append(node(yyy.num, yyy.sub+kk, yyy.sup))
               temp = div(temp, monomial(tl))
               boo = True
               for zz in temp.nodes:
                  if zz.sup != 0:
                     boo = False
               if boo:
                  E[i].append(str(inp.index(z)+1) + ':' + str(inp.index(x)+1) + ',')
                  F[i].append(str(inp.index(x)+1) + ':' + str(inp.index(z)+1) + ',')
                  #E[i].append(',' + str(inp.index(x)+1) + ',' + str(inp.index(z)+1) + '}->1,')
                  #F[i].append(',' + str(inp.index(z)+1) + ',' + str(inp.index(x)+1) + '}->1,')
   for i in range(1,9):
      stK = stK + str(i) + ' : ['
      stE = stE + str(i) + ' : {'
      stF = stF + str(i) + ' : {'
      for j in range(1,249):
         if K[i][j-1] == 0:
            tt = '1'
         elif K[i][j-1] == 1:
            tt = 'q'
         else:
            tt = 'q^' + str(K[i][j-1])
         stK = stK + str(K[i][j-1]) + ','
         #stK = stK + '{' + str(i) + ',' + str(j) + ',' + str(j) + '}->' + tt + ','
      stK = stK + '0], '
      for x in E[i]:
         stE = stE + x
         #stE = stE + '{' + str(i) + x
      for x in F[i]:
         stF = stF + x
         #stF = stF + '{' + str(i) + x
      stE = stE + '}, '
      stF = stF + '}, '
   return [stK, stE, stF]

def E8sv0 (inp):
   sv0 = []
   for i in range(1,249):
      x = inp[i-1]
      for j in range(1,249):
         tmp = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         for xx in x.nodes:
            tmp[xx.num] = tmp[xx.num] + xx.sup
         y = inp[j-1]
         for yy in y.nodes:
            tmp[yy.num] = tmp[yy.num] + yy.sup
         boo = True
         for k in range(1,9):
            if tmp[k] != 0:
               boo = False
         if boo:
            sv0.append(i)
            sv0.append(j)
            print(str(i) + ' : ' + str(j))
   return sv0

def E8sv1 (inp):
   sv1 = []
   for i in range(1,249):
      x = inp[i-1]
      for j in range(1,249):
         tmp = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         for xx in x.nodes:
            tmp[xx.num] = tmp[xx.num] + xx.sup
         y = inp[j-1]
         for yy in y.nodes:
            tmp[yy.num] = tmp[yy.num] + yy.sup
         if tmp[1]==1 and tmp[2]==0 and tmp[3]==0 and tmp[4]==0 and tmp[5]==0 and tmp[6]==0 and tmp[7]==0 and tmp[8]==0:
            sv1.append(i)
            sv1.append(j)
            print(str(i) + ' : ' + str(j))
   return sv1

def E8sv7 (inp):
   sv7 = []
   for i in range(1,249):
      x = inp[i-1]
      for j in range(1,249):
         tmp = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         for xx in x.nodes:
            tmp[xx.num] = tmp[xx.num] + xx.sup
         y = inp[j-1]
         for yy in y.nodes:
            tmp[yy.num] = tmp[yy.num] + yy.sup
         if tmp[1]==0 and tmp[2]==0 and tmp[3]==0 and tmp[4]==0 and tmp[5]==0 and tmp[6]==0 and tmp[7]==1 and tmp[8]==0:
            sv7.append(i)
            sv7.append(j)
            print(str(i) + ' : ' + str(j))
   return sv7

def E8e0 (inp):
   e0 = []
   for i in range(1,249):
      x = inp[i-1]
      for j in range(1,249):
         tmpx = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         tmpy = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         tmp = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
         for xx in x.nodes:
            tmpx[xx.num] = tmpx[xx.num] + xx.sup
         y = inp[j-1]
         for yy in y.nodes:
            tmpy[yy.num] = tmpy[yy.num] + yy.sup
         for k in range(1,9):
            tmp[k] = tmpx[k] - tmpy[k]
         if tmp[1]==1 and tmp[2]==0 and tmp[3]==0 and tmp[4]==0 and tmp[5]==0 and tmp[6]==0 and tmp[7]==0 and tmp[8]==0:
            e0.append('{' + str(j) + ',' + str(i) + '}->a((q^4+q^2+1+q^-2+q^-4)/(q+q^-1))')
            #e0.append(i)
            #e0.append(j)
            print(str(i) + ' : ' + str(j))
   return e0

#sv = E8e0 (out)
#ss = E8KEF(out)
#print(sv)
#print(len(sv))
#print(ss[0])
#print('')
#print(ss[1])
#print('')
#print(ss[2])
print('')

##
li = lie(s)
V = out[0:120]
print(len(V))
E = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{}}
print(div(V[0],V[1]))
for x in V:
   for y in V:
      z = div(x,y)
      k=0
      while k<len(z.nodes) and z.nodes[k].sup<=0:
         k = k+1
      if k < len(z.nodes):
         zz = z.nodes[k]
         if str(div(z,shift(li[zz.num-1],zz.sub-li[zz.num-1].nodes[1].sub)))=="1":
            E[zz.num].update({V.index(y)+1:V.index(x)+1})
print('')
print(E[1])
print('')
print(E[2])
print('')
print(E[3])
print('')
print(E[4])
print('')
print(E[5])
print('')
print(E[6])
print('')
print(E[7])
print('')
print(E[8])
print('')
def find_path(n, ed):
   pa = []
   k = n
   while k != 1:
      boo = True
      for i in range(1,9):
         if ed[i].get(k) != None:
            boo = False
            pa.append(i)
            k = ed[i][k]
      if boo:
         return None
   return pa
st = '{'
for i in range(113,121):
   #print(i)
   ff=find_path(i,E)
   #print(ff)
   st = st + '{'
   for j in ff:
      st = st + str(j) + ','
   st = st[0:len(st)-1] + '},'
   #print('')
st = st[0:len(st)-1] + '}'
print(st)
##


#temp = []
#for i in range(1,27):
#   for j in range(i,27):
#      for k in range(j,27):
#         p = mult(polynomial([qpol.terms[i-1]]), mult(polynomial([qpol.terms[j-1]]), polynomial([qpol.terms[k-1]])))
#         if len(p.terms) == 1:
#            q = p.terms[0].monom
#            dic = {1:0,2:0,3:0,4:0}
#            for t in q.nodes:
#               dic[t.num] = dic[t.num] + t.sup
#            if dic[1] == 0 and dic[2] == 1 and dic[3] == 0 and dic[4] == 0:
#               tm = str(i) + ',' + str(j) + ',' + str(k)
#               print(tm)
#               temp.append(tm)
#print(len(temp))


mo = monomial([node(1,4,1),node(2,1,1)])
s = 'A2'
qpol = qchar(mo, lie(s))
print('')
print('qchar of ' + str(mo) + ' for ' + s + ':')
print(qpol)
print('')
print('Length of qchar = ' + str(length(qpol)))
print('')
print('Number of higher degree monomials = ' + str(squares(qpol)))
print('')
print('Dominant monomials:')
temp = []
for x in qpol.terms:
   boo = True
   for y in x.monom.nodes:
      if y.sup < 0:
         boo = False
   if boo:
      temp.append(x)
for x in temp:
   print(x)
print('')
print('Inadmissible monomials:')
for x in Inadmissible:
   print(x)
print('')


qpol1 = qchar(monomial([node(1,8,1)]), lie(s))
poly=mult(qpol,qpol1)
#print('')
mono = monomial([node(1,4,1),node(1,6,1),node(1,8,-1),node(1,10,-2),node(1,12,-1),node(2,9,-1),node(2,13,1)])
#print(check(mono, poly))