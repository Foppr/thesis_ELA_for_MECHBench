import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic with adaptive conditioning and noise
        base_quad = np.sum(x_norm**2 * (1 + 0.3 * np.sin(7 * x_norm) * np.cos(4 * x_norm)))
        
        # Adaptive ridge structure with varying curvature and phase shifts
        ridge_structure = 0.0
        for i in range(self.dim):
            ridge_structure += np.exp(-0.5 * (x_norm[i] - 0.5)**2) * np.sin(16 * x_norm[i]) + \
                              0.7 * np.exp(-0.3 * (x_norm[i] + 0.3)**2) * np.cos(13 * x_norm[i])
        
        # Dynamic phase interference with time-varying frequencies
        phase_interference = 0.0
        for i in range(self.dim):
            phase_interference += np.sin(9 * x_norm[i] + 0.5 * np.sin(4 * x_norm[i])) * \
                                np.cos(7 * x_norm[i] + 0.3 * np.cos(5 * x_norm[i]))
        
        # Exponentially decaying harmonic modulations with cross-dimensional coupling
        harmonic_modulation = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            harmonic_modulation += np.exp(-2.5 * np.abs(x_norm[i])) * \
                                  np.sin(11 * x_norm[i] + 3 * x_norm[j]) * \
                                  np.cos(8 * x_norm[i] - 2 * x_norm[j])
        
        # Multi-scale fractal-like basin with chaotic perturbations
        r = np.sqrt(np.sum(x_norm**2))
        fractal_basin = 0.8 * np.exp(-r**2) + 0.4 * np.sin(16 * r) * np.cos(9 * r) + \
                        0.3 * np.sin(26 * r) * np.cos(13 * r) + 0.1 * np.sin(36 * r)
        
        # Cross-dimensional polynomial coupling with variable interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            k = (i + 5) % self.dim
            coupling_term += x_norm[i]**2 * x_norm[j] * x_norm[k] * \
                            np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[j]) * \
                            np.exp(-0.15 * np.abs(x_norm[k]))
        
        # Mutation: Slightly increased coupling strength and added cubic interaction
        cubic_interaction = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 4) % self.dim
            cubic_interaction += x_norm[i]**3 * x_norm[j] * x_norm[k] * \
                               np.sin(6 * x_norm[i]) * np.cos(9 * x_norm[j]) * \
                               np.exp(-0.25 * np.abs(x_norm[k]))
        
        # Final combined function with adaptive weighting and enhanced complexity
        return 0.35 * base_quad + 0.25 * ridge_structure + 0.2 * phase_interference + \
               0.15 * harmonic_modulation + fractal_basin + 0.12 * coupling_term + 0.05 * cubic_interaction