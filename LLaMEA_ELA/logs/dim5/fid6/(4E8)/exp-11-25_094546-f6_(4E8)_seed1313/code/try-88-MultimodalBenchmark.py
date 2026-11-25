import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like probabilistic landscape with tunneling effects
        prob_term = np.sum(np.sin(3 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Entangled dimension coupling with quantum correlation
        entangle_factor = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                entangle_factor += np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(np.pi * (x_norm[i] - x_norm[j]))
        
        # Dynamic energy barriers with time-dependent modulation
        barrier_mod = np.sum(2.0 + np.sin(4 * x_norm) * np.cos(2 * x_norm))
        
        # Discrete-local optima with continuous interpolation
        discrete_optima = np.sum(np.floor(10 * np.abs(x_norm)) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Continuous chaotic component with fractional dimensionality
        frac_dim = 1.5 + 0.5 * np.sin(2 * x_norm)
        chaotic_term = np.sum(np.abs(x_norm)**frac_dim * np.cos(5 * x_norm))
        
        # Combine all components with quantum-inspired weights
        return 1.5 * prob_term + 0.8 * entangle_factor + 1.2 * barrier_mod + 0.6 * discrete_optima + 0.9 * chaotic_term