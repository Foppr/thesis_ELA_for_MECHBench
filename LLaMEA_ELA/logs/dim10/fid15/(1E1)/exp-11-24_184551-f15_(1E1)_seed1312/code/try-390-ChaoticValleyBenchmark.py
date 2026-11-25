import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Base polynomial penalty term
        poly_term = np.sum(x**4) * 0.01
        
        # Sinusoidal wave components creating chaotic valleys
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Additional chaotic component with varying frequencies
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(5.0 * x[i] + np.cos(7.0 * x[i])) * 0.5
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * 0.05
                
        # Global minimum at origin with small perturbations
        base_value = poly_term - sin_term + chaos_term + cross_term
        
        # Add a small random noise component to increase challenge
        noise = np.random.normal(0, 0.01)
        
        return base_value + noise