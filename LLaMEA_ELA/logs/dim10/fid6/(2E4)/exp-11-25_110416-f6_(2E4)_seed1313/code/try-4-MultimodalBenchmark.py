import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_normalized**2))
        
        # Sinusoidal oscillations with exponentially decaying amplitude
        oscillation = np.sum(np.exp(-r) * np.sin(10 * np.pi * r)**2)
        
        # Quadratic penalty for distance from origin
        quadratic = 0.5 * r**2
        
        # Additional high-frequency noise terms
        noise = np.sum(np.sin(50 * x_normalized)**2)
        
        # Combine all components
        return quadratic + oscillation + 0.1 * noise