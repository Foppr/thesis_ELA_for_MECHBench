import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # Exponentially decaying sinusoidal modulations
        for i in range(self.dim):
            f_value += 2.0 * np.exp(-0.1 * np.abs(x[i])) * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Polynomial cross-terms with varying exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.5 * (x[i]**3) * (x[j]**2) * np.sin(3 * x[i] + 2 * x[j])
                
        # Chaotic saddle-point components with multiple frequencies
        for i in range(self.dim):
            f_value += 1.5 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.sin(5 * x[i]) * np.cos(7 * x[i])
            
        # Multi-scale exponential decay with trigonometric perturbations
        for i in range(self.dim):
            f_value += 0.8 * np.exp(-0.05 * x[i]**2) * np.sin(15 * x[i]) * np.cos(12 * x[i])
            
        # Higher-order polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.3 * x[i]**5 * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Saddle-point structure with asymmetric cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.4 * (x[i]**2) * (x[j]**3) * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
                
        # Additional chaotic components with varying amplitudes
        f_value += 1.2 * np.sum(np.sin(8 * x) * np.cos(6 * x) * np.exp(-0.02 * x**2))
        
        # Asymmetric polynomial interactions
        for i in range(self.dim):
            f_value += 0.6 * x[i]**4 * np.sin(3 * x[i]) * np.cos(4 * x[i])
            
        # Cross-variable exponential decay with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.7 * np.exp(-0.1 * np.abs(x[i] - x[j])) * np.sin(6 * x[i]) * np.cos(8 * x[j])
                
        # Enhanced chaotic behavior with multi-modal sinusoidal components
        f_value += 0.9 * np.sum(np.sin(12 * x) * np.cos(9 * x) * np.sin(14 * x) * np.cos(11 * x))
        
        # Modified polynomial with exponential modulation
        for i in range(self.dim):
            f_value += 0.5 * x[i]**6 * np.exp(-0.03 * x[i]**2) * np.sin(5 * x[i])
            
        # Additional asymmetric cross-terms with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.3 * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * (x[i]**2) * (x[j]**4) * np.sin(x[i] + x[j])
                
        # Final chaotic component with complex multi-scale interactions
        f_value += 0.4 * np.sum(np.sin(18 * x) * np.cos(16 * x) * np.sin(17 * x) * np.cos(15 * x))
        
        return f_value