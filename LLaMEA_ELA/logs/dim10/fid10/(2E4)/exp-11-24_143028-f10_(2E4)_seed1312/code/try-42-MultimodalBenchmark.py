import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal components with cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.sin(12 * x[i]) * np.cos(9 * x[j]) * np.sin(5 * (x[i] + x[j]))
        
        # Stronger saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.6 * x[i]**5 - 1.0 * x[i]**4 + 0.7 * x[i]**3 - 0.4 * x[i]**2
        
        # Enhanced non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 0.9 * np.sin(20 * sum_x) * np.cos(18 * sum_x)
        
        # Global minimum penalty with exponential scaling
        result += 0.2 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Asymmetric cross-dimensional coupling with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.35 * np.sin(8 * x[i]) * np.cos(6 * x[j]) * np.tan(0.7 * (x[i] - x[j]))
        
        # Additional chaotic component with dynamic frequency and amplitude
        for i in range(self.dim):
            result += 0.3 * np.sin(11 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(7 * x[i])
        
        # Add a new term to increase the number of local minima
        for i in range(self.dim):
            result += 0.15 * np.sin(25 * x[i]) * np.cos(15 * x[i]) * (x[i]**2 + 1)
        
        # Fractal-like oscillation component to further increase complexity
        for i in range(self.dim):
            result += 0.25 * np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(20 * x[i]**2) * (1 + 0.1 * np.abs(x[i]))
        
        # Cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.18 * np.exp(-np.abs(x[i] - x[j]) / (1 + np.abs(x[i]) + np.abs(x[j]))) * np.sin(15 * (x[i] + x[j]))
        
        # Additional high-frequency chaotic term
        for i in range(self.dim):
            result += 0.12 * np.sin(35 * x[i]) * np.cos(30 * x[i]) * np.tan(2.5 * x[i])
        
        # New term: Increased complexity with nested trigonometric functions and polynomial interactions
        for i in range(self.dim):
            result += 0.18 * np.sin(40 * x[i]) * np.cos(35 * x[i]) * np.sin(30 * x[i]**3) * (1 + 0.05 * x[i]**2)
        
        # Additional nested fractal-like oscillation
        for i in range(self.dim):
            result += 0.22 * np.sin(45 * x[i]) * np.cos(40 * x[i]) * np.sin(35 * x[i]**4) * (1 + 0.08 * np.abs(x[i])**3)
        
        # Cross-dimensional hyperbolic coupling for increased non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.tanh(2.0 * x[i]) * np.sech(1.5 * x[j]) * np.sin(25 * (x[i] + x[j]))
        
        # Enhanced chaotic coupling with variable frequency modulation
        for i in range(self.dim):
            result += 0.14 * np.sin(50 * x[i] + 0.3 * np.sum(np.sin(x[:i]))) * np.cos(45 * x[i]) * (1 + 0.1 * np.abs(x[i]))
        
        # New high-order polynomial with chaotic modulation
        for i in range(self.dim):
            result += 0.08 * (x[i]**6 + 0.2 * np.sin(100 * x[i])) * np.cos(50 * x[i])
        
        return result