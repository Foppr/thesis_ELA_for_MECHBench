import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add periodic trigonometric interactions with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) + 0.3 * np.sin(4 * x[i]) * np.cos(5 * x[(i + 2) % self.dim])
            
        # Add polynomial cross-dimensional terms with exponential decay
        for i in range(self.dim):
            f += 0.2 * x[i]**4 * np.exp(-0.1 * np.abs(x[(i + 1) % self.dim])) + 0.15 * x[i]**3 * np.exp(-0.05 * np.abs(x[(i + 2) % self.dim]))
            
        # Add sinusoidal coupling with decaying amplitude
        for i in range(self.dim):
            f += 0.25 * np.sin(6 * x[i] + 0.5 * x[(i + 1) % self.dim]) * np.exp(-0.2 * (x[i]**2 + x[(i + 1) % self.dim]**2))
            
        # Add multiple local minima using Gaussian-like bumps
        for i in range(self.dim):
            f += 0.3 * np.exp(-0.5 * ((x[i] - 1)**2 + (x[(i + 1) % self.dim] - 1)**2)) + 0.2 * np.exp(-0.5 * ((x[i] + 1)**2 + (x[(i + 1) % self.dim] + 1)**2))
            
        # Add non-linear coupling with logarithmic decay
        for i in range(self.dim):
            f += 0.1 * np.log(1 + np.abs(x[i]) + np.abs(x[(i + 1) % self.dim])) * x[i]**2
            
        # Add chaotic behavior via nested trigonometric functions
        for i in range(self.dim):
            f += 0.18 * np.sin(7 * np.sin(3 * x[i])) * np.cos(5 * np.cos(2 * x[(i + 1) % self.dim]))
            
        # Add higher-order polynomial penalties with varying exponents
        f += 0.1 * np.sum(np.abs(x)**4.2) + 0.08 * np.sum(x**6)
        
        return f