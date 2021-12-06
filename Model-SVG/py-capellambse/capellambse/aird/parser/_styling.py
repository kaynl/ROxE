# Copyright 2021 DB Netz AG
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
"""Functions that handle element styling."""
from __future__ import annotations

import collections.abc as cabc
import struct
import typing as t

import lxml.etree

from capellambse import aird

from ._common import LOGGER


def apply_style_overrides(
    diagram_class: str | None,
    element_class: str,
    ostyle: lxml.etree._Element,
) -> dict[str, str | aird.RGB | list[str | aird.RGB]]:
    """Apply style overrides defined in the AIRD to a semantic element.

    Parameters
    ----------
    diagram_class
        The target diagram's style class
    element_class
        The class of this element, in the form of:
        ``{Edge|Box}.{class}``.
    ostyle
        An ownedStyle element.
    """

    def _to_rgb(ostyle: lxml.etree._Element, attrib: str) -> aird.RGB | None:
        color = ostyle.get(attrib)
        if color is not None:
            color = aird.RGB.fromcsv(color)
        return color

    if diagram_class is None:
        return {}

    styleoverrides: dict[str, aird.CSSdef] = {}

    # Background color
    color = _to_rgb(ostyle, "color")
    bgcolor = _to_rgb(ostyle, "backgroundColor")
    fgcolor = _to_rgb(ostyle, "foregroundColor")
    if color:
        styleoverrides["fill"] = color
    elif bgcolor or fgcolor:
        bgcolor = bgcolor or aird.RGB(255, 255, 255)
        fgcolor = fgcolor or aird.RGB(209, 209, 209)

        if bgcolor == fgcolor:
            styleoverrides["fill"] = bgcolor
        else:
            styleoverrides["fill"] = [bgcolor, fgcolor]

    # Foreground / font color
    styleoverrides["text_fill"] = _to_rgb(ostyle, "labelColor")

    linestyle = ostyle.attrib.get("lineStyle")
    if linestyle == "dash":
        styleoverrides["stroke-dasharray"] = "5"
    elif linestyle == "dot":
        styleoverrides["stroke-dasharray"] = "1, 3"
    elif linestyle is not None:
        LOGGER.warning("Ignoring unknown line style %s", linestyle)

    if element_class.startswith("Edge."):
        styleoverrides["stroke"] = _to_rgb(ostyle, "strokeColor")
        styleoverrides["stroke-width"] = ostyle.get("size")
    elif element_class.startswith("Box."):
        styleoverrides["stroke"] = _to_rgb(ostyle, "borderColor")
        styleoverrides["stroke-width"] = ostyle.get("borderSize")
    return _filter_default_styles(diagram_class, element_class, styleoverrides)


def apply_visualelement_styles(
    diagram_class: str, element_class: str, data_element: lxml.etree._Element
) -> dict[str, str | aird.RGB | list[str | aird.RGB]]:
    """Apply style overrides defined in the AIRD to a visual element.

    Parameters
    ----------
    diagram_class
        The target diagram's style class
    element_class
        The class of this element, in the form of:
        ``{Edge|Box}.{class}``
    data_element
        The ``<data>`` subtree's child element
    """
    styleoverrides: dict[str, t.Any] = {}

    def unpack_rgb(color: str, default: int) -> aird.RGB:
        color_int = int(data_element.get(color, default))
        return aird.RGB(
            *struct.unpack_from("3Bx", struct.pack("<i", color_int))
        )

    styleoverrides["stroke"] = unpack_rgb("lineColor", 0xFFFFFF)
    styleoverrides["fill"] = unpack_rgb("fillColor", 0xFFFFFF)
    styleoverrides["text_fill"] = unpack_rgb("fontColor", 0x000000)

    try:
        styleoverrides["stroke-width"] = int(data_element.attrib["lineWidth"])
    except KeyError:
        pass

    return _filter_default_styles(diagram_class, element_class, styleoverrides)


def _filter_default_styles(
    diagram_class: str,
    element_class: str,
    styleoverrides: cabc.Mapping[str, t.Any],
) -> dict[str, str | aird.RGB | list[str | aird.RGB]]:
    def style_is_default(key: str, val: t.Any) -> bool:
        for dia_lookup, elm_lookup in [
            (diagram_class, element_class),
            ("__GLOBAL__", element_class),
            (diagram_class, element_class.split(".")[0]),
            ("__GLOBAL__", element_class.split(".")[0]),
        ]:
            defstyle = aird.STYLES.get(dia_lookup, {}).get(elm_lookup, {})
            try:
                return defstyle[key] == val
            except KeyError:
                pass
        return False

    return {
        k: ([str(vx) for vx in v] if isinstance(v, list) else str(v))
        for k, v in styleoverrides.items()
        if v and not style_is_default(k, v)
    }