import random
import unittest


class Worker():
   def __init__(self,name,parts,assemble_time,slave=None):
      self.name = name
      self.parts = parts
      self.assemble_time = assemble_time
      self.slave = slave
      self.bucket = []
      self.time_rotation = assemble_time

   def run(self,stage):
      try:
         if all([i in self.bucket for i in self.parts]):
            if self.time_rotation <= 0:

               if stage.item == '':
                  self.bucket = []
                  self.time_rotation = self.assemble_time
                  stage.item = 'P'
               else:
                  if self.slave:
                     self.slave.run(stage)
            else:
               if self.slave:
                  self.time_rotation -= 1
                  self.slave.run(stage)
         else:
            if stage.item not in self.bucket and stage.item in self.parts:
               self.bucket.append(stage.item)
               stage.item = ''
            else:
               if self.slave: self.slave.run(stage)
      except Exception as e:
         print("Caught an exception {}".format(e))

class Source():
   def __init__(self,items=['A','B','']):
      self.items = items

   def non_empty_items(self):
      return self.items.remove('')

   def create_item(self):
      return random.choice(self.items)



class Stage(object):

   def __init__(self, item):
      self.item = item

class Validator():

   def __init__(self):
      self.products = {'P': 0, 'A': 0, 'B': 0}


   def add_items(self,output):
      if output.item:
         self.products[output.item] += 1

   def total_products(self):
      return "P: {} A: {} B: {}".format(self.products['P'],self.products['A'],self.products['B'])


class ConveryorBelt():

   def __init__(self, source, validators, stages=3):
      self.noofstages = stages
      self.stages = [Stage('')] * stages
      self.source = source
      self.workers = ConveryorBelt.define_workers(self.stages,self.noofstages)
      self.validators = validators

   @staticmethod
   def define_workers(stages,noofstages):
        workers = {}
        try:
           for i, _ in enumerate(stages):
               # Two workers either side of the conveyor belt
               workers[i] = Worker('M%d' % i,
                                   ['A','B'],
                                   noofstages,
                                   Worker('S%d' % i,
                                          ['A','B'],
                                          noofstages  ))
           return workers
        except Exception as e:
           print("Caught an exception {}".format(e))



   def run(self, iterations):
      k = [self.source.create_item() for l in range(iterations)]
      for j in k:
         # print ('\n' + '------' * len(self.stages))
         self.stages = [Stage(j)] + self.stages[:-1]
         for i, s in enumerate(self.stages):
            print(i,s.item)
            self.workers[i].run(s)
         self.validators.add_items(self.stages[-1])
      # print(self.validators.total_products())
      return self.validators.total_products()

   def testrun(self, testlist):
      for j in testlist:
         # print ('\n' + '------' * len(self.stages))
         self.stages = [Stage(j)] + self.stages[:-1]
         for i, s in enumerate(self.stages):
            # print(i,s.item)
            self.workers[i].run(s)
         self.validators.add_items(self.stages[-1])
      # print(self.validators.total_products())
      return self.validators.total_products()



class TestConvyerBelt(unittest.TestCase):


   def test_doublebelt_withproduct(self):
      self.assertEqual(   ConveryorBelt(Source(),
            Validator(),
            stages=2).testrun(['A','B','','','','']), 'P: 1 A: 0 B: 0')

   def test_triplebelt_withproduct(self):
      self.assertEqual(   ConveryorBelt(Source(),
            Validator(),
            stages=3).testrun(['A','B','A','','','','','','']), 'P: 1 A: 0 B: 0')

   def test_doublebelt_withoutproduct(self):
      self.assertEqual(ConveryorBelt(Source(),
                                     Validator(),
                                     stages=2).testrun(['A', 'B', '', '','']), 'P: 0 A: 0 B: 0')

   def test_triplebelt_withoutproduct(self):
      self.assertEqual(   ConveryorBelt(Source(),
            Validator(),
            stages=3).testrun(['A','B','A','','','','']), 'P: 0 A: 0 B: 0')

   def test_triple_random(self):
      self.assertEqual(   ConveryorBelt(Source(),
            Validator(),
            stages=3).testrun(['A', 'A', 'A', 'A', 'A', 'A', '', 'A', 'A', 'A', 'A', '', 'A', 'A', '', 'A', '', 'B', 'B', '', 'B', 'A', '', '', 'B', 'B', 'B', '', 'B', '', 'B', '', '', 'B', 'A', 'A', 'A', 'A', '', 'B', 'A', 'B', '', 'A', 'A', '', '', 'B', 'A', '', 'B', 'A', 'B', 'B', '', 'A', 'A', 'B', '', 'B', 'A', 'B', 'B', '', 'B', 'B', 'B', 'B', '', '', 'A', 'A', 'B', '', '', '', '', 'A', '', '', '', 'B', '', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'A', '', '', '', 'B', 'A', 'A', '', 'A', '', '', '', 'A', '', 'B', 'B', 'B', 'B', '', 'A', 'B', 'A', 'B', 'B', 'A', '']), 'P: 23 A: 15 B: 8')


if __name__ == '__main__':
   unittest.main()
