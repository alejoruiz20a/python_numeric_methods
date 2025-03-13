from time import perf_counter
import sympy as sp
import webbrowser
import urllib.parse

def falseRule(func, x, a, b, tolerance, overloop_prevention):
    try:
        if (func.subs(x, a)*func.subs(x, b))>=0:
            print("The interval is invalid, there is no roots in it.")
        else:
            xr=0
            prev_xr = None
            i=0
            print(f"\n===== FALSE RULE STARTING ON A={a} AND B={b} =====\n")
            start = perf_counter()
            while((b-a)>tolerance and i<500):
                i+=1
                prev_xr = xr
                fA, fB = func.subs(x, a), func.subs(x, b)
                xr = b - ((fB*(b-a))/(fB-fA))
                fXr = func.subs(x, xr)
                # OVERLOOP PREVENTION
                if overloop_prevention and prev_xr is not None and abs(xr - prev_xr)/xr < tolerance:
                    break

                print(f"Iteration {i} -----> f(a={a}) = {fA} | f(Xr={xr}) = {fXr} | f(b={b}) = {fB}")

                if fXr==0:
                    print(f"Raiz encontrada: {xr}")
                
                if (fA*fXr)<0:
                    b = xr
                    print(f"Moving B to Xr (Moving left)\n")
                else:
                    a = xr
                    print(f"Moving A to Xr (Moving right)\n")
            end = perf_counter()
            real_value = sp.nsolve(func, xr)
            time = end-start
            abs_error = abs(real_value-xr)
            rel_error = abs(real_value-xr)/abs(real_value)
            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT FOUND = {xr} (aprox)\nTOLERANCE: {tolerance:.15f}")
            print(f"REAL VALUE = {real_value}\nABSOLUTE ERROR = {abs_error:.15f}\nRELATIVE ERROR = {rel_error:.15f}\nTIME: {time} seconds")

    except Exception as e:
        print("An unknown error ocurred.",e) 

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

falseRule(func, x, a, b, tolerance, True)
#openGeogebra(func)