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
            # Enhanced sinusoidal oscillations with varying frequencies and amplitudes
            chaos_term += (np.sin(x[i]) * np.cos(2 * x[i]) * np.sin(3 * x[i]) + 
                          0.5 * np.sin(0.5 * x[i]) * np.cos(1.5 * x[i]))
            # Add exponential barrier terms to create rugged landscape
            chaos_term += np.exp(-0.3 * (x[i] - 1.0)**2) + np.exp(-0.3 * (x[i] + 1.0)**2)
            # Cross-dimensional interactions with more complex coupling
            if i > 0:
                chaos_term += 0.4 * np.sin(x[i-1]) * np.cos(x[i]) * np.sin(0.7 * x[i-1]) * np.cos(0.3 * x[i])
        
        # Add polynomial basin term for global convergence with modified coefficients
        basin = 0.05 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Add noise-like perturbations with different frequency components
        noise = 0.03 * np.sum(np.sin(15 * x) + np.cos(15 * x) + np.sin(7 * x) * np.cos(7 * x))
        
        # Add a new term to improve conditioning and challenge optimization algorithms more effectively
        conditioning_term = 0.02 * np.sum(np.abs(x)**3)
        
        return chaos_term + basin + noise + conditioning_term