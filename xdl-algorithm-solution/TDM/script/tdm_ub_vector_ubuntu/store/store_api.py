# Copyright (C) 2016-2018 Alibaba Group Holding Limited
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_store_api', [dirname(__file__)])
        except ImportError:
            import _store_api
            return _store_api
        if fp is not None:
            try:
                _mod = imp.load_module('_store_api', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _store_api = swig_import_helper()
    del swig_import_helper
else:
    import _store_api
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def cdata(*args):
  return _store_api.cdata(*args)
cdata = _store_api.cdata

def memmove(*args):
  return _store_api.memmove(*args)
memmove = _store_api.memmove
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _store_api.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _store_api.SwigPyIterator_value(self)
    def incr(self, n=1): return _store_api.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _store_api.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _store_api.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _store_api.SwigPyIterator_equal(self, *args)
    def copy(self): return _store_api.SwigPyIterator_copy(self)
    def next(self): return _store_api.SwigPyIterator_next(self)
    def __next__(self): return _store_api.SwigPyIterator___next__(self)
    def previous(self): return _store_api.SwigPyIterator_previous(self)
    def advance(self, *args): return _store_api.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _store_api.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _store_api.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _store_api.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _store_api.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _store_api.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _store_api.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _store_api.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class _string_list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _string_list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _string_list, name)
    __repr__ = _swig_repr
    def iterator(self): return _store_api._string_list_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _store_api._string_list___nonzero__(self)
    def __bool__(self): return _store_api._string_list___bool__(self)
    def __len__(self): return _store_api._string_list___len__(self)
    def pop(self): return _store_api._string_list_pop(self)
    def __getslice__(self, *args): return _store_api._string_list___getslice__(self, *args)
    def __setslice__(self, *args): return _store_api._string_list___setslice__(self, *args)
    def __delslice__(self, *args): return _store_api._string_list___delslice__(self, *args)
    def __delitem__(self, *args): return _store_api._string_list___delitem__(self, *args)
    def __getitem__(self, *args): return _store_api._string_list___getitem__(self, *args)
    def __setitem__(self, *args): return _store_api._string_list___setitem__(self, *args)
    def append(self, *args): return _store_api._string_list_append(self, *args)
    def empty(self): return _store_api._string_list_empty(self)
    def size(self): return _store_api._string_list_size(self)
    def clear(self): return _store_api._string_list_clear(self)
    def swap(self, *args): return _store_api._string_list_swap(self, *args)
    def get_allocator(self): return _store_api._string_list_get_allocator(self)
    def begin(self): return _store_api._string_list_begin(self)
    def end(self): return _store_api._string_list_end(self)
    def rbegin(self): return _store_api._string_list_rbegin(self)
    def rend(self): return _store_api._string_list_rend(self)
    def pop_back(self): return _store_api._string_list_pop_back(self)
    def erase(self, *args): return _store_api._string_list_erase(self, *args)
    def __init__(self, *args): 
        this = _store_api.new__string_list(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _store_api._string_list_push_back(self, *args)
    def front(self): return _store_api._string_list_front(self)
    def back(self): return _store_api._string_list_back(self)
    def assign(self, *args): return _store_api._string_list_assign(self, *args)
    def resize(self, *args): return _store_api._string_list_resize(self, *args)
    def insert(self, *args): return _store_api._string_list_insert(self, *args)
    def reserve(self, *args): return _store_api._string_list_reserve(self, *args)
    def capacity(self): return _store_api._string_list_capacity(self)
    __swig_destroy__ = _store_api.delete__string_list
    __del__ = lambda self : None;
_string_list_swigregister = _store_api._string_list_swigregister
_string_list_swigregister(_string_list)


def STORE_API_new(*args):
  return _store_api.STORE_API_new(*args)
STORE_API_new = _store_api.STORE_API_new

def STORE_API_load(*args):
  return _store_api.STORE_API_load(*args)
STORE_API_load = _store_api.STORE_API_load

def STORE_API_close(*args):
  return _store_api.STORE_API_close(*args)
STORE_API_close = _store_api.STORE_API_close

def STORE_API_put(*args):
  return _store_api.STORE_API_put(*args)
STORE_API_put = _store_api.STORE_API_put

def STORE_API_get(*args):
  return _store_api.STORE_API_get(*args)
STORE_API_get = _store_api.STORE_API_get

def STORE_API_mget(*args):
  return _store_api.STORE_API_mget(*args)
STORE_API_mget = _store_api.STORE_API_mget

def STORE_API_mput(*args):
  return _store_api.STORE_API_mput(*args)
STORE_API_mput = _store_api.STORE_API_mput

def new_string():
  return _store_api.new_string()
new_string = _store_api.new_string

def string_value(*args):
  return _store_api.string_value(*args)
string_value = _store_api.string_value

def free_string(*args):
  return _store_api.free_string(*args)
free_string = _store_api.free_string

def new_string_vector():
  return _store_api.new_string_vector()
new_string_vector = _store_api.new_string_vector

def string_vector_value(*args):
  return _store_api.string_vector_value(*args)
string_vector_value = _store_api.string_vector_value

def free_string_vector(*args):
  return _store_api.free_string_vector(*args)
free_string_vector = _store_api.free_string_vector
# This file is compatible with both classic and new-style classes.

