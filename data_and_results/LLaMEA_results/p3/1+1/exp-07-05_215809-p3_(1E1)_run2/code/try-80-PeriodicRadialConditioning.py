import numpy as np

class PeriodicRadialConditioning:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Radial component with periodic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(5 * r) + 0.2 * np.cos(3 * r)
        
        # Angular components with multiple frequencies
        angular_sum = 0.0
        for i in range(self.dim):
            angular_sum += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(4 * x_norm[i])
            
        # Multi-modal periodic structure with adaptive conditioning
        periodicity = 0.0
        for i in range(self.dim):
            # Adaptive frequency based on dimension
            freq = 2 + 0.5 * np.sin(i * 0.3)
            periodicity += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Combined landscape with global minimum at origin
        f = radial_term + 0.5 * angular_sum + 0.3 * periodicity
        
        # Add a structured noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(7 * x[i]) * np.cos(8 * x[i]) * np.sin(9 * x[i])
        f += noise
        
        # Add conditioning that increases difficulty near boundaries
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += 0.2 * (1 - np.exp(-0.5 * (x[i] / 5.0)**2)) * x[i]**2
        f += conditioning
        
        # Add a global scaling factor based on distance from origin
        global_scale = 1.0 + 0.5 * np.exp(-0.1 * r**2)
        f *= global_scale
        
        return f