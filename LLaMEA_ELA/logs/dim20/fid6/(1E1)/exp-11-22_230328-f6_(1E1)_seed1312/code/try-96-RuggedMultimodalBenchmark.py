import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize periodic forcing parameters
        self.freqs = np.random.uniform(1.0, 3.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Initialize saddle point parameters
        self.saddle_strength = np.random.uniform(0.1, 1.0, dim)
        self.saddle_positions = np.random.uniform(-3.0, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic forcing term with amplitude modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += self.amps[i] * np.sin(self.freqs[i] * x_norm[i] + self.phase_shifts[i])
        
        # Saddle point structure creating complex local optima
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_strength[i] * (x_norm[i] - self.saddle_positions[i])**2 * \
                          np.exp(-0.5 * (x_norm[i] - self.saddle_positions[i])**2)
        
        # Non-separable cross-dimensional interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * \
                             np.exp(-0.1 * (x_norm[i] - x_norm[j])**2) * \
                             (i + j) / (self.dim * (self.dim + 1))
        
        # Sharp transition regions with exponential weighting
        transition_term = 0.0
        for i in range(self.dim):
            transition_term += np.exp(-5.0 * np.abs(x_norm[i])) * \
                              np.sin(3 * np.pi * x_norm[i]) * \
                              np.cos(2 * np.pi * x_norm[i])
        
        # Combined fitness landscape with adaptive scaling
        combined = periodic_term + saddle_term + cross_term + transition_term
        
        # Add noise and bias terms
        noise = 0.01 * np.random.uniform(-1, 1)
        bias = 0.1 * np.sum(np.sin(x_norm) * np.cos(x_norm))
        
        return combined + noise + bias