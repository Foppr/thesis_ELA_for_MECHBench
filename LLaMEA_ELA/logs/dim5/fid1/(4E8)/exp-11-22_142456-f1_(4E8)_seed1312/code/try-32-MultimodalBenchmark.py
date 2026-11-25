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
            scaled_x = (x[i] ** 2) * (i + 1) * 0.3
            phase_shift = np.sin(0.4 * x[i]) * np.cos(0.6 * x[i])
            result += scaled_x + 0.3 * phase_shift
        
        # Add complex nested trigonometric interactions with multiple frequencies
        for i in range(self.dim):
            freq1 = 0.6 * (i + 1)
            freq2 = 0.4 * (i + 1)
            result += 12 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[(i + 1) % self.dim])
        
        # Add cross-dimensional interactions with higher-order terms
        for i in range(self.dim):
            result += 6 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[(i + 2) % self.dim]) * np.sin(0.3 * x[(i + 3) % self.dim])
        
        # Add a chaotic component using sine of sine terms
        for i in range(self.dim):
            result += 4 * np.sin(np.sin(0.8 * x[i]))
        
        # Add a large number of local minima through high-frequency trigonometric terms
        for i in range(self.dim):
            result += 10 * np.cos(2.5 * x[i]) * np.sin(3.0 * x[(i + 1) % self.dim])
        
        # Add noise-like perturbations to increase complexity
        result += 0.3 * np.sum(np.sin(1.8 * x) * np.cos(1.4 * x))
        
        # Add exponential scaling to increase function complexity
        for i in range(self.dim):
            result += 2 * np.exp(-0.1 * (x[i] ** 2)) * np.sin(1.5 * x[i])
        
        return result