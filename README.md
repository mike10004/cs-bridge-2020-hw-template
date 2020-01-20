# Homework Project Template

This repository is a template for projects that contain solutions to homework 
assignments for NYU Tandon CS Bridge Winter 2020.

To use this template, fork the repository and perform the following 
modifications:

1. change this readme to reflect that this is an assignment, not the template
2. rename `q1/mac937_hwN_q1.cpp` with the correct NetID (replacing `mac937`) 
   and week number (replacing `N`)
3. change `q1/CMakeLists.txt` to use the correct `.cpp` filename
4. modify `question.md`, `input.txt`, and `expected-output.txt` as appropriate 
   for the question; delete `input.txt` if no input is necessary
5. for each additional question, copy `q1` to a new subdirectory, add a 
   subdirectory line to `CMakeLists.txt`, and repeat steps 2-4 for the 
   new question subdirectory 

## Commands

The `build.sh` and `clean.sh` scripts do what they sound like they do.

When you execute `check.sh`, for each executable, the executable is launched,
each line from `input.txt` is copied to the process standard input 
stream, and the output is checked against `expected-output.txt`.

This happens inside a `screen` session so that the input text is echoed to
the output, as would happen in a tty.

## License

Copyright (c) 2019 Mike Chaberski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.