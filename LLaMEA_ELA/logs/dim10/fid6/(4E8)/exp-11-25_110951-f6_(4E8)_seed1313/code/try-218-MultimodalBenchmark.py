import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay potentials with varying scales and chaotic modulation
        potential_term = 0.0
        for i in range(self.dim):
            potential_term += np.exp(-np.abs(x_norm[i])) * (1 + 0.5 * np.sin(3 * x_norm[i]) + 
                                                           0.3 * np.sin(7 * x_norm[i]) * np.cos(11 * x_norm[i]))
        
        # Sinusoidal modulations with multi-frequency components and fractal-like structure
        sinusoidal_term = 0.0
        frequencies = [2, 4, 6, 8, 10]
        for i in range(self.dim):
            for j, freq in enumerate(frequencies):
                sinusoidal_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] / (j + 1)) * \
                                  np.sin(2 * np.pi * x_norm[i] * (j + 1))
        
        # Asymmetric elliptic structures with cross-dimensional coupling and chaotic interference
        elliptic_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            elliptic_term += (x_norm[i]**2 + 0.5 * x_norm[j]**2 + 0.3 * x_norm[k]**2) * \
                           np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j]) * \
                           np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Multi-scale harmonic interference with amplitude modulation and chaotic coupling
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += (np.sin(10 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2) + 
                             0.3 * np.cos(15 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2) +
                             0.1 * np.sin(25 * x_norm[i]) * np.cos(30 * x_norm[i]))
        
        # Cross-dimensional interaction with polynomial coupling and fractal basin modification
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x_norm[i] * x_norm[j])**3 + (x_norm[i] + x_norm[j])**2 + \
                            0.5 * np.sin(5 * x_norm[i]) * np.cos(5 * x_norm[j])
        
        # Asymmetric gradient modulation with logarithmic scaling and chaotic perturbation
        grad_term = 0.0
        for i in range(self.dim):
            grad_term += (np.log(1 + np.abs(x_norm[i])) * np.sin(5 * x_norm[i]) + 
                         0.2 * np.cos(13 * x_norm[i]) * np.sin(17 * x_norm[i]))
        
        # Fractal basin enhancement with multi-scale harmonic interference
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += (np.sin(50 * x_norm[i]) * np.cos(40 * x_norm[i]) + 
                            0.7 * np.sin(30 * x_norm[i])**2 * np.cos(20 * x_norm[i]))
        
        # Final combined function with dynamic weighting and chaotic scaling
        return (0.25 * potential_term + 0.2 * sinusoidal_term + 0.15 * elliptic_term + 
                0.1 * harmonic_term + 0.08 * poly_term + 0.07 * grad_term + 0.1 * fractal_term)