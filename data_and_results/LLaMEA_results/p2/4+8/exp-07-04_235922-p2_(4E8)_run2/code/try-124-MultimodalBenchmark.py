import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial chaos with trigonometric modulation
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**8 - 28*xi**6 + 350*xi**4 - 1750*xi**2 + 3125
            trig_term = np.sin(2 * xi) * np.cos(3 * xi) + 0.5 * np.sin(5 * xi) * np.cos(7 * xi)
            result += 0.1 * poly_term * trig_term
        
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) + np.cos(0.4 * x[i]) * np.sin(0.6 * x[j])
                result += 0.3 * coupling * (x[i]**2 + x[j]**2)
        
        # Add radial adaptive barriers
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += (x[i] - 1.5)**2 + (x[i] + 1.5)**2
        barrier = 0.5 * np.exp(-0.1 * radial_sum) + 0.3 * np.exp(-0.05 * radial_sum**2)
        result += barrier
        
        # Add dynamic conditioning based on dimensionality
        conditioning = 1.0 + 0.1 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4) + 0.05 * np.sin(self.dim * 0.9)
        result *= conditioning
        
        # Add multi-scale sinusoidal modulation
        modulate = 0.0
        for i in range(self.dim):
            modulate += np.sin(4 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.02 * x[i]**2) + 0.2 * np.sin(9 * x[i]) * np.cos(11 * x[i]) * np.exp(-0.01 * x[i]**2)
        result += 0.2 * modulate
        
        # Add noise component with polynomial scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.03 * x[i]**2) + 0.1 * np.sin(15 * x[i]) * np.cos(14 * x[i])
        result += 0.01 * noise
        
        return result