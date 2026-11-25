import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial symmetry breaking with modified cosine modulation
        radial_term = np.sum((x**2 + 2) * np.cos(np.sqrt(np.sum(x**2)) * 2.0)) / self.dim
        
        # Sinusoidal oscillation with higher frequencies and amplitude modulation
        sin_term = np.sum(np.sin(3.5 * x) * np.cos(4.5 * x) * np.exp(-x**2 / 8.0)) / self.dim
        
        # Enhanced polynomial saddle point structure with mixed powers and interaction terms
        poly_term = np.sum(x**9 * np.sin(x)**2 - x**4 * np.cos(x)**2 + x**2 * np.tan(x/2.0)) / (self.dim * 25.0)
        
        # Dynamic scaling factor with enhanced nonlinearity
        scale_factor = np.mean(np.abs(x))**1.7 + 1.3
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x))) / self.dim
        
        # Chaos-inducing component with enhanced trigonometric mixing and logarithmic decay
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 3.2) * np.cos(x * 0.6)) / self.dim
        
        # Multimodal interference with enhanced Gaussian peaks and valleys
        multi_term = np.sum(np.exp(-0.35 * (x - 2.5)**2) + np.exp(-0.35 * (x + 2.5)**2) - 1.4) / self.dim
        
        # Additional chaotic component with fractional powers and cross-terms
        frac_term = np.sum(x**(1.8) * np.sin(x**2.1) * np.cos(x)) / (self.dim * 15.0)
        
        # Combine all terms with adjusted weights for better balance
        total = 0.26 * radial_term + 0.19 * sin_term + 0.27 * poly_term + 0.14 * dynamic_term + 0.11 * chaos_term + 0.04 * multi_term + 0.03 * frac_term
        
        return total