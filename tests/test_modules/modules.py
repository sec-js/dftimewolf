# -*- coding: utf-8 -*-
"""Contains dummy modules used in tests."""

from dftimewolf.lib import module
from dftimewolf.lib.containers import containers


class DummyModule1(module.BaseModule):
  """This is a dummy module."""

  def __init__(self, state, name=None):
    self.runtime_value = None
    super(DummyModule1, self).__init__(state, name)

  def SetUp(self, runtime_value=None):  # pylint: disable=arguments-differ
    """Dummy setup function."""
    self.runtime_value = runtime_value
    print(self.name + ' Setup!')
    self.RegisterStreamingCallback(callback=self.Callback,
                                   container_type=containers.Report)

  def Callback(self, container):
    """Dummy callback that we just want to have called"""

  def Process(self):
    """Dummy Process function."""
    print(self.name + ' Process!')
    self.LogTelemetry({'random_key1': 'random_value1'})


class DummyModule2(module.BaseModule):
  """This is a dummy module."""

  def __init__(self, state, name=None):
    self.runtime_value = None
    super(DummyModule2, self).__init__(state, name)

  def SetUp(self, runtime_value=None):  # pylint: disable=arguments-differ
    """Dummy setup function."""
    self.runtime_value = runtime_value
    print(self.name + ' Setup!')

  def Process(self):
    """Dummy Process function."""
    print(self.name + ' Process!')
    self.LogTelemetry({'random_key2': 'random_value2'})


class DummyPreflightModule(module.PreflightModule):
  """Dummy preflight module."""

  def __init__(self, state, name=None):
    super(DummyPreflightModule, self).__init__(state, name)

  def SetUp(self, args):  # pylint: disable=arguments-differ
    """Dummy Process function."""
    print(self.name + ' SetUp!')

  def Process(self):
    """Dummy Process function."""
    print(self.name + ' Process!')

  def CleanUp(self):
    """Dummy cleanup function."""
    print(self.name + 'CleanUp!')
