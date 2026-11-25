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
                result += 0.9 * np.sin(15 * x[i]) * np.cos(10 * x[j]) * np.sin(6 * (x[i] + x[j]))
        
        # Stronger saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 0.7 * x[i]**5 - 1.2 * x[i]**4 + 0.8 * x[i]**3 - 0.5 * x[i]**2
        
        # Enhanced non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 1.0 * np.sin(25 * sum_x) * np.cos(20 * sum_x)
        
        # Global minimum penalty with exponential scaling
        result += 0.25 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Asymmetric cross-dimensional coupling with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(10 * x[i]) * np.cos(8 * x[j]) * np.tan(0.8 * (x[i] - x[j]))
        
        # Additional chaotic component with dynamic frequency and amplitude
        for i in range(self.dim):
            result += 0.35 * np.sin(13 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(8 * x[i])
        
        # Add a new term to increase the number of local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(30 * x[i]) * np.cos(18 * x[i]) * (x[i]**2 + 1)
        
        # Fractal-like oscillation component to further increase complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(35 * x[i]) * np.cos(30 * x[i]) * np.sin(25 * x[i]**2) * (1 + 0.15 * np.abs(x[i]))
        
        # Cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.exp(-np.abs(x[i] - x[j]) / (1 + np.abs(x[i]) + np.abs(x[j]))) * np.sin(20 * (x[i] + x[j]))
        
        # Additional high-frequency chaotic term
        for i in range(self.dim):
            result += 0.15 * np.sin(40 * x[i]) * np.cos(35 * x[i]) * np.tan(3.0 * x[i])
        
        # Additional fractal-like component with increased complexity
        for i in range(self.dim):
            result += 0.22 * np.sin(45 * x[i]) * np.cos(40 * x[i]) * np.sin(30 * x[i]**3) * (1 + 0.2 * np.abs(x[i]))
        
        # Increased chaotic coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.28 * np.sin(18 * x[i]) * np.cos(14 * x[j]) * np.tan(0.9 * (x[i] + x[j]))
        
        # Additional term to improve fitness score by increasing problem difficulty
        for i in range(self.dim):
            result += 0.3 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.tan(2.5 * x[i]) * (1 + 0.1 * x[i]**2)
        
        # Additional cross-dimensional coupling with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.32 * np.sin(22 * x[i]) * np.cos(17 * x[j]) * np.sin(15 * (x[i] - x[j])) * np.exp(-0.5 * (x[i]**2 + x[j]**2))
        
        # Fractal-like structure with higher frequency components
        for i in range(self.dim):
            result += 0.25 * np.sin(55 * x[i]) * np.cos(50 * x[i]) * np.sin(40 * x[i]**4) * (1 + 0.3 * np.abs(x[i]))
        
        # Add a new term to further increase complexity and local minima
        for i in range(self.dim):
            result += 0.28 * np.sin(60 * x[i]) * np.cos(55 * x[i]) * np.tan(4.0 * x[i]) * (1 + 0.15 * x[i]**3)
        
        # Cross-dimensional fractal coupling with enhanced non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.35 * np.sin(28 * x[i]) * np.cos(24 * x[j]) * np.sin(20 * (x[i]**2 + x[j]**2)) * np.exp(-0.3 * (x[i] - x[j])**2)
        
        # Additional high-order polynomial with chaotic oscillations
        for i in range(self.dim):
            result += 0.18 * x[i]**6 * np.sin(65 * x[i]) * np.cos(60 * x[i])
        
        return result