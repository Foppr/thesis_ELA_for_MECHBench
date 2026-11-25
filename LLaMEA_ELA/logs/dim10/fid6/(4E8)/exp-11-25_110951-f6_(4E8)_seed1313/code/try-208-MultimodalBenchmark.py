import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay potentials with varying scales
        potential_term = 0.0
        for i in range(self.dim):
            potential_term += np.exp(-np.abs(x_norm[i])) * (1 + 0.5 * np.sin(3 * x_norm[i]))
        
        # Sinusoidal modulations with multi-frequency components
        sinusoidal_term = 0.0
        frequencies = [2, 4, 6, 8]
        for i in range(self.dim):
            for freq in frequencies:
                sinusoidal_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] / 2)
        
        # Asymmetric elliptic structures with cross-dimensional coupling
        elliptic_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            elliptic_term += (x_norm[i]**2 + 0.5 * x_norm[j]**2) * \
                           np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j])
        
        # Multi-scale harmonic interference with amplitude modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(10 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2) + \
                           0.3 * np.cos(15 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Cross-dimensional interaction with polynomial coupling
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x_norm[i] * x_norm[j])**3 + (x_norm[i] + x_norm[j])**2
        
        # Asymmetric gradient modulation with logarithmic scaling
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += np.log(1 + np.abs(x_norm[i])) * np.sin(5 * x_norm[i])
        
        # Final combined function with dynamic weighting
        return 0.3 * potential_term + 0.25 * sinusoidal_term + 0.2 * elliptic_term + \
               0.1 * harmonic_term + 0.1 * poly_term + 0.05 * grad_term