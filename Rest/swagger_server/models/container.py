# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Container(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, host: str=None, monitor: bool=None, status: str=None):  # noqa: E501
        """Container - a model defined in Swagger

        :param name: The name of this Container.  # noqa: E501
        :type name: str
        :param host: The host of this Container.  # noqa: E501
        :type host: str
        :param monitor: The monitor of this Container.  # noqa: E501
        :type monitor: bool
        :param status: The status of this Container.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'name': str,
            'host': str,
            'monitor': bool,
            'status': str
        }

        self.attribute_map = {
            'name': 'name',
            'host': 'host',
            'monitor': 'monitor',
            'status': 'status'
        }

        self._name = name
        self._host = host
        self._monitor = monitor
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Container':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Container of this Container.  # noqa: E501
        :rtype: Container
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Container.


        :return: The name of this Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Container.


        :param name: The name of this Container.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def host(self) -> str:
        """Gets the host of this Container.


        :return: The host of this Container.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this Container.


        :param host: The host of this Container.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def monitor(self) -> bool:
        """Gets the monitor of this Container.


        :return: The monitor of this Container.
        :rtype: bool
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor: bool):
        """Sets the monitor of this Container.


        :param monitor: The monitor of this Container.
        :type monitor: bool
        """

        self._monitor = monitor

    @property
    def status(self) -> str:
        """Gets the status of this Container.


        :return: The status of this Container.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Container.


        :param status: The status of this Container.
        :type status: str
        """

        self._status = status
