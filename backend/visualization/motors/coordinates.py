
import math

def cylindricalToCartesian(r,theta,h):
        return (r*math.cos(theta), r*math.sin(theta), h)
    
    # Returns theta in [-pi/2, pi/2]
def cartesianToCylindrical(x,z,y):
        theta = 0;
        if (x > 0):
            theta = math.atan(z/x)
        elif (x==0):
            if (z>0):
                theta = math.pi/2
            else:
                theta = -math.pi/2
        elif (x < 0 and z > 0):
            theta = math.atan(z/x)+math.pi
        else:
            theta = math.atan(z/x)-math.pi

        return (math.sqrt(x*x + z*z), theta, y)

print(cylindricalToCartesian(1,math.pi/2,1))
print(cartesianToCylindrical(6.123233995736766e-17, 1.0, 1))
print(cylindricalToCartesian(1,-7*math.pi/16,1))
print((1,-7*math.pi/16,1))
print(cartesianToCylindrical(0.19509032201612833, -0.9807852804032304, 1))