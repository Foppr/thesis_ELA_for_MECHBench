import numpy as np

class QuasiPeriodicSumOfSquares:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sum-of-squares base term
        sos_term = np.sum(x_scaled**2)
        
        # Quasiperiodic trigonometric components with dimensionality-dependent frequencies
        qp_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * (i + 1) / self.dim  # Varying frequencies per dimension
            qp_term += np.sin(freq * np.pi * x_scaled[i])**2 + \
                      np.cos(freq * np.pi * x_scaled[i])**2
        
        # Adaptive cross-dimensional coupling with varying strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.3 * (i + 1) / self.dim * (j + 1) / self.dim
                cross_term += coupling_strength * np.sin(np.pi * x_scaled[i]) * np.cos(np.pi * x_scaled[j])
        
        # Dimensionality-dependent harmonic modulation
        harm_mod = 0.0
        for i in range(self.dim):
            harm_mod += (0.5 + 0.5 * np.sin(4.0 * np.pi * x_scaled[i])) * \
                       (1.0 + 0.2 * np.cos(3.0 * np.pi * x_scaled[i]))
        
        # Combined function with optimized weights
        return 0.7 * sos_term + 0.8 * qp_term + 0.4 * cross_term + 0.3 * harm_mod + 1.5