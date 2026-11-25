import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic radial basis with fractional powers and enhanced symmetry breaking
        radial_term = np.sum((x**2.7 + 1.3) * np.cos(np.sqrt(np.sum(x**2)) * 2.9)) / self.dim
        
        # Sinusoidal oscillation with higher frequencies, amplitude modulation, and phase shifting
        sin_term = np.sum(np.sin(4.2 * x + 0.7) * np.cos(5.1 * x - 1.2) * np.exp(-x**2 / 6.0)) / self.dim
        
        # Enhanced polynomial saddle point structure with mixed powers, interaction terms and fractional exponents
        poly_term = np.sum(x**9 * np.sin(x)**2.3 - x**4.7 * np.cos(x)**1.8 + x**2.9 * np.tan(x/2.1)) / (self.dim * 25.0)
        
        # Dynamic scaling factor with enhanced nonlinearity and noise injection
        scale_factor = np.mean(np.abs(x))**1.8 + 1.6 + 0.1 * np.random.rand()
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x))) / self.dim
        
        # Chaos-inducing component with enhanced trigonometric mixing, logarithmic decay and cross-term interactions
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 3.2) * np.cos(x * 0.8) * np.sin(x * 1.5)) / self.dim
        
        # Multimodal interference with enhanced Gaussian peaks, valleys and additional chaotic modulation
        multi_term = np.sum(np.exp(-0.4 * (x - 2.7)**2) + np.exp(-0.4 * (x + 2.7)**2) - 1.6 + 0.05 * np.sin(x * 2.3)) / self.dim
        
        # Additional chaotic component with fractional powers, cross-terms and dynamic frequency modulation
        frac_term = np.sum(x**(1.8) * np.sin(x**2.5) * np.cos(x * 1.3) * np.exp(-x**2 / 10.0)) / (self.dim * 18.0)
        
        # Cross-term interaction with enhanced coupling and asymmetric gradient fields
        cross_term = np.sum(np.sin(x[0] * x[1]) * np.cos(x[0] + x[1]) * np.tan(x[0] - x[1])) / self.dim
        
        # Combine all terms with adjusted weights for better balance and increased complexity
        total = 0.28 * radial_term + 0.23 * sin_term + 0.22 * poly_term + 0.12 * dynamic_term + 0.10 * chaos_term + 0.05 * multi_term + 0.04 * frac_term + 0.03 * cross_term
        
        return total