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
            poly_term = xi**7 - 21*xi**5 + 245*xi**3 - 1225*xi
            trig_term = np.sin(1.5 * xi) * np.cos(2.5 * xi) + 0.3 * np.sin(4 * xi) * np.cos(6 * xi)
            result += 0.15 * poly_term * trig_term
        
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.3 * x[i]) * np.cos(0.2 * x[j]) + np.cos(0.5 * x[i]) * np.sin(0.4 * x[j])
                result += 0.25 * coupling * (x[i]**2 + x[j]**2)
        
        # Add radial adaptive barriers
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += (x[i] - 2.0)**2 + (x[i] + 2.0)**2
        barrier = 0.6 * np.exp(-0.15 * radial_sum) + 0.2 * np.exp(-0.03 * radial_sum**2)
        result += barrier
        
        # Add dynamic conditioning based on dimensionality
        conditioning = 1.0 + 0.15 * np.sin(self.dim * 0.8) * np.cos(self.dim * 0.5) + 0.06 * np.sin(self.dim * 1.1)
        result *= conditioning
        
        # Add multi-scale sinusoidal modulation
        modulate = 0.0
        for i in range(self.dim):
            modulate += np.sin(3.5 * x[i]) * np.cos(5.5 * x[i]) * np.exp(-0.015 * x[i]**2) + 0.25 * np.sin(8.5 * x[i]) * np.cos(10.5 * x[i]) * np.exp(-0.008 * x[i]**2)
        result += 0.25 * modulate
        
        # Add noise component with polynomial scaling
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(11 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.025 * x[i]**2) + 0.12 * np.sin(14 * x[i]) * np.cos(13 * x[i])
        result += 0.015 * noise
        
        return result