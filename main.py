import pylab
from sympy import diff, symbols, cos, sin
import numpy as np
from scipy import optimize
from mpl_toolkits.mplot3d import Axes3D


def graphics(x, y, z):
    fig = pylab.figure()
    axes = Axes3D(fig)

    axes.plot_surface(x, y, z)

    pylab.show()


def get_intervals():
    try:
        x_l = float(input("Enter the left border on the X-axis : "))
        x_r = float(input("Enter the right border on the X-axis : "))
        y_l = float(input("Enter the left border on the Y-axis : "))
        y_r = float(input("Enter the right border on the Y-axis : "))
        step = float(input("Enter the step of the grid : "))
    except:
        print("ERROR: Check the correctness of the entered data. The value must be integers or real numbers.")
        return -1
    if x_l > x_r or y_l > y_r:
        print("ERROR: The left border exceeds the value of the right.")
        return -1
    return [x_l, x_r, y_l, y_r, step]


def func(point):
    x, y = point
    #return np.sin(x) * np.sin(y)
    return x**2 * y**3


def makeData(x, y, step):
    x_ = np.arange(x[0], x[1], step[0])
    y_ = np.arange(y[0], y[1], step[0])

    x_grid, y_grid = np.meshgrid(x_, y_)

    z_grid = func([x_grid, y_grid])
    return x_grid, y_grid, z_grid


def get_derivative():
    x, y = symbols('x y')
    variables = (x, y)
    symbol_func = sin(x) * cos(y)
    symbol_func = x**2*y**3
    gr = (symbol_func.diff(x), symbol_func.diff(y))
    print("The function's gradient : ", gr)
    print("Enter the point to calculate the gradient")
    x_g = input("x : ")
    y_g = input("y : ")
    gr_x = gr[0].subs({x: x_g, y: y_g})
    gr_y = gr[1].subs({x: x_g, y: y_g})
    print("The gradient in the point is : (", gr_x, ",", gr_y, ")")
    derivatives = []
    for variable in variables:
        derivatives.append(diff(symbol_func, variable))
    print("The derivative of the function cos(x) * sin(x) is equal to : ", derivatives)


def main():
    input_data = get_intervals()
    if input_data == -1:
        print("The program ended with an error.\nClose")
        return -1
    x, y, z = makeData(input_data[0:2], input_data[2:4], input_data[4:])
    graphics(x, y, z)
    print("Calculating the local minimum value...")
    print("Enter the initial assumption point")
    while True:
        x_i = float(input("x : "))
        y_i = float(input("y : "))
        if input_data[0] <= x_i <= input_data[1] and input_data[2] <= y_i <= input_data[3]:
            break
        else:
            print("ERROR: The value entered is outside the interval")
    print("Local minimum : ", optimize.minimize(func, [x_i, y_i], tol=1e-6).x)
    get_derivative()


if __name__ == "__main__":
    #main()
    get_derivative()
