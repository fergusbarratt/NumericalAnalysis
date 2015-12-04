'''Differential Equation solvers in python'''
from __future__ import division
import numpy as np


class DiffEq:
    '''DiffEq solvers'''
    def __init__(self, *args, **kwargs):
        self.a = args[0]
        self.b = args[1]
        self.c = args[2]
        self.euler_step_size = 1/1000
        self.runge_kutta_step_size = 1/1000

    def __str__(self):
        return '%d+%dt+%dx'%(self.a, self.b, self.c)

    def rhs(self, t=None, x=None):
        if t is None and x is None:
            raise Exception('set x and t')
        if t is not None and x is None:
            x = 0
        return self.a+self.b*t+self.c*x

    def euler_solution(self, t, initial_condition=[0, 0]):
        h = self.euler_step_size
        initial_time = initial_condition[1]
        y = initial_condition[0]
        for time in np.linspace(initial_time, t, (t/h)+1):
            y = y + h*self.rhs(
                time + h, y)
        return y

    def runge_kutta_solution(self, t, initial_condition=[0., 0.], noisy=False):
        h = self.runge_kutta_step_size
        initial_time = initial_condition[1]
        y = initial_condition[0]
        for time in np.linspace(
                initial_time, t, (t/h)+1):
            K1 = self.rhs(time, y)
            K2 = self.rhs(time + h/2, y + (h/2) * K1)
            K3 = self.rhs(time + h/2, y + (h/2) * K2)
            K4 = self.rhs(time + h, y+h*K3)
            y = y + (h/6) * (K1 + 2*K2 + 2*K3 + K4)
            if noisy:
                print '\nK1: ', K1, ' K2: ', K2, ' K3: ', K3, 'K4: ', K4
                print y, time
        return y

    def leapfrog_solution(self, t=None):
        pass

    def symbolic_solution(self, t=None):
        if t is None:
            return 'need t'
        if self.c:
            return 'no hardcoded solution'
        if not self.a and not self.b:
            return 0
        if self.a and self.b:
            return self.a*t+(self.b*t**2)/2
        elif self.a:
            return self.a*t
        elif self.b:
            return (self.b*t**2)/2
        else:
            return 'No hardcoded symbolic solution'


def test_diff_eq(noisy=True):
    '''x doesn't work'''
    diff_eq = DiffEq(0, 1, 0)
    # analytic solution?: t^2/2
    x = 5
    if noisy:
        print 'eqn: ', diff_eq
        print 'Actual at %d: '%x, diff_eq.symbolic_solution(x)
        print 'Euler at %d: '%x, diff_eq.euler_solution(x)
        print 'Runge-Kutta at %d: '%x, diff_eq.runge_kutta_solution(x)


test_diff_eq()
