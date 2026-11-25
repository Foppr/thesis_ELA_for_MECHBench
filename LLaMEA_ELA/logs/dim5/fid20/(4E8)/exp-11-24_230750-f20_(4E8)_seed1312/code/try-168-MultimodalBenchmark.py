import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic logarithmic spiral component with higher frequency modulation
        spiral = 0.0
        for i in range(self.dim):
            angle = np.log(np.abs(x[i]) + 1e-8) * (i * 2.1 + 1.3)
            spiral += np.sin(angle * 2.0) * np.cos(angle * 3.0) * np.sin(angle * 1.7)
        
        # Modified polynomial cross-terms with increased degree and stronger coupling
        poly_terms = 0.0
        for i in range(self.dim - 3):
            weight = 0.5 + 0.5 * np.sin(i * 1.1 + 2.0)
            poly_terms += weight * (x[i]**5 * x[i+1] * x[i+2] * x[i+3] - 
                                  x[i] * x[i+1]**3 * x[i+2]**2 * x[i+3]**4)
        
        # Dynamic Gaussian peaks with multi-scale positioning and varying amplitudes
        gaussian_sum = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 3.0) * 4.0
            width = 1.1 + 0.2 * np.cos(i * np.pi / 2.0)
            height = 1.5 + 0.5 * np.sin(i * 1.2)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Logarithmic conditioning with multi-scale factors, dynamic exponents and chaotic modulation
        log_condition = 1.0 + 0.6 * np.log(np.mean(np.abs(x)) + 1e-8) + \
                       0.2 * np.sin(self.dim * 0.7) * np.std(x) + \
                       0.1 * np.cos(self.dim * 0.4) * np.mean(x**2)
        
        # Quadratic base with enhanced adaptive scaling and complex coupling terms
        quadratic = log_condition * np.sum(x**2 * (1.0 + 0.5 * np.abs(x) + 0.2 * x**3))
        
        # Hyperbolic tangent interaction with stronger coupling weights and additional nonlinearities
        tanh_interaction = 1.0 * np.sum(np.tanh(x[:-1] + x[1:]) * 
                                      np.tanh(2.0 * x[:-1] - 0.6 * x[1:]) * 
                                      np.sin(x[:-1] * x[1:]))
        
        # Multi-scale chaotic noise with frequency modulation and amplitude scaling
        noise = 0.1 * np.random.rand() * np.sum(np.sin(5.2 * x) * np.cos(3.1 * x) * np.tanh(x))
        
        # Combined function value with enhanced landscape complexity
        return quadratic + spiral + poly_terms + gaussian_sum + tanh_interaction + noise