import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic base with conditioning
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal components with chaotic modulation
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        # Multi-scale exponential terms with irregular decay
        f3 = np.sum(np.exp(-x_normalized**2) * np.sin(6 * np.pi * x_normalized) * np.cos(4 * np.pi * x_normalized))
        
        # Complex interaction terms with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with non-polynomial coupling
                interaction += np.sin(3 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(5 * np.pi * (x_normalized[i] - x_normalized[j]))
                interaction += np.abs(x_normalized[i] - x_normalized[j])**(1.5 + 0.5 * np.sin(2 * np.pi * i))
        
        # Nested valleys with varying depths and widths
        nested = 0
        for i in range(self.dim):
            nested += (np.sin(8 * np.pi * x_normalized[i]) + 0.5 * np.sin(16 * np.pi * x_normalized[i]))**2
        
        # Add non-smooth regions with absolute value terms
        nonsmooth = np.sum(np.abs(x_normalized)**1.3)
        
        # Combine all components with dynamic weights
        result = 0.2 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * interaction + 0.1 * nested + 0.1 * nonsmooth
        
        # Add a chaotic periodic modulation to create many local minima
        chaotic_mod = np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(13 * np.pi * x_normalized) * np.tan(0.5 * np.pi * x_normalized))
        result += 0.08 * chaotic_mod
        
        # Introduce saddle points with negative curvature regions
        saddle = np.sum(x_normalized**6 - 3 * x_normalized**4 + 2 * x_normalized**2)
        result += 0.05 * saddle
        
        return result