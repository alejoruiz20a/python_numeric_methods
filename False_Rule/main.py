import timeit
import sympy as sp
import webbrowser
import urllib.parse

x = sp.symbols('x')
func = sp.exp(-x) + sp.tan(x) - ((sp.exp(x)*sp.sin(x))**-1) 
derivative = sp.diff(func,x)

a = float(input("Type the A value: "))
b = float(input("Type the B value: "))
tolerance = 10**-int((input("Type the tolerance: ")))

def falseRule(func, a, b, tolerance, overloop_prevention):
    try:
        if (func(a)*func(b))>=0:
            print("The interval is invalid, there is no roots in it.")
        else:
            xr=0
            prev_xr = None
            i=0
            print(f"===== FALSE RULE STARTING ON A={a} AND B={b} =====\n")
            while((b-a)>tolerance and i<500):
                i+=1
                prev_xr = xr
                fA, fB = func(a), func(b)
                xr = b - ((fB*(b-a))/(fB-fA))
                fXr = func(xr)

                # OVERLOOP PREVENTION
                if overloop_prevention and prev_xr is not None and abs(xr - prev_xr) < tolerance:
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

            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT = {xr} (aprox)\nTOLERANCE: {tolerance}")
    except Exception as e:
        print("An unknown error ocurred.",e) 

def openGeogebra(func):
    func_str = f"y={sp.simplify(func)}"
    func_url = urllib.parse.quote(func_str)  

    url = f"https://www.geogebra.org/graphing?command={func_url}"
    webbrowser.open(url)

time = format(timeit.timeit(lambda: falseRule(sp.lambdify(x, func, modules=['numpy']), a, b, tolerance, True), number=1),'.20f')
print(f"TIME: {time} seconds")
openGeogebra(func)