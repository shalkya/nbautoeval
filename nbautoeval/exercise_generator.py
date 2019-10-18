# -*- coding: utf-8 -*-

# pylint: disable=c0111, r1705, w0703

import itertools

from collections.abc import Iterator

from .exercise_function import ExerciseFunction

class ExerciseGenerator(ExerciseFunction):
    """
    With these exercises the students are asked to write a generator
    function; the Args mechanism is the same as for regular functions;
    an optional 'max_iterations' attribute allows to deal with infinite 
    iterators
    validation is done by 
    (*) counting the number of items in the enumeration 
        maxed by max_iterations if relevant
    (*) comparing each of the results yielded by next()
    """
    @staticmethod
    def generator_to_solution(generator_function, max_iterations=None):
        def solution(*args, **kwds):
            # call the function written by the student
            generator = generator_function(*args, **kwds)
            if not isinstance(generator, (Iterator, range)):
                raise TypeError(f"received a {type(generator)} instance: {generator} that is not an iterator ")
            if max_iterations is None:
                return list(generator)
            result = list(itertools.islice(generator, None, max_iterations+1))
            if len(result) == max_iterations+1:
                result[-1] = '...'
            return result
        return solution

    def __init__(self, generator, datasets, max_iterations=None,
                 *args, **keywords):
        """
        a generator exercise is made with
        . a generator function for the solution
        . a list of Args instances to produce iterators that are then tested
        . max_iterations is a global limit on the number of items 
          that are attempted to be retrieved
        . additional settings from ExerciseFunction
        """
        solution = ExerciseGenerator.generator_to_solution(generator, max_iterations)
        ExerciseFunction.__init__(self, solution, datasets, *args, **keywords)
        self.generator = generator
        self.max_iterations = max_iterations

    def correction(self, student_generator):                    
        student_solution = ExerciseGenerator.generator_to_solution(
            student_generator, self.max_iterations)
        return ExerciseFunction.correction(self, student_solution)
