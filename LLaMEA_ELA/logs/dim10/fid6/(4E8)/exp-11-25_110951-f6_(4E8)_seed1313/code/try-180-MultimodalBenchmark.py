import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with enhanced hyperbolic tangent modulation and chaotic perturbations
        base_quad = np.sum(np.tanh(x_norm ** 2) ** 2 * (1 + 0.3 * np.sin(7 * x_norm) * np.cos(3 * x_norm)))
        
        # Multi-scale periodic structures with increased complexity and varying amplitudes
        periodic_structure = 0.0
        for i in range(self.dim):
            periodic_structure += (0.6 * np.sin(12 * x_norm[i]) + 
                                  0.4 * np.cos(18 * x_norm[i]) + 
                                  0.3 * np.sin(25 * x_norm[i]) +
                                  0.2 * np.cos(30 * x_norm[i])) * \
                                 np.exp(-0.3 * x_norm[i]**2)
        
        # Asymmetric ridge interactions with enhanced exponential decay and cross-dimensional coupling
        asymmetric_ridge = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 3) % self.dim
            asymmetric_ridge += np.exp(-0.4 * np.abs(x_norm[i])) * \
                               np.sin(10 * x_norm[i] + 0.6 * x_norm[j] + 0.2 * x_norm[k]) * \
                               np.cos(7 * x_norm[i] - 0.4 * x_norm[j] + 0.3 * x_norm[k])
        
        # Modified fractal basin with chaotic perturbations and increased spectral complexity
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.7 * np.tanh(6 * r) + 0.4 * np.sin(15 * r) * np.cos(8 * r) + \
                        0.3 * np.sin(25 * r) * np.cos(12 * r) + 0.2 * np.cos(35 * r)
        
        # Cross-dimensional coupling with polynomial interaction, trigonometric modulation, and chaotic perturbations
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 4) % self.dim
            l = (i + 6) % self.dim
            coupling_term += x_norm[i]**3 * x_norm[j] * np.cos(6 * x_norm[k]) * \
                            np.tanh(3 * x_norm[i]) * np.sin(4 * x_norm[j]) * \
                            np.exp(-0.2 * np.abs(x_norm[l]))
        
        # Additional chaotic modulation term with dynamic phase interference
        chaos_modulation = 0.0
        for i in range(self.dim):
            chaos_modulation += np.sin(20 * x_norm[i] + np.sin(10 * x_norm[i])) * \
                               np.cos(15 * x_norm[i] + np.cos(8 * x_norm[i]))
        
        # Final combined function with adaptive weighting and enhanced complexity
        return 0.35 * base_quad + 0.25 * periodic_structure + 0.2 * asymmetric_ridge + \
               0.15 * fractal_basin + 0.05 * coupling_term + 0.05 * chaos_modulation