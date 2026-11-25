import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.frequencies = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, dim)
        self.widths = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            amplitude = 1.0 + 0.3 * np.sin(i * 0.5)
            result += amplitude * np.sin(self.frequencies[i] * x[i]) * np.cos(2 * self.frequencies[i] * x[i])
            
        # Add radial basis function components
        for i in range(self.dim):
            result += np.exp(-self.widths[i] * (x[i] - self.centers[i])**2)
            
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling * np.sin(x[i] * x[j]) * np.cos(0.5 * (i - j))
                
        # Add a modified Schwefel function component for global optimization challenge
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.01 * schwefel_term
        
        # Add a multi-modal component with multiple local minima
        multimodal_term = 0.0
        for i in range(self.dim):
            multimodal_term += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10)
        result += 0.02 * multimodal_term
        
        # Add noise to increase irregularity
        noise = 0.005 * np.sum(np.sin(x * 15))
        result += noise
        
        return result