import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic term for basin attraction
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal terms with different frequencies and amplitudes
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Additional high-frequency oscillation to increase complexity
        f3 = np.sum(np.sin(10 * np.pi * x_norm**2))
        
        # Add a small noise term to make the landscape more complex
        noise = 0.05 * np.random.random()
        
        return f1 + 0.2 * f2 + 0.1 * f3 + noise