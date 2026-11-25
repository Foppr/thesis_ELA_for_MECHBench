import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic spiral component with varying angular frequencies
        spiral = 0.0
        for i in range(self.dim):
            angle = np.log(np.abs(x[i]) + 1e-8) * (i * 1.3 + 0.7)
            spiral += np.sin(angle) * np.cos(angle * 1.5)
        
        # Adaptive polynomial cross-terms with modified weights and alternating signs
        poly_terms = 0.0
        for i in range(self.dim - 2):
            weight = 0.3 + 0.7 * np.sin(i * 0.9 + 1.0)
            poly_terms += weight * (x[i]**4 * x[i+1] * x[i+2] - x[i] * x[i+1]**2 * x[i+2]**3)
        
        # Dynamic Gaussian peaks with position-dependent heights and widths
        gaussian_sum = 0.0
        for i in range(min(4, self.dim)):
            center = np.sin(i * np.pi / 2.5) * 3.5
            width = 0.9 + 0.3 * np.cos(i * np.pi / 1.8)
            height = 1.2 + 0.4 * np.sin(i * 0.7)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Logarithmic conditioning with multi-scale factors and dynamic exponents
        log_condition = 1.0 + 0.4 * np.log(np.mean(np.abs(x)) + 1e-8) + \
                       0.15 * np.sin(self.dim * 0.5) * np.std(x)
        
        # Quadratic base with adaptive scaling and coupling terms
        quadratic = log_condition * np.sum(x**2 * (1.0 + 0.3 * np.abs(x)))
        
        # Hyperbolic tangent interaction with dynamic coupling weights
        tanh_interaction = 0.7 * np.sum(np.tanh(x[:-1] + x[1:]) * 
                                      np.tanh(1.5 * x[:-1] - 0.4 * x[1:]))
        
        # Multi-scale chaotic noise with frequency modulation
        noise = 0.06 * np.random.rand() * np.sum(np.sin(4.5 * x) * np.cos(2.3 * x))
        
        # Combined function value with enhanced landscape complexity
        return quadratic + spiral + poly_terms + gaussian_sum + tanh_interaction + noise