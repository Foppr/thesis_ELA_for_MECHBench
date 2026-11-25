import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.freq_params = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute radial basis centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, dim)
        self.widths = 0.5 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add radial basis function component
        for i in range(self.dim):
            result += np.exp(-self.widths[i] * (x[i] - self.centers[i])**2)
            
        # Add sinusoidal oscillation component with varying frequencies
        for i in range(self.dim):
            result += np.sin(self.freq_params[i] * x[i]) * np.cos(0.5 * x[i])
            
        # Add cross-dimensional coupling with trigonometric interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                result += 0.1 * coupling * (i + j)
                
        # Add a modified Ackley-like term for enhanced multimodality
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        result += -20 * np.exp(-0.2 * np.sqrt(sum_sq / self.dim)) - np.exp(sum_cos / self.dim) + 20 + np.e
        
        # Add a periodic component with increasing frequency
        for i in range(self.dim):
            result += 0.05 * np.sin(10 * x[i]) * np.cos(8 * x[i])
            
        # Add conditioning through polynomial scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2)
        result += 0.01 * poly_term
        
        return result