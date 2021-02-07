
# QUESTION 1
#
# # x = xdot
# x(0) = 1
# # Functions -
# eulers_step: single eulers_step
# solve_to: solve from x1t1 --> x2t2 in steps no bigger than delatt_max
# deltat_max: max deltat
# solve_ode: uses solve_to and eulers_step to generate a series of numerical solution estimates x1,x2,x3

# ESTIMATE X(1) USING DIFFERENT TIMESTEPS
# SHOW HOW THE ERROR DEPENDS ON THE SIZE OF THE TIMESTEP/

x0 = 1
t0 = 0
tmax = 1
n = 5
h = (tn - t0)/n
xvalues = []

x1 = x0 + h*f(x0,t0)



def func(x,t):
    return(x)



def eulers_step(x,t,f):
    # for i in range(1e-16 to tmax):
    for i in range(0-n):
        x = (i) + h*func(x,t)
        xvalues.append(i)

        x2 = x1 + h*func(x1, t1)
        




x =
