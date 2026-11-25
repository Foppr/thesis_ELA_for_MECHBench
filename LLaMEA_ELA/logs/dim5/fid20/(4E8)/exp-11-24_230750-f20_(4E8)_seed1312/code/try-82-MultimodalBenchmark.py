import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity patterns with recursive scaling
        fractal_pattern = 0.0
        for i in range(1, min(4, self.dim)):
            scale = 2.0 ** (-i)
            fractal_pattern += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**2))
        
        # Quantum harmonic oscillator components with imaginary frequency terms
        quantum_osc = 0.3 * np.sum((x**2 + 0.5j * x**3) * np.exp(-0.1 * np.abs(x)))
        
        # Adaptive gradient fields with dynamic step sizes and directional couplings
        grad_field = 0.0
        for i in range(self.dim - 2):
            dx1 = x[i+1] - x[i]
            dx2 = x[i+2] - x[i+1]
            grad_field += np.tanh(dx1 * dx2) * (1.0 + 0.1 * np.sin(i))
        
        # Enhanced radial basis functions with self-similar centers and variable widths
        rbf_sum = 0.0
        for i in range(min(6, self.dim)):
            center = 3.0 * np.sin(i * np.pi / 3) * np.cos(i * np.pi / 5)
            width = 1.2 + 0.4 * np.sin(i * np.pi / 2)
            rbf_sum += np.exp(-0.2 * ((x[i] - center) / width)**2)
        
        # Augmented polynomial cross-terms with fractional exponents and coupling
        poly_cross = 0.5 * np.sum(x[:-2]**1.5 * x[1:-1]**2.5 * x[2:]**1.5 - 
                                x[:-2]**2.5 * x[1:-1]**1.5 * x[2:]**2.5)
        
        # Dynamic conditioning with multi-scale factors and chaotic modulation
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * 0.4) * np.mean(np.abs(x)) + \
                          0.15 * np.cos(self.dim * 0.2) * np.std(x) + \
                          0.2 * np.sin(np.sum(x)**2)
        
        # Quadratic basin with non-uniform weights, dynamic scaling, and coupling terms
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.3 * x**4))
        
        # Additional chaotic noise component with adaptive intensity and frequency
        noise = 0.1 * np.random.rand() * np.sum(np.sin(5 * x) * np.cos(2 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Combined function value with additional interaction terms
        return quadratic + fractal_pattern + quantum_osc + grad_field + rbf_sum + poly_cross + noise