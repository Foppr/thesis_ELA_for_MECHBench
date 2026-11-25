import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.9
        self.forcing_freq = 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Initialize chaotic system
        chaos_vals = np.zeros(self.dim)
        for i in range(self.dim):
            # Logistic map with coupling from previous dimensions
            if i == 0:
                chaos_vals[i] = 0.5
            else:
                chaos_vals[i] = self.logistic_r * chaos_vals[i-1] * (1 - chaos_vals[i-1])
            
            # Add periodic forcing
            chaos_vals[i] += 0.1 * np.sin(self.forcing_freq * x_norm[i])
            
            # Apply nonlinearity and coupling
            chaos_vals[i] = np.tanh(chaos_vals[i])**3
        
        # Combine with quadratic and sine components for multimodality
        quadratic_term = np.sum(x_norm**2)
        sine_term = np.sum(np.sin(3 * x_norm))
        chaotic_term = np.sum(chaos_vals**2)
        
        # Final function value with multiple competing forces
        return 0.5 * quadratic_term + 0.3 * sine_term + 0.2 * chaotic_term + 1.0