from time import perf_counter
import sympy as sp
import webbrowser
import urllib.parse

def bisection(func, x, a, b, tolerance):
    mid_point=0
    try:
        if func.subs(x, a)*func.subs(x, b) >= 0:
            print("The interval is invalid, there is no roots in it.")
        else:
            i=0
            print(f"\n===== BISECTION STARTING ON A={a} AND B={b} =====\n")
            start = perf_counter()
            while((b-a)>tolerance and i<500):
                i+=1
                mid_point = (b+a)/2
                fA, fMp, fB = func.subs(x, a), func.subs(x, mid_point), func.subs(x, b)
                print(f"Iteration {i} -----> f(a={a}) = {fA} | f(mid_point={mid_point}) = {fMp} | f(b={b}) = {fB}")
                if fMp*fA < 0:
                    b = mid_point
                    print(f"Moving B to midpoint (Moving left)\n")
                elif fMp*fB < 0:
                    a = mid_point
                    print(f"Moving A to midpoint (Moving right)\n")
                else:
                    print(f"Root found at {mid_point}")
            end = perf_counter()
            real_value = sp.nsolve(func, mid_point)
            time = end-start
            abs_error = abs(real_value-mid_point)
            rel_error = abs(real_value-mid_point)/abs(real_value)
            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT FOUND = {mid_point} (aprox)\nTOLERANCE: {tolerance:.15f}")
            print(f"REAL VALUE = {real_value}\nABSOLUTE ERROR = {abs_error:.15f}\nRELATIVE ERROR = {rel_error:.15f}\nTIME: {time} seconds")

    except Exception as e:
        print("An unknown error ocurred.",e) 

    return mid_point

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
b = float(input("Type the B value: "))
tolerance = 10**-int((input("Type the tolerance: ")))

bisection(func, x, a, b, tolerance)
#openGeogebra(func)