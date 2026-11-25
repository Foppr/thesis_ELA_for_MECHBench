import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for each dimension
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.interference_strength = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x / 5.0) * np.pi
        
        # Base sinusoidal components with adaptive frequencies and amplitudes
        sin_terms = np.sum(self.amplitudes * np.sin(self.frequencies * x_norm + self.phase_shifts))
        
        # Adaptive frequency modulation based on position
        modulated_freq = self.frequencies * (1.0 + 0.3 * np.sin(x_norm))
        modulated_terms = np.sum(self.amplitudes * np.sin(modulated_freq * x_norm + self.phase_shifts))
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Interference term with distance-based decay and phase modulation
                dist = np.abs(x[i] - x[j])
                phase_diff = np.abs(self.phase_shifts[i] - self.phase_shifts[j])
                interference += (self.interference_strength[i] * 
                               np.cos(dist * 0.5) * 
                               np.sin(phase_diff) * 
                               np.exp(-dist**2 * 0.1))
        
        # Adaptive basin boundaries with improved scaling
        boundary_terms = 0.0
        for i in range(self.dim):
            # Asymmetric boundary effects with improved nonlinearity
            if x[i] < 0:
                boundary_terms += (np.sin(x[i]**2) * np.exp(-x[i]) + 
                                 0.1 * np.cos(x[i]**3) * np.sin(x[i]))
            else:
                boundary_terms += (np.cos(x[i]**2) * np.exp(-x[i]**2) + 
                                 0.1 * np.sin(x[i]**3) * np.cos(x[i]))
        
        # Combined objective function with improved weighting
        return (0.3 * sin_terms**2 + 
                0.35 * modulated_terms**2 + 
                0.25 * interference + 
                0.1 * boundary_terms)