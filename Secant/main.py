from time import perf_counter
import sympy as sp
import webbrowser
import urllib.parse

def newtonRaphson(func, x, x0, x1, tolerance):
    try:
        if func.subs(x, x0) == 0 or func.subs(x, x1) == 0:
            print("The given starting value is a root.")
        else:
            i = 0
            print(f"\n===== SECANT STARTING ON x0={x0} AND x1={x1} =====\n")
            start = perf_counter()
            while i<500:
                i+=1
                fx0, fx1 = func.subs(x, x0), func.subs(x, x1)
                if fx1 - fx0 == 0:
                    print("Division by zero reached.")
                    break
                x2 = x1 - (fx1*(x1-x0))/(fx1-fx0)
                print(f"Iteration {i} -----> f(x0={x0}) = {fx0} | f'(x1={x1}) = {fx1} | x2 = {x2}\n")

                if abs(x2-x1)<tolerance:
                    print("CONVERGENCE REACHED")
                    break
                else:
                    x0 = x1
                    x1 = x2

            end = perf_counter()
            real_value = sp.nsolve(func, x2)
            time = end-start
            abs_error = abs(real_value-x2)
            rel_error = abs(real_value-x2)/abs(real_value)
            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT FOUND = {x2} (aprox)\nTOLERANCE: {tolerance:.15f}")
            print(f"REAL VALUE = {real_value}\nABSOLUTE ERROR = {abs_error:.15f}\nRELATIVE ERROR = {rel_error:.15f}\nTIME: {time} seconds")

    except Exception as e:
        print("An unknown error ocurred.", e) 

    return x2

def openGeogebra(func):
    func_str = f"y={sp.simplify(func)}"
    func_url = urllib.parse.quote(func_str)  

    url = f"https://www.geogebra.org/graphing?command={func_url}"
    webbrowser.open(url)

# OPERATING AREA

x = sp.symbols('x')
func = sp.exp(-x) + sp.tan(x) - ((sp.exp(x)*sp.sin(x))**-1) 
d_func = sp.diff(func,x)

x0 = float(input("Type the x0 value: "))
x1 = float(input("Type the x1 value: "))
tolerance = 10**-int((input("Type the tolerance: ")))

newtonRaphson(func, x, x0, x1, tolerance)
#openGeogebra(func)