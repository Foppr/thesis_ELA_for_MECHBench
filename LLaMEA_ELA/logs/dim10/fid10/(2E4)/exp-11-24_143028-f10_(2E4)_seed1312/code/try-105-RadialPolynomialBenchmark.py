import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term with quartic decay
        result = 0.3 * np.sum(x**4) * np.exp(-0.15 * np.sum(x**2))
        
        # Multi-frequency polynomial oscillations
        for i in range(self.dim):
            result += 1.8 * x[i]**5 * np.sin(12 * x[i]) * np.cos(9 * x[i])
        
        # Radial basis function components with varying widths and phases
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.4 * (x[i] - 2.5)**2) + 1.2 * np.exp(-0.2 * (x[i] + 3.5)**2) + 0.8 * np.exp(-0.6 * (x[i] - 1.0)**2)
        
        # Asymmetric boundary penalties with cubic terms
        for i in range(self.dim):
            if x[i] < 0:
                result += 2.8 * np.exp(-0.4 * (x[i] + 5.0)**3) * (1 + 0.6 * np.sin(18 * x[i]))
            else:
                result += 2.2 * np.exp(-0.2 * (x[i] - 5.0)**3) * (1 + 0.5 * np.cos(14 * x[i]))
        
        # Coupling between dimensions with cosine modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.9 + 0.4 * np.cos(6 * (x[i] - x[j]))
                result += coupling * np.cos(8 * x[i]) * np.sin(10 * x[j]) * np.exp(-0.15 * (x[i] + x[j])**2)
        
        # High-frequency chaotic modulation with multiple sine waves
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= np.sin(15 * x[i]) + np.cos(17 * x[i]) + 1.8
        result += 1.5 * chaos_factor
        
        # Fractal-like structure with recursive cosine components
        for i in range(self.dim):
            result += 1.0 * np.cos(25 * x[i]) * np.sin(22 * x[i]) * np.cos(20 * x[i]**2) * (1 + 0.4 * np.abs(x[i]))
        
        # Weighted sum of polynomial and trigonometric terms with cubic interaction
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**5 + 0.6 * x[i]**4 - 0.3 * x[i]**3 + 0.1 * x[i]**2
        result += 1.2 * poly_term * np.sin(6 * np.sum(x))
        
        # Cross-dimensional exponential interaction with sine coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.3 * np.abs(x[i] + x[j]))) * np.cos(12 * (x[i] - x[j]))
        
        # Additional asymmetric wave pattern with hyperbolic tangent
        sum_x = np.sum(x)
        result += 2.1 * np.sin(30 * sum_x) * np.cos(25 * sum_x) * (1 + 0.5 * np.tanh(2 * sum_x))
        
        # Cross-dimensional polynomial coupling with quintic terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.5 * (x[i]**3 + x[j]**3) * np.sin(5 * (x[i] - x[j]))
        
        # Additional high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(50 * x[i]) * np.cos(45 * x[i])
        result += noise
        
        return result