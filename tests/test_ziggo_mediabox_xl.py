#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ziggo_mediabox_xl` package."""


import unittest

import ziggo_mediabox_xl


class TestZiggo_mediabox_xl(unittest.TestCase):
    """Tests for `ziggo_mediabox_xl` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self._zmxl = ziggo_mediabox_xl.ZiggoMediaboxXL('127.6.6.6')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        self.assertFalse(self._zmxl.turned_on())
        self.assertIn('NPO 1', self._zmxl.channels().values())
