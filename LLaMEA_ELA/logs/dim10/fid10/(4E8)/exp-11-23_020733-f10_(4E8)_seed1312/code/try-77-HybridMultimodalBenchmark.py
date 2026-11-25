import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.5
        
        # Sinusoidal oscillation components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            amp = 1.5 + 0.3 * np.cos(i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function terms with varying centers and widths
        centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        for i in range(min(8, self.dim)):
            center = centers[i]
            width = 0.8 + 0.2 * np.sin(i)
            dist = np.sum((x - center)**2)
            result += 0.8 * np.exp(-dist / (2 * width**2)) * np.cos(3 * dist)
        
        # Cross-dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) + 0.5 * np.cos(x[i] + x[j])
                result += 0.3 * coupling * (1 + 0.2 * np.sin(i + j))
        
        # Asymmetric saddle points with varying steepness
        for i in range(self.dim):
            result += 0.2 * x[i]**4 - 0.5 * x[i]**2 + 0.1 * np.sin(10 * x[i])
        
        # Multi-scale periodic components
        for i in range(self.dim):
            result += 0.15 * np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.tan(3 * x[i])
        
        # Boundary penalty and conditioning variation
        boundary_penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.5:
                boundary_penalty += 10 * (abs(x[i]) - 4.5)**2
        result += boundary_penalty
        
        # Global scaling factor
        result *= 1.5
        
        return result