import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        radial_term = r * np.sin(5.0 * r) * np.cos(3.0 * r)
        
        # Multimodal trigonometric components with varying frequencies and amplitudes
        multimodal_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 * (i + 1)
            amp = 2.0 / (i + 1)**1.5
            multimodal_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                weight = 1.0 / (1.0 + np.abs(x[i] - x[j]))
                coupling_term += weight * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Polynomial and exponential components with conditioning
        poly_term = np.sum(x**4) * np.exp(-0.05 * r)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.2 * r)
        
        # Additional chaotic modulation
        chaos_factor = 1.0 + 0.5 * np.sin(10.0 * r) * np.cos(7.0 * r)
        
        # Final combination with adaptive scaling
        result = chaos_factor * (radial_term + multimodal_sum + coupling_term + poly_term + exp_term)
        
        return result