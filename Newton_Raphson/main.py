from time import perf_counter
import sympy as sp
import webbrowser
import urllib.parse

def newtonRaphson(func, d_func, x, a, tolerance):
    try:
        if func.subs(x, a) == 0:
            print("The given starting value is a root.")
        else:
            i = 0
            print(f"\n===== NEWTON-RAPHSON STARTING ON A={a} =====\n")
            start = perf_counter()
            while i<500:
                i+=1
                fA, fdA = func.subs(x, a), d_func.subs(x, a)
                b = a - (fA/fdA)
                print(f"Iteration {i} -----> f(a={a}) = {fA} | f'(a={a}) = {fdA} | b = {b}\n")

                if abs(b-a)<tolerance:
                    print("CONVERGENCE REACHED")
                    break
                else:
                    a = b

            end = perf_counter()
            real_value = sp.nsolve(func, a)
            time = end-start
            abs_error = abs(real_value-a)
            rel_error = abs(real_value-a)/abs(real_value)
            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT FOUND = {a} (aprox)\nTOLERANCE: {tolerance:.15f}")
            print(f"REAL VALUE = {real_value}\nABSOLUTE ERROR = {abs_error:.15f}\nRELATIVE ERROR = {rel_error:.15f}\nTIME: {time} seconds")

    except Exception as e:
        print("An unknown error ocurred.", e) 

    return a

def openGeogebra(func):
    func_str = f"y={sp.simplify(func)}"
    func_url = urllib.parse.quote(func_str)  

    url = f"https://www.geogebra.org/graphing?command={func_url}"
    webbrowser.open(url)

# OPERATING AREA

x = sp.symbols('x')
func = sp.exp(-x) + sp.tan(x) - ((sp.exp(x)*sp.sin(x))**-1) 
d_func = sp.diff(func,x)

a = float(input("Type the A value: "))
tolerance = 10**-int((input("Type the tolerance: ")))

newtonRaphson(func, d_func, x, a, tolerance)
#openGeogebra(func)