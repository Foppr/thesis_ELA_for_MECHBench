import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic oscillation term with exponential barriers
        chaos_term = 0.0
        for i in range(self.dim):
            # Sinusoidal oscillations with varying frequencies
            chaos_term += np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i])
            # Add exponential barrier terms to create rugged landscape
            chaos_term += np.exp(-0.5 * (x[i] - 1.0)**2) + np.exp(-0.5 * (x[i] + 1.0)**2)
            # Cross-dimensional interactions
            if i > 0:
                chaos_term += 0.3 * np.sin(x[i-1]) * np.cos(x[i]) * np.sin(0.5 * x[i-1])
        
        # Add polynomial basin term for global convergence
        basin = 0.1 * np.sum(x**4)
        
        # Add noise-like perturbations for increased complexity
        noise = 0.05 * np.sum(np.sin(10 * x) + np.cos(10 * x))
        
        return chaos_term + basin + noise