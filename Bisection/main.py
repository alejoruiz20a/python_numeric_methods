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

def bisection(func, a, b, tolerance):
    try:
        if func(a)*func(b) >= 0:
            print("The interval is invalid, there is no roots in it.")
        else:
            i=0
            mid_point=0
            print(f"===== BISECTION STARTING ON A={a} AND B={b} =====\n")
            while((b-a)>tolerance and i<500):
                i+=1
                mid_point = (b+a)/2
                fA, fMp, fB = func(a), func(mid_point), func(b)
                print(f"Iteration {i} -----> f(a={a}) = {fA} | f(mid_point={mid_point}) = {fMp} | f(b={b}) = {fB}")
                if fMp*fA < 0:
                    b = mid_point
                    print(f"Moving B to midpoint (Moving left)\n")
                elif fMp*fB < 0:
                    a = mid_point
                    print(f"Moving A to midpoint (Moving right)\n")
                else:
                    print(f"Root found at {mid_point}")
            print(f"BISECTION FINISHED AT {i} ITERATIONS.\nROOT = {mid_point} (aprox)\nTOLERANCE: {tolerance}")

    except Exception as e:
        print("An unknown error ocurred.") 

def openGeogebra(func):
    func_str = f"y={sp.simplify(func)}"
    func_url = urllib.parse.quote(func_str)  

    url = f"https://www.geogebra.org/graphing?command={func_url}"
    webbrowser.open(url)

time = format(timeit.timeit(lambda: bisection(sp.lambdify(x, func, modules=['numpy']), a, b, tolerance), number=1),'.20f')
print(f"TIME: {time} seconds")
openGeogebra(func)

