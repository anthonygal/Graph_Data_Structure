The proposed problem to solve is the following:

## Model of a student's curricular program

A student must complete a given set of courses to get his degree.  
A course may have one or several prerequisites. This means that to complete the course at a given semester, the student must have completed the prerequisite courses during previous semesters.
Lets assume that a student can only follow one course per semester. What we want to know is:
##### In what order the student should complete the courses in order to get his degree?

#### Proposed graph model

This problem can be modeled as a dependency graph such that:

G(V,E) is a directed acyclic graph.

V = {c is a course}

E = {(x,y) | x and y are courses and x must be completed before y}

#### Let's consider the following set of courses:

Courses with no prerequisites:
 - Business Management 
 - Human Sciences
  
Prerequisite course for Mechanics 1 and Software 1 courses:
 - Mathematics 1
 
Prerequisite course for Mechanics 1 course:
  - Physics 1
  
Advanced courses: 
 - Mathematics 2
 - Physics 2
 - Mechanics 1
 - Mechanics 2
 - Software 1
 - Software 2
 
NB: Level 1 courses must be completed before level 2 courses