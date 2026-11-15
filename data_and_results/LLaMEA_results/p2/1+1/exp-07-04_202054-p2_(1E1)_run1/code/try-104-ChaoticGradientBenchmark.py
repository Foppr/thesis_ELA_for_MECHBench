import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum
        f_value = np.sum(x**2)
        
        # Chaotic component using logistic map-like behavior
        for i in range(self.dim):
            f_value += 0.5 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(12 * x[i])
            
        # Saddle point structure with mixed positive/negative curvature
        for i in range(self.dim):
            f_value += 0.3 * x[i]**3 * np.sin(5 * x[i])
            
        # Multi-scale sinusoidal modulation with varying frequencies
        f_value += 0.4 * np.sum(np.sin(20 * x) * np.cos(15 * x) * np.sin(25 * x))
        
        # Cross-variable interaction with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.25 * np.sin(6 * x[i]) * np.cos(9 * x[j]) * np.sin(4 * x[i] + 3 * x[j]) * np.cos(7 * x[i] - 2 * x[j])
                
        # High-frequency oscillation with amplitude modulation
        f_value += 0.35 * np.sum(np.sin(30 * x)**2 + np.cos(25 * x)**2)
        
        # Variable-dependent curvature with exponential modulation
        for i in range(self.dim):
            f_value += 0.2 * np.exp(-x[i]**2) * np.sin(15 * x[i])
            
        # Multi-modal structure with irregular peaks
        f_value += 0.25 * np.sum(np.sin(40 * x) * np.cos(35 * x) * np.sin(45 * x))
        
        # Cross-term with complex trigonometric interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.2 * np.sin(8 * x[i]) * np.cos(11 * x[j]) * np.sin(6 * x[i] + 5 * x[j]) * np.cos(9 * x[i] - 4 * x[j]) * np.sin(7 * x[i] + 3 * x[j])
                
        # Asymmetric polynomial with chaotic behavior
        for i in range(self.dim):
            f_value += 0.15 * x[i]**5 * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Add noise to create irregularity
        noise = np.random.normal(0, 0.05, self.dim)
        f_value += 0.1 * np.sum(noise * x)
        
        # Enhanced cross-variable coupling with multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.18 * np.sin(12 * x[i]) * np.cos(14 * x[j]) * np.sin(10 * x[i] + 8 * x[j]) * np.cos(6 * x[i] - 5 * x[j])
                
        # Add irregular bumps for challenge
        for i in range(self.dim):
            f_value += 0.2 * np.sin(60 * x[i]) * np.cos(40 * x[i]) * np.sin(50 * x[i])
            
        # Additional chaotic component with varying phase
        f_value += 0.3 * np.sum(np.sin(22 * x) * np.cos(18 * x) * np.sin(24 * x))
        
        # Final polynomial with strong nonlinearity
        for i in range(self.dim):
            f_value += 0.2 * x[i]**8 * np.sin(4 * x[i])
            
        return f_value