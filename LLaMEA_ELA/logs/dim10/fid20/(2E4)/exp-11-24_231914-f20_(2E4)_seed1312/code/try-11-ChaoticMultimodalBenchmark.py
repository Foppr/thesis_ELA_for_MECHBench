import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with global minimum at origin
        f_val = np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies
        for i in range(self.dim):
            f_val += 2.0 * np.sin(3.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Add exponential decay terms that create rugged terrain
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(4.0 * x[i])
            
        # Cross-dimensional interaction terms creating complex correlations
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                f_val += 0.3 * np.sin(x[i]) * np.cos(x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Add a chaotic component with high-frequency oscillations
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(100.0 * x[i]) * np.cos(50.0 * x[i])
        f_val += 0.1 * chaotic_term
        
        # Add a penalty for being far from the feasible region to encourage convergence
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                penalty += 10.0 * (abs(x[i]) - 4.0)**2
        f_val += penalty
        
        return f_val