import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal basin terms with recursive scaling and multi-scale harmonics
        basin = 0.2 * np.sum(x**2) + 0.1 * np.sum(np.sin(15.0 * x) * np.cos(10.0 * x)) + \
                0.05 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x)) + \
                0.03 * np.sum(x**6)
        
        # Modified grid of global minima with nested frequencies and amplitude modulation
        grid_minima = 0.0
        for i in range(self.dim):
            grid_minima += 7.2 * np.sin(3.0 * x[i]) * np.cos(2.5 * x[i]) + \
                          4.1 * np.sin(4.2 * x[i]) * np.cos(3.8 * x[i]) + \
                          2.8 * np.sin(5.5 * x[i]) * np.cos(5.0 * x[i]) + \
                          1.5 * np.sin(6.8 * x[i]) * np.cos(6.3 * x[i]) + \
                          0.7 * np.sin(8.1 * x[i]) * np.cos(7.6 * x[i])
            
        # Enhanced cross-terms with fractal coupling and chaotic interaction patterns
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 2.0 * np.sin(3.0 * x[i]) * np.cos(3.0 * x[j]) + \
                              1.7 * np.cos(3.5 * x[i]) * np.sin(3.5 * x[j]) + \
                              1.3 * np.sin(2.5 * x[i]) * np.sin(2.5 * x[j]) + \
                              1.0 * np.cos(3.2 * x[i]) * np.cos(3.2 * x[j]) + \
                              0.6 * np.sin(4.1 * x[i]) * np.cos(4.1 * x[j])
        
        # Novel hybrid noise component with fractional Brownian motion characteristics
        noise = 0.05 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) + 
                             np.cos(18.0 * x) * np.sin(14.0 * x) + 
                             np.sin(22.0 * x) * np.cos(19.0 * x))
        
        # Higher-order polynomial terms with chaotic coefficient modulation
        cubic_term = 0.15 * np.sum(x**3)
        quartic_term = 0.08 * np.sum(x**4)
        quintic_term = 0.04 * np.sum(x**5)
        sextic_term = 0.02 * np.sum(x**6)
        
        # Chaotic sine-cosine combination with nested frequencies and irregular modulation
        chaotic_component = 0.08 * np.sum(np.sin(18.0 * x) + np.cos(19.0 * x) + 
                                         np.sin(25.0 * x) + np.cos(26.0 * x))
        
        # Additional nested fractal structure with recursive harmonic components
        nested_fractal = 0.03 * np.sum(np.sin(25.0 * np.sin(10.0 * x)) + 
                                      np.cos(25.0 * np.cos(10.0 * x)))
        
        return basin + grid_minima + cross_terms + noise + cubic_term + quartic_term + \
               quintic_term + sextic_term + chaotic_component + nested_fractal