import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial symmetry breaking component with cosine modulation
        radial_term = np.sum((x**2 + 1) * np.cos(np.sqrt(np.sum(x**2)) * 1.5)) / self.dim
        
        # Sinusoidal oscillation with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.exp(-x**2 / 10.0)) / self.dim
        
        # Polynomial saddle point structure with mixed even/odd powers
        poly_term = np.sum(x**6 * np.sin(x)**2 - x**4 * np.cos(x)**2) / (self.dim * 20.0)
        
        # Dynamic scaling factor based on coordinate positions
        scale_factor = np.mean(np.abs(x)) + 1.0
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor)) / self.dim
        
        # Chaos-inducing component with logarithmic decay and trigonometric mixing
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 2.5)) / self.dim
        
        # Multimodal interference with Gaussian peaks and valleys
        multi_term = np.sum(np.exp(-0.5 * (x - 2.0)**2) + np.exp(-0.5 * (x + 2.0)**2) - 1.0) / self.dim
        
        # Combine all terms with adaptive weights
        total = 0.3 * radial_term + 0.25 * sin_term + 0.2 * poly_term + 0.1 * dynamic_term + 0.1 * chaos_term + 0.05 * multi_term
        
        return total