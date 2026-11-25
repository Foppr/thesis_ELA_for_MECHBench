import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with quadratic decay
        result = 0.5 * np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Multi-frequency trigonometric oscillations
        for i in range(self.dim):
            result += 2.0 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.tan(6 * x[i])
        
        # Radial basis function components with varying widths
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.5 * (x[i] - 2.0)**2) + 1.0 * np.exp(-0.3 * (x[i] + 3.0)**2)
        
        # Asymmetric boundary penalties
        for i in range(self.dim):
            if x[i] < 0:
                result += 3.0 * np.exp(-0.5 * (x[i] + 5.0)**2) * (1 + 0.5 * np.sin(15 * x[i]))
            else:
                result += 2.5 * np.exp(-0.3 * (x[i] - 5.0)**2) * (1 + 0.4 * np.cos(12 * x[i]))
        
        # Coupling between dimensions with sine modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.8 + 0.3 * np.sin(5 * (x[i] + x[j]))
                result += coupling * np.sin(7 * x[i]) * np.cos(9 * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # High-frequency chaotic modulation
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= np.sin(13 * x[i]) + 1.5
        result += 1.2 * chaos_factor
        
        # Fractal-like structure with recursive sine components
        for i in range(self.dim):
            result += 0.8 * np.sin(20 * x[i]) * np.cos(18 * x[i]) * np.sin(16 * x[i]**2) * (1 + 0.3 * np.abs(x[i]))
        
        # Weighted sum of polynomial and trigonometric terms
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**4 + 0.5 * x[i]**3 - 0.2 * x[i]**2
        result += 1.0 * poly_term * np.cos(5 * np.sum(x))
        
        # Cross-dimensional exponential interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.2 * np.abs(x[i] + x[j]))) * np.sin(10 * (x[i] + x[j]))
        
        # Additional asymmetric wave pattern
        sum_x = np.sum(x)
        result += 1.8 * np.sin(25 * sum_x) * np.cos(20 * sum_x) * (1 + 0.4 * np.tanh(sum_x))
        
        return result