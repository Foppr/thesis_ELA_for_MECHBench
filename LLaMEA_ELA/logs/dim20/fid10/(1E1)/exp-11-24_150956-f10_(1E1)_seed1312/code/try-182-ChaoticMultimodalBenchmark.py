import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine-wave components with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(13.0 * x_scaled) * np.cos(17.0 * x_scaled) + 
                              0.7 * np.sin(23.0 * x_scaled**2) * np.cos(29.0 * x_scaled**2) + 
                              0.4 * np.sin(37.0 * x_scaled**3) * np.cos(41.0 * x_scaled**3))
        
        # Polynomial chaos with mixed degrees and cross-terms
        poly_chaos = np.sum(x_scaled**4 + 0.8 * x_scaled**3 + 0.6 * x_scaled**2 + 0.3 * x_scaled + 
                           (x_scaled[:-1]**2 * x_scaled[1:]**3) + (x_scaled[:-2]**3 * x_scaled[2:]**2))
        
        # Adaptive gradient modulation with exponential decay
        grad_mod = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled))
        
        # Cross-dimensional coupling with hyperbolic tangent interactions
        cross_coupling = np.sum(np.tanh(2.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                               np.tanh(1.5 * (x_scaled[:-1] - x_scaled[1:])) + 
                               np.tanh(3.0 * (x_scaled[:-2] + x_scaled[2:])) * 
                               np.tanh(2.5 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Asymmetric harmonic interference with phase shifts and amplitude modulation
        asym_harmonics = np.sum(np.sin(7.0 * x_scaled) * np.cos(9.0 * x_scaled) * 
                               (1.0 + 0.3 * np.sin(5.0 * x_scaled)) + 
                               0.6 * np.sin(11.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) * 
                               (1.0 + 0.4 * np.cos(7.0 * x_scaled)))
        
        # Combined landscape with weighted components
        return 0.4 * chaotic_terms + 0.25 * poly_chaos + 0.15 * grad_mod + 0.1 * cross_coupling + 0.1 * asym_harmonics + 1.8