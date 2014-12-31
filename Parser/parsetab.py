
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x1f\xe5?\x85\xc7\x8d\xc4\x9c\xae\x1f(\ts\xc9\x04\x07'
    
_lr_action_items = {'GREATER':([46,],[51,]),'KEY':([22,],[33,]),'RANGE':([39,],[44,]),'UPDATE':([0,],[1,]),'INSERT':([0,],[4,]),'TABLE':([14,],[23,]),'$end':([2,3,7,8,10,11,12,15,17,24,25,26,27,29,30,35,36,37,39,41,42,45,47,52,53,54,55,],[0,-4,-1,-7,-6,-3,-5,-2,-17,-17,-17,-17,-14,-18,-8,-19,-16,-15,-11,-12,-13,-9,-20,-10,-21,-23,-22,]),'SELECT':([0,],[5,]),'INTEGER':([21,],[31,]),'ATTRIBUTE':([13,],[21,]),'LESS':([46,],[50,]),'DEFINE':([0,],[9,]),'PRIMARY':([13,],[22,]),'DELETE':([0,],[6,]),'SET':([0,],[13,]),'NUMBER':([16,17,19,24,25,26,32,44,48,49,50,51,],[24,25,29,25,25,25,40,48,52,53,54,55,]),'FROM':([18,],[28,]),'CREATE':([0,],[14,]),'RELATION':([9,],[20,]),'WORD':([1,4,5,6,17,20,23,24,25,26,28,31,33,34,40,43,],[16,17,18,19,26,30,34,26,26,26,38,39,41,42,45,46,]),'WHERE':([38,],[43,]),'CHARACTER':([21,],[32,]),'EQUAL':([46,],[49,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'update_cmd':([0,],[10,]),'select_cmd':([0,],[8,]),'expr':([43,],[47,]),'define_cmd':([0,],[7,]),'create_cmd':([0,],[11,]),'delete_cmd':([0,],[12,]),'command':([0,],[2,]),'insert_cmd':([0,],[3,]),'set_cmd':([0,],[15,]),'attribute_expr':([17,24,25,26,],[27,35,36,37,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command","S'",1,None,None,None),
  ('command -> define_cmd','command',1,'p_command','SqlYacc.py',14),
  ('command -> set_cmd','command',1,'p_command','SqlYacc.py',15),
  ('command -> create_cmd','command',1,'p_command','SqlYacc.py',16),
  ('command -> insert_cmd','command',1,'p_command','SqlYacc.py',17),
  ('command -> delete_cmd','command',1,'p_command','SqlYacc.py',18),
  ('command -> update_cmd','command',1,'p_command','SqlYacc.py',19),
  ('command -> select_cmd','command',1,'p_command','SqlYacc.py',20),
  ('define_cmd -> DEFINE RELATION WORD','define_cmd',3,'p_define_cmd','SqlYacc.py',23),
  ('set_cmd -> SET ATTRIBUTE CHARACTER NUMBER WORD','set_cmd',5,'p_set_cmd','SqlYacc.py',27),
  ('set_cmd -> SET ATTRIBUTE INTEGER WORD RANGE NUMBER NUMBER','set_cmd',7,'p_set_cmd','SqlYacc.py',28),
  ('set_cmd -> SET ATTRIBUTE INTEGER WORD','set_cmd',4,'p_set_cmd','SqlYacc.py',29),
  ('set_cmd -> SET PRIMARY KEY WORD','set_cmd',4,'p_set_cmd','SqlYacc.py',30),
  ('create_cmd -> CREATE TABLE WORD WORD','create_cmd',4,'p_create_cmd','SqlYacc.py',37),
  ('insert_cmd -> INSERT WORD attribute_expr','insert_cmd',3,'p_insert_cmd','SqlYacc.py',41),
  ('attribute_expr -> WORD attribute_expr','attribute_expr',2,'p_attribute_expr','SqlYacc.py',45),
  ('attribute_expr -> NUMBER attribute_expr','attribute_expr',2,'p_attribute_expr','SqlYacc.py',46),
  ('attribute_expr -> <empty>','attribute_expr',0,'p_attribute_expr','SqlYacc.py',47),
  ('delete_cmd -> DELETE WORD NUMBER','delete_cmd',3,'p_delete_cmd','SqlYacc.py',51),
  ('update_cmd -> UPDATE WORD NUMBER attribute_expr','update_cmd',4,'p_update_cmd','SqlYacc.py',55),
  ('select_cmd -> SELECT WORD FROM WORD WHERE expr','select_cmd',6,'p_select_cmd','SqlYacc.py',59),
  ('expr -> WORD EQUAL NUMBER','expr',3,'p_expr','SqlYacc.py',63),
  ('expr -> WORD GREATER NUMBER','expr',3,'p_expr','SqlYacc.py',64),
  ('expr -> WORD LESS NUMBER','expr',3,'p_expr','SqlYacc.py',65),
]
