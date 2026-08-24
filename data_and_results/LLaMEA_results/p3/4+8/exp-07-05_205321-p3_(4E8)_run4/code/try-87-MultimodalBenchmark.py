import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic particle interaction term with modified coupling
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                chaos += np.sin(15 * dist) * np.exp(-dist**2.5)
        
        # Gradient-based saddle point component with higher-order terms
        gradient = 0.0
        for i in range(self.dim):
            gradient += (x_norm[i]**4 - 2*x_norm[i]**2 + 1.0)**2
        
        # Frequency-modulated sinusoidal waves with phase shifts
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 3**(i % 4)  # Different frequency progression
            phase_shift = np.pi * (i / self.dim)
            freq_mod += np.sin(freq * x_norm[i] + phase_shift) * np.cos(freq * x_norm[i] + phase_shift)
        
        # Radial symmetry with modified decay and added harmonic term
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2.2) * (np.sin(6 * r) + 0.5 * np.cos(3 * r))
        
        # Additional cross-dimensional coupling term
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_norm[i] * x_norm[j]) * (i + j)
        
        # Combine all components with adjusted weights
        return 0.3 * chaos + 0.4 * gradient + 0.2 * freq_mod + 0.08 * radial + 0.02 * cross_coupling + 1.0