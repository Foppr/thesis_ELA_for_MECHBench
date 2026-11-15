import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            f_value += 0.5 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
            
        # Exponential modulation with polynomial interactions
        for i in range(self.dim):
            f_value += 0.3 * np.exp(-0.5 * x[i]**2) * np.sin(5 * x[i])
            
        # High-dimensional cross-variable interactions with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * np.sin(8 * x[i] + 3 * x[j]) * np.cos(6 * x[i] - 2 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Multi-scale chaotic components with varying amplitudes
        f_value += 0.25 * np.sum(np.sin(25 * x) * np.cos(30 * x) * np.exp(-0.05 * x**2))
        
        # Polynomial chaos with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.35 * x[i]**9 * np.sin(7 * x[i])
            
        # Non-separable high-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_value += 0.2 * np.sin(5 * x[i] + 4 * x[j] + 3 * x[k]) * np.cos(6 * x[i] - 2 * x[j] + x[k])
                    
        # Exponential decay with sinusoidal perturbations
        f_value += 0.4 * np.sum(np.exp(-0.2 * x**2) * np.sin(12 * x))
        
        # Composite chaotic polynomial terms
        for i in range(self.dim):
            f_value += 0.2 * x[i]**10 * np.cos(4 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Multi-modal exponential interactions
        for i in range(self.dim):
            f_value += 0.3 * np.exp(-x[i]**2) * np.sin(15 * x[i]) * np.cos(10 * x[i])
            
        # Complex cross-dimensional coupling with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.25 * np.exp(-0.1 * (x[i] + x[j])**2) * np.sin(9 * x[i]) * np.cos(11 * x[j])
                
        # Higher-order chaotic polynomial with multi-scale sinusoidal modulation
        f_value += 0.3 * np.sum(x**11 * np.sin(3 * x) * np.cos(5 * x))
        
        # Additional chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.sin(12 * x[i]) * np.cos(14 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(8 * x[i] + 6 * x[j])
                
        # Add noise to increase irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        return f_value