import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_normalized**2)
        
        # Sinusoidal terms with multiple frequencies and amplitudes
        f2 = np.sum(np.sin(12 * np.pi * x_normalized)**2 + 0.6 * np.sin(25 * np.pi * x_normalized)**2)
        
        # Gaussian-like terms with varying widths
        f3 = np.sum(np.exp(-2.5 * x_normalized**2) * np.cos(3.5 * np.pi * x_normalized))
        
        # Interaction terms with non-linear coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_normalized[i]**2 + x_normalized[j]**2) * np.sin(4 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Add a more complex global minimum structure
        global_structure = np.sum(0.8 * np.abs(x_normalized)**4 + 0.4 * np.abs(x_normalized)**6 + 0.2 * np.abs(x_normalized)**8)
        
        # Combine all terms with adaptive weights
        result = 0.35 * f1 + 0.3 * f2 + 0.25 * f3 + 0.05 * interaction + 0.05 * global_structure
        
        return result