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
            angle = np.log(np.abs(x[i]) + 1e-8) * (i + 1)
            spiral += np.sin(angle) * np.cos(angle)
        
        # Adaptive polynomial cross-terms with dimension-dependent weights and alternating signs
        poly_terms = 0.0
        for i in range(self.dim - 2):
            weight = 0.5 + 0.5 * np.sin(i * 0.7)
            poly_terms += weight * (x[i]**3 * x[i+1] * x[i+2] - x[i] * x[i+1]**3 * x[i+2])
        
        # Dynamic Gaussian peaks with position-dependent heights and widths
        gaussian_sum = 0.0
        for i in range(min(4, self.dim)):
            center = np.sin(i * np.pi / 3.0) * 4.0
            width = 0.8 + 0.4 * np.cos(i * np.pi / 2.0)
            height = 1.0 + 0.5 * np.sin(i * 0.5)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Logarithmic conditioning with multi-scale factors and dynamic exponents
        log_condition = 1.0 + 0.3 * np.log(np.mean(np.abs(x)) + 1e-8) + \
                       0.2 * np.sin(self.dim * 0.4) * np.std(x)
        
        # Quadratic base with adaptive scaling and coupling terms
        quadratic = log_condition * np.sum(x**2 * (1.0 + 0.2 * np.abs(x)))
        
        # Hyperbolic tangent interaction with dynamic coupling weights
        tanh_interaction = 0.6 * np.sum(np.tanh(x[:-1] + x[1:]) * 
                                      np.tanh(2.0 * x[:-1] - 0.5 * x[1:]))
        
        # Multi-scale chaotic noise with frequency modulation
        noise = 0.05 * np.random.rand() * np.sum(np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Combined function value with enhanced landscape complexity
        return quadratic + spiral + poly_terms + gaussian_sum + tanh_interaction + noise