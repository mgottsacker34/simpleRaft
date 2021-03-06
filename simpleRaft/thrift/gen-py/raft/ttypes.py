#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class LogEntry:
  """
  Attributes:
   - term
   - index
   - command
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'term', None, None, ), # 1
    (2, TType.I64, 'index', None, None, ), # 2
    (3, TType.STRING, 'command', None, None, ), # 3
  )

  def __init__(self, term=None, index=None, command=None,):
    self.term = term
    self.index = index
    self.command = command

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.term = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.index = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.command = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LogEntry')
    if self.term is not None:
      oprot.writeFieldBegin('term', TType.I32, 1)
      oprot.writeI32(self.term)
      oprot.writeFieldEnd()
    if self.index is not None:
      oprot.writeFieldBegin('index', TType.I64, 2)
      oprot.writeI64(self.index)
      oprot.writeFieldEnd()
    if self.command is not None:
      oprot.writeFieldBegin('command', TType.STRING, 3)
      oprot.writeString(self.command)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.term is None:
      raise TProtocol.TProtocolException(message='Required field term is unset!')
    if self.index is None:
      raise TProtocol.TProtocolException(message='Required field index is unset!')
    if self.command is None:
      raise TProtocol.TProtocolException(message='Required field command is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AppendEntries:
  """
  Attributes:
   - term
   - leaderId
   - commitIndex
   - prevLogIndex
   - prevLogTerm
   - entries
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'term', None, None, ), # 1
    (2, TType.STRING, 'leaderId', None, None, ), # 2
    (3, TType.I64, 'commitIndex', None, -1, ), # 3
    (4, TType.I64, 'prevLogIndex', None, -1, ), # 4
    (5, TType.I32, 'prevLogTerm', None, -1, ), # 5
    (6, TType.LIST, 'entries', (TType.STRUCT,(LogEntry, LogEntry.thrift_spec)), None, ), # 6
  )

  def __init__(self, term=None, leaderId=None, commitIndex=thrift_spec[3][4], prevLogIndex=thrift_spec[4][4], prevLogTerm=thrift_spec[5][4], entries=None,):
    self.term = term
    self.leaderId = leaderId
    self.commitIndex = commitIndex
    self.prevLogIndex = prevLogIndex
    self.prevLogTerm = prevLogTerm
    self.entries = entries

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.term = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.leaderId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.commitIndex = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.prevLogIndex = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.prevLogTerm = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.entries = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = LogEntry()
            _elem5.read(iprot)
            self.entries.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AppendEntries')
    if self.term is not None:
      oprot.writeFieldBegin('term', TType.I32, 1)
      oprot.writeI32(self.term)
      oprot.writeFieldEnd()
    if self.leaderId is not None:
      oprot.writeFieldBegin('leaderId', TType.STRING, 2)
      oprot.writeString(self.leaderId)
      oprot.writeFieldEnd()
    if self.commitIndex is not None:
      oprot.writeFieldBegin('commitIndex', TType.I64, 3)
      oprot.writeI64(self.commitIndex)
      oprot.writeFieldEnd()
    if self.prevLogIndex is not None:
      oprot.writeFieldBegin('prevLogIndex', TType.I64, 4)
      oprot.writeI64(self.prevLogIndex)
      oprot.writeFieldEnd()
    if self.prevLogTerm is not None:
      oprot.writeFieldBegin('prevLogTerm', TType.I32, 5)
      oprot.writeI32(self.prevLogTerm)
      oprot.writeFieldEnd()
    if self.entries is not None:
      oprot.writeFieldBegin('entries', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.entries))
      for iter6 in self.entries:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.term is None:
      raise TProtocol.TProtocolException(message='Required field term is unset!')
    if self.leaderId is None:
      raise TProtocol.TProtocolException(message='Required field leaderId is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AppendEntriesResponse:
  """
  Attributes:
   - term
   - success
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'term', None, None, ), # 1
    (2, TType.BOOL, 'success', None, None, ), # 2
  )

  def __init__(self, term=None, success=None,):
    self.term = term
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.term = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AppendEntriesResponse')
    if self.term is not None:
      oprot.writeFieldBegin('term', TType.I32, 1)
      oprot.writeI32(self.term)
      oprot.writeFieldEnd()
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 2)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.term is None:
      raise TProtocol.TProtocolException(message='Required field term is unset!')
    if self.success is None:
      raise TProtocol.TProtocolException(message='Required field success is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RequestVote:
  """
  Attributes:
   - memberId
   - term
   - lastLogIndex
   - lastLogTerm
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'memberId', None, None, ), # 1
    (2, TType.I32, 'term', None, None, ), # 2
    (3, TType.I64, 'lastLogIndex', None, -1, ), # 3
    (4, TType.I32, 'lastLogTerm', None, -1, ), # 4
  )

  def __init__(self, memberId=None, term=None, lastLogIndex=thrift_spec[3][4], lastLogTerm=thrift_spec[4][4],):
    self.memberId = memberId
    self.term = term
    self.lastLogIndex = lastLogIndex
    self.lastLogTerm = lastLogTerm

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.memberId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.term = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.lastLogIndex = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.lastLogTerm = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RequestVote')
    if self.memberId is not None:
      oprot.writeFieldBegin('memberId', TType.STRING, 1)
      oprot.writeString(self.memberId)
      oprot.writeFieldEnd()
    if self.term is not None:
      oprot.writeFieldBegin('term', TType.I32, 2)
      oprot.writeI32(self.term)
      oprot.writeFieldEnd()
    if self.lastLogIndex is not None:
      oprot.writeFieldBegin('lastLogIndex', TType.I64, 3)
      oprot.writeI64(self.lastLogIndex)
      oprot.writeFieldEnd()
    if self.lastLogTerm is not None:
      oprot.writeFieldBegin('lastLogTerm', TType.I32, 4)
      oprot.writeI32(self.lastLogTerm)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.memberId is None:
      raise TProtocol.TProtocolException(message='Required field memberId is unset!')
    if self.term is None:
      raise TProtocol.TProtocolException(message='Required field term is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RequestVoteResponse:
  """
  Attributes:
   - currentTerm
   - granted
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'currentTerm', None, None, ), # 1
    (2, TType.BOOL, 'granted', None, None, ), # 2
  )

  def __init__(self, currentTerm=None, granted=None,):
    self.currentTerm = currentTerm
    self.granted = granted

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.currentTerm = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.granted = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RequestVoteResponse')
    if self.currentTerm is not None:
      oprot.writeFieldBegin('currentTerm', TType.I32, 1)
      oprot.writeI32(self.currentTerm)
      oprot.writeFieldEnd()
    if self.granted is not None:
      oprot.writeFieldBegin('granted', TType.BOOL, 2)
      oprot.writeBool(self.granted)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.currentTerm is None:
      raise TProtocol.TProtocolException(message='Required field currentTerm is unset!')
    if self.granted is None:
      raise TProtocol.TProtocolException(message='Required field granted is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Snapshot:
  """
  Attributes:
   - stateMachineState
   - lastLogEntryIndex
   - lastLogEntryTerm
   - membershipState
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'stateMachineState', None, None, ), # 1
    (2, TType.I64, 'lastLogEntryIndex', None, None, ), # 2
    (3, TType.I32, 'lastLogEntryTerm', None, None, ), # 3
    (4, TType.STRING, 'membershipState', None, None, ), # 4
  )

  def __init__(self, stateMachineState=None, lastLogEntryIndex=None, lastLogEntryTerm=None, membershipState=None,):
    self.stateMachineState = stateMachineState
    self.lastLogEntryIndex = lastLogEntryIndex
    self.lastLogEntryTerm = lastLogEntryTerm
    self.membershipState = membershipState

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.stateMachineState = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.lastLogEntryIndex = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.lastLogEntryTerm = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.membershipState = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Snapshot')
    if self.stateMachineState is not None:
      oprot.writeFieldBegin('stateMachineState', TType.STRING, 1)
      oprot.writeString(self.stateMachineState)
      oprot.writeFieldEnd()
    if self.lastLogEntryIndex is not None:
      oprot.writeFieldBegin('lastLogEntryIndex', TType.I64, 2)
      oprot.writeI64(self.lastLogEntryIndex)
      oprot.writeFieldEnd()
    if self.lastLogEntryTerm is not None:
      oprot.writeFieldBegin('lastLogEntryTerm', TType.I32, 3)
      oprot.writeI32(self.lastLogEntryTerm)
      oprot.writeFieldEnd()
    if self.membershipState is not None:
      oprot.writeFieldBegin('membershipState', TType.STRING, 4)
      oprot.writeString(self.membershipState)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.stateMachineState is None:
      raise TProtocol.TProtocolException(message='Required field stateMachineState is unset!')
    if self.lastLogEntryIndex is None:
      raise TProtocol.TProtocolException(message='Required field lastLogEntryIndex is unset!')
    if self.lastLogEntryTerm is None:
      raise TProtocol.TProtocolException(message='Required field lastLogEntryTerm is unset!')
    if self.membershipState is None:
      raise TProtocol.TProtocolException(message='Required field membershipState is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InstallSnapshot:
  """
  Attributes:
   - term
   - leaderId
   - snapshot
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'term', None, None, ), # 1
    (2, TType.STRING, 'leaderId', None, None, ), # 2
    (3, TType.STRUCT, 'snapshot', (Snapshot, Snapshot.thrift_spec), None, ), # 3
  )

  def __init__(self, term=None, leaderId=None, snapshot=None,):
    self.term = term
    self.leaderId = leaderId
    self.snapshot = snapshot

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.term = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.leaderId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.snapshot = Snapshot()
          self.snapshot.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InstallSnapshot')
    if self.term is not None:
      oprot.writeFieldBegin('term', TType.I32, 1)
      oprot.writeI32(self.term)
      oprot.writeFieldEnd()
    if self.leaderId is not None:
      oprot.writeFieldBegin('leaderId', TType.STRING, 2)
      oprot.writeString(self.leaderId)
      oprot.writeFieldEnd()
    if self.snapshot is not None:
      oprot.writeFieldBegin('snapshot', TType.STRUCT, 3)
      self.snapshot.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.term is None:
      raise TProtocol.TProtocolException(message='Required field term is unset!')
    if self.leaderId is None:
      raise TProtocol.TProtocolException(message='Required field leaderId is unset!')
    if self.snapshot is None:
      raise TProtocol.TProtocolException(message='Required field snapshot is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InstallSnapshotResponse:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'success', None, None, ), # 1
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InstallSnapshotResponse')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 1)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.success is None:
      raise TProtocol.TProtocolException(message='Required field success is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JoinMember:
  """
  Attributes:
   - memberId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'memberId', None, None, ), # 1
  )

  def __init__(self, memberId=None,):
    self.memberId = memberId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.memberId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JoinMember')
    if self.memberId is not None:
      oprot.writeFieldBegin('memberId', TType.STRING, 1)
      oprot.writeString(self.memberId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.memberId is None:
      raise TProtocol.TProtocolException(message='Required field memberId is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class JoinMemberResponse:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'success', None, None, ), # 1
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('JoinMemberResponse')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 1)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.success is None:
      raise TProtocol.TProtocolException(message='Required field success is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
