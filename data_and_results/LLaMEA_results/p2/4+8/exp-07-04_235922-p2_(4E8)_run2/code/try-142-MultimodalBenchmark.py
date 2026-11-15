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
            trig_term = np.sin(2.2 * xi) * np.cos(3.1 * xi) + 0.55 * np.sin(5.3 * xi) * np.cos(7.2 * xi)
            result += 0.11 * poly_term * trig_term
        
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.55 * x[i]) * np.cos(0.35 * x[j]) + np.cos(0.42 * x[i]) * np.sin(0.63 * x[j])
                result += 0.32 * coupling * (x[i]**2 + x[j]**2)
        
        # Add radial adaptive barriers
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += (x[i] - 1.6)**2 + (x[i] + 1.4)**2
        barrier = 0.52 * np.exp(-0.11 * radial_sum) + 0.32 * np.exp(-0.055 * radial_sum**2)
        result += barrier
        
        # Add dynamic conditioning based on dimensionality
        conditioning = 1.0 + 0.11 * np.sin(self.dim * 0.72) * np.cos(self.dim * 0.41) + 0.052 * np.sin(self.dim * 0.91)
        result *= conditioning
        
        # Add multi-scale sinusoidal modulation
        modulate = 0.0
        for i in range(self.dim):
            modulate += np.sin(4.1 * x[i]) * np.cos(6.1 * x[i]) * np.exp(-0.021 * x[i]**2) + 0.21 * np.sin(9.1 * x[i]) * np.cos(11.1 * x[i]) * np.exp(-0.011 * x[i]**2)
        result += 0.21 * modulate
        
        # Add noise component with polynomial scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(12.1 * x[i]) * np.cos(10.1 * x[i]) * np.exp(-0.031 * x[i]**2) + 0.11 * np.sin(15.1 * x[i]) * np.cos(14.1 * x[i])
        result += 0.011 * noise
        
        return result