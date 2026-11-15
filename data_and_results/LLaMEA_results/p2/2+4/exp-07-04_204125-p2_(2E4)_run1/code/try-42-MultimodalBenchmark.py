import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Radial component with periodic modulation
        r_squared = np.sum(x**2)
        result += 0.5 * r_squared + 0.3 * np.sin(5.0 * np.sqrt(r_squared))
        
        # Multi-scale trigonometric terms
        for i in range(self.dim):
            result += 0.8 * np.sin(2.0 * np.pi * x[i]) + 0.4 * np.cos(3.0 * np.pi * x[i])
            
            # Adaptive conditioning based on dimension
            condition_factor = 1.0 + 0.2 * np.sin(0.5 * i)
            result += 0.1 * condition_factor * x[i]**4
            
            # Cross-term interactions with periodic coupling
            if i > 0:
                result += 0.05 * np.sin(4.0 * (x[i] - x[i-1])) * np.cos(2.0 * (x[i] + x[i-1]))
        
        # Add a structured noise component with fractal-like scaling
        noise = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                noise += np.exp(-0.1 * dist**2) * np.sin(10.0 * dist)
        result += 0.08 * noise
        
        # Add dimensionality-dependent scaling
        result *= (1.0 + 0.05 * self.dim)
        
        return result