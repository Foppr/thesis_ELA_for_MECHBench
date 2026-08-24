import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_normalized = x / 5.0
        
        # Quadratic term with severe conditioning
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with chaotic behavior
        f2 = np.sum(np.sin(20 * np.pi * x_normalized)**4 + 0.3 * np.sin(50 * np.pi * x_normalized)**3)
        
        # Multi-modal Gaussian terms with varying scales and positions
        f3 = np.sum(np.exp(-5 * x_normalized**2) * np.cos(5 * np.pi * x_normalized) + 
                   0.5 * np.exp(-0.5 * (x_normalized - 0.5)**2) * np.sin(10 * np.pi * x_normalized))
        
        # Complex interaction terms with chaotic coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with non-linear coupling
                interaction += (x_normalized[i]**3 + x_normalized[j]**3) * np.sin(5 * np.pi * (x_normalized[i] - x_normalized[j])) * np.cos(2 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Multi-scale global structure with fractal-like properties
        global_structure = np.sum(np.abs(x_normalized)**5 + 0.5 * np.abs(x_normalized)**7 + 0.1 * np.abs(x_normalized)**9)
        
        # Add a chaotic noise term to increase complexity
        noise = np.sum(np.sin(100 * x_normalized) * np.cos(75 * x_normalized))
        
        # Combine all terms with adaptive weights
        result = 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.1 * interaction + 0.1 * global_structure + 0.05 * noise
        
        return result