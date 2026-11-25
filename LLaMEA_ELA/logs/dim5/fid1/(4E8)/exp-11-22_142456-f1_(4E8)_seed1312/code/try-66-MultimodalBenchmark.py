import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales and phase shifts
        for i in range(self.dim):
            scaled_x = (x[i] ** 2) * (i + 1) * 0.5
            phase_shift = np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            result += scaled_x + 0.2 * phase_shift
        
        # Add complex nested trigonometric interactions with multiple frequencies
        for i in range(self.dim):
            freq1 = 0.5 * (i + 1)
            freq2 = 0.3 * (i + 1)
            result += 10 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[(i + 1) % self.dim])
        
        # Add cross-dimensional interactions with higher-order terms
        for i in range(self.dim):
            result += 5 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[(i + 2) % self.dim]) * np.sin(0.4 * x[(i + 3) % self.dim])
        
        # Add a chaotic component using sine of sine terms
        for i in range(self.dim):
            result += 3 * np.sin(np.sin(0.9 * x[i]))
        
        # Add a large number of local minima through high-frequency trigonometric terms
        for i in range(self.dim):
            result += 8 * np.cos(3.0 * x[i]) * np.sin(2.5 * x[(i + 1) % self.dim])
        
        # Add noise-like perturbations to increase complexity
        result += 0.2 * np.sum(np.sin(1.5 * x) * np.cos(1.2 * x))
        
        return result