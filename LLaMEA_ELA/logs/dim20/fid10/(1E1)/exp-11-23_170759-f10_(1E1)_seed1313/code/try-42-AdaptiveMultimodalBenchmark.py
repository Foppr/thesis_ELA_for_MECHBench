import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base terms with dimension-dependent scaling
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) + 0.3 * (x[i] ** 3) + 0.1 * (x[i] ** 2)
        
        # Gaussian components with position-dependent variance and amplitude
        for i in range(self.dim):
            sigma = 1.0 + 0.5 * abs(x[i])
            result += 0.8 * np.exp(-0.5 * (x[i] / sigma) ** 2) * (1.0 + 0.2 * i)
        
        # Sinusoidal components with adaptive frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * (1.0 + 0.1 * abs(x[i]))
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Dynamic cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                result += 0.3 * np.exp(-dist) * np.sin(2.0 * (x[i] + x[j]))
        
        # Adaptive conditioning based on coordinate values
        for i in range(self.dim):
            if x[i] < 0:
                result += 0.25 * x[i] ** 2 * (1.0 + 0.1 * abs(x[i]))
            else:
                result += 0.3 * x[i] ** 2 * (1.0 + 0.05 * x[i])
        
        # High-frequency oscillatory component with dynamic amplitude
        for i in range(self.dim):
            result += 0.6 * np.sin(20.0 * x[i]) * (1.0 + 0.2 * np.sin(5.0 * x[i]))
        
        # Radial symmetry component with variable strength
        if self.dim >= 2:
            r = np.sqrt(np.sum(x**2))
            result += 0.5 * np.sin(3.0 * r) * np.exp(-0.1 * r)
        
        # Boundary attraction and repulsion terms
        for i in range(self.dim):
            boundary_term = 0.3 * (5.0 - abs(x[i])) ** 2
            if x[i] > 0:
                result += boundary_term * (1.0 + 0.1 * x[i])
            else:
                result += boundary_term * (1.0 + 0.05 * abs(x[i]))
        
        # Dimensionality-dependent modulation
        result *= (1.0 + 0.1 * self.dim)
        
        return result