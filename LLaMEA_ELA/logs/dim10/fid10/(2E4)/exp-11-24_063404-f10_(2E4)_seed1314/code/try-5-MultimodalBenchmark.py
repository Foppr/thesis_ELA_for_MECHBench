import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (1.0 + 0.5 * np.sin(3 * r))
        
        # Angular component with multiple frequencies
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            angular = np.sum([np.sin((i+1) * angles) * np.cos((i+1) * angles) 
                             for i in range(min(3, self.dim))])
        else:
            angular = 0.0
            
        # High-frequency oscillation component
        oscillation = np.sum(np.sin(10 * x_scaled)**2 + np.cos(7 * x_scaled)**2)
        
        # Combined function with multiple competing terms
        return radial + 0.3 * angular + 0.1 * oscillation + 0.001 * np.sum(x_scaled**4)