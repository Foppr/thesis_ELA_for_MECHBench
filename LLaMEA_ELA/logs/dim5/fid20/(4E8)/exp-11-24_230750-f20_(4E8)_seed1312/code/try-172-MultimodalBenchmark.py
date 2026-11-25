import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic spiral component with dynamic frequency modulation
        spiral = 0.0
        for i in range(self.dim):
            freq = 1.2 + 0.8 * np.sin(i * 0.7 + 1.3)
            angle = x[i] * freq + np.sin(x[i] * 0.5) * np.cos(x[i] * 1.3)
            spiral += np.sin(angle) * np.cos(angle * 2.1)
        
        # Modified polynomial cross-terms with adaptive coefficients and alternating signs
        poly_terms = 0.0
        for i in range(self.dim - 2):
            coeff = 0.4 + 0.6 * np.cos(i * 1.1 + 0.9)
            term = coeff * (x[i]**3 * x[i+1] * x[i+2]**2 - x[i] * x[i+1]**3 * x[i+2])
            poly_terms += term
        
        # Multi-scale Gaussian peaks with dynamic positioning and amplitude
        gaussian_sum = 0.0
        for i in range(min(5, self.dim)):
            center = 3.0 * np.sin(i * np.pi / 3.0)
            width = 1.0 + 0.2 * np.cos(i * 0.8)
            height = 1.5 + 0.5 * np.sin(i * 0.6)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Enhanced logarithmic conditioning with multi-scale factors and dynamic exponents
        log_condition = 1.0 + 0.3 * np.log(np.mean(np.abs(x)) + 1e-8) + \
                       0.2 * np.sin(self.dim * 0.4) * np.std(x)
        
        # Quadratic base with enhanced scaling and coupling terms
        quadratic = log_condition * np.sum(x**2 * (1.0 + 0.4 * np.abs(x) + 0.1 * x**2))
        
        # Hyperbolic tangent interaction with modified coupling weights
        tanh_interaction = 0.8 * np.sum(np.tanh(x[:-1] + 0.5 * x[1:]) * 
                                      np.tanh(2.0 * x[:-1] - 0.3 * x[1:]))
        
        # Multi-scale chaotic noise with enhanced frequency modulation
        noise = 0.08 * np.random.rand() * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Combined function value with improved landscape complexity
        return quadratic + spiral + poly_terms + gaussian_sum + tanh_interaction + noise