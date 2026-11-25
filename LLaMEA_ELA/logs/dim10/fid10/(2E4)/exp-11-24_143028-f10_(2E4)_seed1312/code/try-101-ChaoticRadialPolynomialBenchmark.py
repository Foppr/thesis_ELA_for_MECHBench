import numpy as np

class ChaoticRadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial quadratic term with exponential decay
        result = 0.5 * np.sum(x**2) * np.exp(-0.1 * np.sum(x**2))
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.0 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i]**2) + \
                      1.5 * np.cos(13 * x[i]) * np.sin(9 * x[i]) * np.cos(4 * x[i]**3)
        
        # Radial basis functions with dynamic widths
        for i in range(self.dim):
            result += 1.8 * np.exp(-0.3 * (x[i] - 2.0)**2) + \
                      1.2 * np.exp(-0.5 * (x[i] + 3.0)**2) + \
                      0.9 * np.exp(-0.4 * (x[i] - 1.5)**2)
        
        # Cross-dimensional polynomial coupling with quintic terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                result += 0.8 * (x[i]**5 + x[j]**5) * np.sin(3 * (x[i] - x[j]))
        
        # Asymmetric boundary penalties with hyperbolic tangent
        for i in range(self.dim):
            if x[i] < 0:
                result += 1.5 * np.exp(-0.2 * (x[i] + 5.0)**2) * np.tanh(3 * x[i])
            else:
                result += 1.3 * np.exp(-0.3 * (x[i] - 5.0)**2) * np.tanh(2 * x[i])
        
        # High-frequency chaotic modulation with multiple sine components
        chaos_mod = 1.0
        for i in range(self.dim):
            chaos_mod *= np.sin(18 * x[i]) + np.cos(16 * x[i]) + np.sin(14 * x[i]**2)
        result += 1.2 * chaos_mod
        
        # Fractal-like structure with recursive sine components
        for i in range(self.dim):
            result += 0.8 * np.sin(20 * x[i]) * np.cos(18 * x[i]) * np.sin(16 * x[i]**2)
        
        # Weighted sum of polynomial and trigonometric terms with cubic interaction
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**4 + 0.7 * x[i]**3 - 0.4 * x[i]**2 + 0.2 * x[i]
        result += 1.0 * poly_term * np.cos(5 * np.sum(x))
        
        # Cross-dimensional exponential interaction with cosine coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.exp(-np.abs(x[i] - x[j]) / (1 + 0.2 * np.abs(x[i] + x[j]))) * np.cos(10 * (x[i] - x[j]))
        
        # Additional asymmetric wave pattern with logarithmic scaling
        sum_x = np.sum(x)
        result += 1.8 * np.sin(25 * sum_x) * np.cos(20 * sum_x) * (1 + 0.3 * np.log(np.abs(sum_x) + 1))
        
        # Cross-dimensional polynomial coupling with septic terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.4 * (x[i]**7 + x[j]**7) * np.cos(4 * (x[i] - x[j]))
        
        # Additional high-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.2 * np.sin(40 * x[i]) * np.cos(35 * x[i])
        result += noise
        
        return result