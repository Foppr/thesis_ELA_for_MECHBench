import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with hyperbolic tangent modulation
        base_quad = np.sum(np.tanh(x_norm) ** 2 * (1 + 0.3 * np.sin(7 * x_norm)))
        
        # Multi-scale periodic structures with varying amplitudes
        periodic_structure = 0.0
        for i in range(self.dim):
            periodic_structure += (0.6 * np.sin(12 * x_norm[i]) + 
                                  0.4 * np.cos(18 * x_norm[i]) + 
                                  0.3 * np.sin(25 * x_norm[i])) * \
                                 np.exp(-0.4 * x_norm[i]**2)
        
        # Asymmetric ridge interactions with exponential decay
        asymmetric_ridge = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            asymmetric_ridge += np.exp(-0.4 * np.abs(x_norm[i])) * \
                               np.sin(10 * x_norm[i] + 0.6 * x_norm[j]) * \
                               np.cos(7 * x_norm[i] - 0.4 * x_norm[j])
        
        # Hyperbolic tangent based fractal basin with chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.7 * np.tanh(6 * r) + 0.4 * np.sin(15 * r) * np.cos(8 * r) + \
                        0.3 * np.sin(25 * r) * np.cos(12 * r)
        
        # Cross-dimensional coupling with polynomial interaction and trigonometric modulation
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 4) % self.dim
            coupling_term += x_norm[i]**3 * x_norm[j] * np.cos(6 * x_norm[k]) * \
                            np.tanh(3 * x_norm[i]) * np.sin(4 * x_norm[j])
        
        # Final combined function with adaptive weighting and enhanced complexity
        return 0.35 * base_quad + 0.35 * periodic_structure + 0.2 * asymmetric_ridge + \
               0.1 * fractal_basin + 0.05 * coupling_term