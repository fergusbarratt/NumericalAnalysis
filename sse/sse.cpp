// Copyright 2015 Fergus Barratt
#include <iostream>
#include <string>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::vector;
using std::endl;
// using std::map; //for initial solutions

class FirstOrderLinearAutonomousEquation {
 private:
  double a;
  double b;
  std::vector<double> initial_values;
  double euler_step_size;
  int params_size;

 public:
  FirstOrderLinearAutonomousEquation(double ain, double bin,
    double t_initial, double f_initial);
    double rhs(double y, double t);
    double euler_solution(double t);
};

FirstOrderLinearAutonomousEquation::FirstOrderLinearAutonomousEquation
(double ain, double bin, double t_initial, double f_initial) {
  a = ain;
  b = bin;
  initial_values;
  euler_step_size = 1;
  initial_values[0] = t_initial;
  initial_values[1] = f_initial;
}

double FirstOrderLinearAutonomousEquation::rhs(double y, double t) {
  double result = a+b*y;
  return result;
}

double FirstOrderLinearAutonomousEquation::euler_solution(double t) {
  double last_step = initial_values[1];
  for (double i=initial_values[0]; i+=euler_step_size; t) {
    double next_step = last_step+euler_step_size*rhs(last_step, t);
    last_step = next_step;
  }
  return last_step;
}

int main(int argc, char* argv[]) {
  FirstOrderLinearAutonomousEquation eqn(0.0, 1.0, 0.0, 0.0);
  std::cout << eqn.rhs(2, 0);
  return 0;
}
