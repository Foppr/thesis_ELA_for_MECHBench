import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial symmetry breaking with modified cosine modulation and hyperbolic tangent
        radial_term = np.sum((x**2 + 2) * np.cos(np.sqrt(np.sum(x**2)) * 2.0) * np.tanh(x)) / self.dim
        
        # Sinusoidal oscillation with higher frequencies, amplitude modulation, and phase shifts
        sin_term = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.exp(-x**2 / 12.0) * np.sin(x)) / self.dim
        
        # Enhanced polynomial saddle point structure with mixed powers, interaction terms, and fractional exponents
        poly_term = np.sum(x**9 * np.sin(x)**3 - x**6 * np.cos(x)**3 + x**4 * np.tan(x/3.0) + x**(1.3)) / (self.dim * 30.0)
        
        # Dynamic scaling factor with enhanced nonlinearity and chaotic feedback
        scale_factor = np.mean(np.abs(x))**2.0 + 2.0 + 0.5 * np.sin(np.sum(x))
        dynamic_term = np.sum(np.sin(x * scale_factor) * np.cos(x / scale_factor) * np.log(1.0 + np.abs(x)) * np.exp(-x**2/10.0)) / self.dim
        
        # Chaos-inducing component with enhanced trigonometric mixing, logarithmic decay, and hyperchaotic modulation
        chaos_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 4.0) * np.cos(x * 0.7) * np.tanh(x**2)) / self.dim
        
        # Multimodal interference with enhanced Gaussian peaks, valleys, and hyperbolic secant components
        multi_term = np.sum(np.exp(-0.4 * (x - 3.0)**2) + np.exp(-0.4 * (x + 3.0)**2) - 1.8 + np.sech(x)) / self.dim
        
        # Additional chaotic component with fractional powers, cross-terms, and hyperbolic functions
        frac_term = np.sum(x**(1.9) * np.sin(x**2.5) * np.cos(x * 1.5) * np.tanh(x)) / (self.dim * 20.0)
        
        # Hyperchaotic coupling term with multiple interacting nonlinear components
        hyperchaos_term = np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.exp(-x**2/15.0) * np.log(2.0 + x**2)) / self.dim
        
        # Combine all terms with adjusted weights for better balance and increased complexity
        total = 0.2 * radial_term + 0.18 * sin_term + 0.22 * poly_term + 0.13 * dynamic_term + 0.12 * chaos_term + 0.07 * multi_term + 0.05 * frac_term + 0.03 * hyperchaos_term
        
        return total