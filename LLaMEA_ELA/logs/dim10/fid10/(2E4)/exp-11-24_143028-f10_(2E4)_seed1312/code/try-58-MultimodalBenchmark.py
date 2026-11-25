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
                result += 1.2 * np.sin(20 * x[i]) * np.cos(15 * x[j]) * np.sin(8 * (x[i] + x[j]))
        
        # Stronger saddle point structure with higher-order polynomial terms
        for i in range(self.dim):
            result += 1.0 * x[i]**5 - 1.5 * x[i]**4 + 1.0 * x[i]**3 - 0.7 * x[i]**2
        
        # Enhanced non-separable high-frequency oscillations
        sum_x = np.sum(x)
        result += 1.5 * np.sin(30 * sum_x) * np.cos(25 * sum_x)
        
        # Global minimum penalty with exponential scaling
        result += 0.35 * np.exp(-np.sum(np.abs(x)) / self.dim)
        
        # Asymmetric cross-dimensional coupling with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.sin(15 * x[i]) * np.cos(12 * x[j]) * np.tan(1.2 * (x[i] - x[j]))
        
        # Additional chaotic component with dynamic frequency and amplitude
        for i in range(self.dim):
            result += 0.5 * np.sin(20 * x[i] + np.sum(x[:i]) if i > 0 else 0) * np.cos(12 * x[i])
        
        # Add a new term to increase the number of local minima
        for i in range(self.dim):
            result += 0.3 * np.sin(40 * x[i]) * np.cos(25 * x[i]) * (x[i]**2 + 1)
        
        # Fractal-like oscillation component to further increase complexity
        for i in range(self.dim):
            result += 0.45 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.sin(35 * x[i]**2) * (1 + 0.2 * np.abs(x[i]))
        
        # Cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.exp(-np.abs(x[i] - x[j]) / (1 + np.abs(x[i]) + np.abs(x[j]))) * np.sin(25 * (x[i] + x[j]))
        
        # Additional high-frequency chaotic term
        for i in range(self.dim):
            result += 0.2 * np.sin(50 * x[i]) * np.cos(45 * x[i]) * np.tan(4.0 * x[i])
        
        # Additional fractal-like component with increased complexity
        for i in range(self.dim):
            result += 0.35 * np.sin(60 * x[i]) * np.cos(55 * x[i]) * np.sin(40 * x[i]**3) * (1 + 0.25 * np.abs(x[i]))
        
        # Increased chaotic coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(25 * x[i]) * np.cos(20 * x[j]) * np.tan(1.1 * (x[i] + x[j]))
        
        # Additional term to improve fitness score by increasing problem difficulty
        for i in range(self.dim):
            result += 0.4 * np.sin(70 * x[i]) * np.cos(65 * x[i]) * np.tan(3.5 * x[i]) * (1 + 0.15 * x[i]**2)
        
        # Additional cross-dimensional coupling with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(30 * x[i]) * np.cos(25 * x[j]) * np.sin(20 * (x[i] - x[j])) * np.exp(-0.6 * (x[i]**2 + x[j]**2))
        
        # Fractal-like structure with higher frequency components
        for i in range(self.dim):
            result += 0.35 * np.sin(70 * x[i]) * np.cos(65 * x[i]) * np.sin(50 * x[i]**4) * (1 + 0.35 * np.abs(x[i]))
        
        # Add a new term to further increase complexity and local minima
        for i in range(self.dim):
            result += 0.4 * np.sin(80 * x[i]) * np.cos(75 * x[i]) * np.tan(5.0 * x[i]) * (1 + 0.2 * x[i]**3)
        
        # Cross-dimensional fractal coupling with enhanced non-separability
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.45 * np.sin(35 * x[i]) * np.cos(30 * x[j]) * np.sin(25 * (x[i]**2 + x[j]**2)) * np.exp(-0.4 * (x[i] - x[j])**2)
        
        # Additional high-order polynomial with chaotic oscillations
        for i in range(self.dim):
            result += 0.25 * x[i]**7 * np.sin(80 * x[i]) * np.cos(75 * x[i])
        
        # Boundary sensitivity enhancement
        boundary_penalty = 0
        for i in range(self.dim):
            if abs(x[i]) >= 4.9:
                boundary_penalty += 2.0 * (abs(x[i]) - 4.9)**2
        result += boundary_penalty
        
        return result