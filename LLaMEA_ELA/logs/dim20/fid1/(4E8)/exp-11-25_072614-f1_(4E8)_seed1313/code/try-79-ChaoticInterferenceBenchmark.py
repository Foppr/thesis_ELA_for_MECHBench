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
        sin_term = np.sum(np.sin(3.0 * x) * np.cos(4.0 * x) * np.exp(-x**2 / 8.0)) / self.dim
        
        # Enhanced polynomial saddle point structure with mixed powers and interaction terms
        poly_term = np.sum(x**8 * np.sin(x)**2 - x**5 * np.cos(x)**2 + x**3 * np.tan(x/2.0)) / (self.dim * 25.0)
        
        # Dynamic scaling factor with enhanced nonlinearity
        scale_factor = np.mean(np.abs(x))**1.5 + 1.5
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x))) / self.dim
        
        # Chaos-inducing component with enhanced trigonometric mixing and logarithmic decay
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 3.0) * np.cos(x * 0.5)) / self.dim
        
        # Multimodal interference with enhanced Gaussian peaks and valleys
        multi_term = np.sum(np.exp(-0.3 * (x - 2.5)**2) + np.exp(-0.3 * (x + 2.5)**2) - 1.5) / self.dim
        
        # Additional chaotic component with fractional powers and cross-terms
        frac_term = np.sum(x**(1.7) * np.sin(x**2) * np.cos(x)) / (self.dim * 15.0)
        
        # Combine all terms with adjusted weights for better balance
        total = 0.25 * radial_term + 0.2 * sin_term + 0.25 * poly_term + 0.15 * dynamic_term + 0.1 * chaos_term + 0.05 * multi_term + 0.05 * frac_term
        
        return total