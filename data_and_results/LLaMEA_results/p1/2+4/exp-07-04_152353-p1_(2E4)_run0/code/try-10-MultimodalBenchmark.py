import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_normalized**4)
        
        # Trigonometric components with multiple frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized))
        
        # Radial basis function component
        f3 = np.sum(np.exp(-5.0 * np.sum((x_normalized.reshape(1, -1) - x_normalized.reshape(-1, 1))**2, axis=1)))
        
        # Non-separable interaction terms with exponential coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.exp(-0.5 * (x_normalized[i] - x_normalized[j])**2) * np.sin(2 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Add a global sinusoidal modulation
        modulation = np.sin(0.5 * np.sum(x_normalized**2))
        
        # Combine all terms with different weights
        result = 0.3 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * interaction + 0.05 * modulation
        
        # Add a small perturbation term to increase complexity
        result += 0.01 * np.sum(np.sin(10 * x_normalized) * np.cos(7 * x_normalized))
        
        return result