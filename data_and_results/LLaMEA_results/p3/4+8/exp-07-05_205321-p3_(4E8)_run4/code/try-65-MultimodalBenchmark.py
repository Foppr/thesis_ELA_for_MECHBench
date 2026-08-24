import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic particle interaction term
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                chaos += np.sin(10 * dist) * np.exp(-dist**2)
        
        # Gradient-based saddle point component
        gradient = 0.0
        for i in range(self.dim):
            gradient += (x_norm[i]**2 - 1.0)**2
        
        # Frequency-modulated sinusoidal waves
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3)  # Varying frequencies
            freq_mod += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial symmetry with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * np.sin(5 * r)
        
        # Combine all components
        return 0.25 * chaos + 0.35 * gradient + 0.25 * freq_mod + 0.15 * radial + 1.0