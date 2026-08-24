import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic multimodal components
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.exp(-0.1 * x**2) * np.sin(5 * x))
        term3 = np.sum(np.cos(3 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Coupling terms creating complex interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] * x[j]) / (1 + np.abs(x[i] - x[j]))
        
        # Add chaotic behavior with exponential decay
        chaotic = np.sum(np.exp(-np.abs(x)) * np.sin(np.pi * x))
        
        # Combine all terms
        return term1 + 0.5 * term2 + 0.3 * term3 + 0.1 * coupling + 0.2 * chaotic + 2.0