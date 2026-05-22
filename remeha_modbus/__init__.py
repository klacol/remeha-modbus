# remeha_modbus

"""Python library for accessing Remeha heating systems via Modbus TCP (GTW-08 gateway)."""

from .registers import RegisterDefinition, DataType
from .client import RemehaModbusClient

__all__ = ["RemehaModbusClient", "RegisterDefinition", "DataType"]
