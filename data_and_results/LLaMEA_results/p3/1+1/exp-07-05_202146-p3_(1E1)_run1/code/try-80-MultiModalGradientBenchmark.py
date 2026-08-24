import numpy as np

class MultiModalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation coefficients for sinusoidal interactions
        self.correlation_coeffs = np.array([np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sinusoidal correlation structure with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * self.correlation_coeffs[i]
            
        # Polynomial interaction terms with increasing degree
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.2 * x[i]**3
            
        # Multi-scale sinusoidal modulation with distance-based decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.3 * np.sin(3.0 * dist) * np.exp(-0.1 * dist)
                
        # Gradient-based basin complexity with directional influence
        grad_influence = 0.0
        for i in range(self.dim):
            grad_influence += 0.2 * x[i] * np.sin(x[i] * 0.5)
        result += grad_influence
        
        # High-frequency oscillatory component with local maxima
        for i in range(self.dim):
            result += 0.15 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
            
        # Cross-dimensional polynomial coupling with non-linear interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                
        # Multi-modal structure with multiple local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Asymmetric ridge structure with varying amplitude
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.1 * np.sin(3.0 * x[i]) * np.cos(1.0 * x[i]) * (1.0 + 0.2 * np.sin(i * 0.3))
        result += ridge_term
        
        # Memory-like effect through cumulative influence
        if hasattr(self, 'prev_x'):
            memory_effect = 0.0
            for i in range(self.dim):
                memory_effect += 0.08 * (x[i] - self.prev_x[i]) * np.sin(x[i])
            result += memory_effect
        self.prev_x = x.copy()
        
        # Add noise to increase ruggedness
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(15.0 * x[i]) * np.cos(7.5 * x[i])
        result += noise
        
        return result