class node:
   def __init__(self, num, sub, sup):
      self.num = num
      self.sub = sub
      self.sup = sup
   def __str__ (self):
      if self.sup == 0:
         return f""
      elif self.sup == 1:
         return f"\\mathbb{{{self.num}}}_{{{self.sub}}}"
      else:
         return f"\\mathbb{{{self.num}}}_{{{self.sub}}}^{{{self.sup}}}"

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

Inadmissible = []

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
   #print(str(tmono) + ' # ' + str(qm.term))
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