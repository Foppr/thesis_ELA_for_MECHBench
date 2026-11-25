import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis with fractional powers and asymmetric modulation
        radial_term = np.sum((x**2 + 1.5) * np.cos(np.sqrt(np.sum(x**2)) * 2.3) * np.sin(np.sum(x**3) / 10.0)) / self.dim
        
        # Enhanced sinusoidal oscillation with multiple frequency components and amplitude modulation
        sin_term = np.sum(np.sin(4.2 * x) * np.cos(5.1 * x) * np.tan(x / 2.0) * np.exp(-x**2 / 8.0)) / self.dim
        
        # Complex polynomial saddle point structure with mixed powers, trigonometric interactions and cross-terms
        poly_term = np.sum(x**9 * np.sin(x)**3 - x**4 * np.cos(x)**3 + x**2 * np.tan(x/2.5) * np.log(1.0 + np.abs(x))) / (self.dim * 25.0)
        
        # Dynamic scaling factor with hyperchaotic nonlinearity and time-varying components
        scale_factor = np.mean(np.abs(x))**2.1 + 1.8
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x)) * np.sin(np.sum(x**2) / 5.0)) / self.dim
        
        # Enhanced chaos-inducing component with fractional powers, cross-term interactions and logarithmic decay
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 3.2) * np.cos(x * 0.8) * np.tan(x / 1.5)) / self.dim
        
        # Multimodal interference with hyperbolic peaks, valleys and enhanced Gaussian components
        multi_term = np.sum(np.exp(-0.4 * (x - 2.7)**2) + np.exp(-0.4 * (x + 2.7)**2) - 1.6 * np.sin(x)**2) / self.dim
        
        # Novel cross-term interaction with fractional powers, trigonometric mixing and dynamic coupling
        frac_term = np.sum(x**(1.8) * np.sin(x**2.5) * np.cos(x * 1.3) * np.exp(-np.sum(x**2) / 20.0)) / (self.dim * 18.0)
        
        # Additional asymmetric gradient field component with enhanced noise injection
        asym_term = np.sum(np.abs(x)**1.9 * np.sin(x * 1.7) * np.cos(x * 0.9) * np.log(2.0 + x**2)) / (self.dim * 12.0)
        
        # Combine all terms with adjusted weights for maximum difficulty
        total = 0.23 * radial_term + 0.22 * sin_term + 0.21 * poly_term + 0.12 * dynamic_term + 0.10 * chaos_term + 0.05 * multi_term + 0.04 * frac_term + 0.03 * asym_term
        
        return total