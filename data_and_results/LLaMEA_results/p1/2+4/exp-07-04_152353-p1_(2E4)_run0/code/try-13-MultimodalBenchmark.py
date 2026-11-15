import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Strongly conditioned quadratic term
        f1 = np.sum((x_normalized**2) * (2**(np.arange(self.dim))))
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = np.sum(2.0 * np.sin(15 * np.pi * x_normalized)**2 + 
                   1.5 * np.sin(30 * np.pi * x_normalized)**2 + 
                   0.8 * np.sin(45 * np.pi * x_normalized)**2)
        
        # Multi-scale Gaussian terms with different widths and centers
        f3 = np.sum(np.exp(-3 * x_normalized**2) * np.cos(5 * np.pi * x_normalized) + 
                   0.5 * np.exp(-0.5 * (x_normalized - 0.3)**2) * np.sin(10 * np.pi * x_normalized) + 
                   0.3 * np.exp(-2 * (x_normalized + 0.5)**2) * np.cos(7 * np.pi * x_normalized))
        
        # Complex interaction terms with multiple coupling patterns
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear coupling with different interaction strengths
                interaction += (x_normalized[i]**3 + x_normalized[j]**3) * np.sin(5 * np.pi * (x_normalized[i] - x_normalized[j])) + \
                              (x_normalized[i]**2 * x_normalized[j] + x_normalized[i] * x_normalized[j]**2) * np.cos(2 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Enhanced global structure with multiple local minima
        global_structure = np.sum(np.abs(x_normalized)**5 + 0.5 * np.abs(x_normalized)**7 + 0.2 * np.abs(x_normalized)**9)
        
        # Add periodic boundary effects
        periodic = np.sum(np.sin(8 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        # Combine all terms with carefully adjusted weights
        result = 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.1 * interaction + 0.1 * global_structure + 0.05 * periodic
        
        return result