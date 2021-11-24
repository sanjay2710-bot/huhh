# Ported from @TeamDaisyX
# Written by InukaAsith for the Daisy project

# This file is part of Shadow (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.


import json
import math

import requests

from Shadow.decorator import register

from .utils.disable import disableable_dec
from .utils.message import get_args_str


@register(cmds=["math", "simplify"])
@disableable_dec("math")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/simplify/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds=["factor", "factorize"])
@disableable_dec("factor")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/factor/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="derive")
@disableable_dec("derive")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/derive/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="integrate")
@disableable_dec("integrate")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/integrate/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="zeroes")
@disableable_dec("zeroes")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/zeroes/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="tangent")
@disableable_dec("tangent")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/tangent/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="area")
@disableable_dec("area")
async def _(message):
    args = get_args_str(message)
    response = requests.get(f"https://newton.now.sh/api/v2/area/{args}")
    c = response.text
    obj = json.loads(c)
    j = obj["result"]
    await message.reply(j)


@register(cmds="cos")
@disableable_dec("cos")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.cos(int(args))))


@register(cmds="sin")
@disableable_dec("sin")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.sin(int(args))))


@register(cmds="tan")
@disableable_dec("tan")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.tan(int(args))))


@register(cmds="arccos")
@disableable_dec("arccos")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.acos(int(args))))


@register(cmds="arcsin")
@disableable_dec("arcsin")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.asin(int(args))))


@register(cmds="arctan")
@disableable_dec("arctan")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.atan(int(args))))


@register(cmds="abs")
@disableable_dec("abs")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.fabs(int(args))))


@register(cmds="log")
@disableable_dec("log")
async def _(message):
    args = get_args_str(message)
    await message.reply(str(math.log(int(args))))


__help__ = """
Solves complex math problems using <a href="https://newton.now.sh">this website</a> and python math module

 - /simplify: Math <code>/math 2^2+2(2)</code>
 - /factor: Factor <code>/factor x^2 + 2x</code>
 - /derive: Derive <code>/derive x^2+2x</code>
 - /integrate: Integrate <code>/integrate x^2+2x</code>
 - /zeroes: Find 0's <code>/zeroes x^2+2x</code>
 - /tangent: Find Tangent <code>/tangent 2lx^</code>
 - /area: Area Under Curve <code>/area 2:4lx^3</code>
 - /cos: Cosine <code>/cos pi</code>
 - /sin: Sine <code>/sin 0</code>
 - /tan: Tangent <code>/tan 0</code>
 - /arccos: Inverse Cosine <code>/arccos 1</code>
 - /arcsin: Inverse Sine <code>/arcsin 0</code>
 - /arctan: Inverse Tangent <code>/arctan 0</code>
 - /abs: Absolute Value <code>/abs -1</code>
 - /log: Logarithm <code>/log 2l8</code>
 
Keep in mind, To find the tangent line of a function at a certain x value, send the request as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
To find the area under a function, send the request as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
To compute fractions, enter expressions as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).
"""

__mod_name__ = "Maths"
