import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis with fractional exponents and dynamic modulation
        radial_term = np.sum((x**2.7 + 1.8) * np.cos(np.sqrt(np.sum(x**2)) * 2.3)) / self.dim
        
        # Asymmetric gradient field with sine-cosine mixing and amplitude scaling
        sin_term = np.sum(np.sin(4.2 * x) * np.cos(5.1 * x) * np.exp(-x**2 / 9.0)) / self.dim
        
        # Enhanced polynomial saddle point structure with mixed powers, interaction terms and fractional coefficients
        poly_term = np.sum(x**9 * np.sin(x)**2.1 - x**4.7 * np.cos(x)**2.3 + x**2.8 * np.tan(x/2.1)) / (self.dim * 25.0)
        
        # Dynamic scaling factor with hyperchaotic nonlinearity and time-varying components
        scale_factor = np.mean(np.abs(x))**1.8 + 1.6
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x)) * np.sin(0.5 * np.sum(x))) / self.dim
        
        # Chaos-inducing component with enhanced trigonometric mixing, logarithmic decay and cross-terms
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 3.2) * np.cos(x * 0.8) * np.exp(-np.sum(x**2)/20.0)) / self.dim
        
        # Multimodal interference with enhanced Gaussian peaks, valleys and asymmetric modulation
        multi_term = np.sum(np.exp(-0.4 * (x - 2.7)**2.1) + np.exp(-0.4 * (x + 2.7)**2.1) - 1.6) / self.dim
        
        # Additional chaotic component with fractional powers, cross-terms and dynamic phase modulation
        frac_term = np.sum(x**(1.8) * np.sin(x**2.3) * np.cos(x * 1.3) * np.sin(0.7 * x)) / (self.dim * 16.0)
        
        # Cross-term interaction with higher-order polynomial and trigonometric coupling
        cross_term = np.sum(np.sin(x[0] * x[1]) * np.cos(x[1] * x[2]) * np.exp(-x[0]**2/10.0)) / self.dim if self.dim > 2 else 0
        
        # Combine all terms with adjusted weights for better balance and increased complexity
        total = 0.23 * radial_term + 0.22 * sin_term + 0.25 * poly_term + 0.13 * dynamic_term + 0.10 * chaos_term + 0.05 * multi_term + 0.04 * frac_term + 0.08 * cross_term
        
        return total