import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic modulations
        radius = np.sqrt(np.sum(x**2))
        radial_component = (np.sin(5 * radius) * np.cos(7 * radius) * 
                          np.exp(-radius / 3) * np.sin(3 * radius**0.5))
        
        # Higher order polynomial chaos with mixed exponents and coefficients
        poly_chaos = (np.sum(x**11) / (11 * self.dim) + 
                     np.sum(x**9) / (9 * self.dim) + 
                     np.sum(x**8) / (8 * self.dim) + 
                     np.sum(x**6) / (6 * self.dim) + 
                     0.4 * np.sum(x**3) / self.dim + 
                     0.2 * np.sum(x**2) / self.dim)
        
        # Complex cross-dimensional coupling with multiple interaction terms
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (np.sin(2.0 * x[i]) * np.cos(3.0 * x[i+1]) * 
                              np.exp(-0.3 * abs(x[i] - x[i+1])) * 
                              np.sin(1.5 * (x[i] + x[i+1])))
        cross_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with increased frequency diversity and amplitude
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(4 * x[i]) * np.cos(8 * x[i]) * 
                           np.sin(6 * x[i]) * np.cos(10 * x[i]) * 
                           np.exp(-x[i]**2 / 5))
        multi_scale /= self.dim
        
        # Nested structure with enhanced local minima using combined trigonometric functions
        nested = 0.0
        for i in range(self.dim):
            nested += (np.sin(15 * x[i]) * np.cos(13 * x[i]) + 
                      0.5 * np.sin(10 * x[i]) + 
                      0.3 * np.sin(20 * x[i]) + 
                      0.1 * np.sin(25 * x[i]))
        nested /= self.dim
        
        # Additional chaotic perturbation with modified parameters and higher frequency components
        chaos_perturb = 0.2 * np.sum(np.sin(18 * x) * np.cos(14 * x) * np.exp(-x**2 / 2)) / self.dim
        chaos_perturb += 0.1 * np.sum(np.sin(25 * x) * np.cos(22 * x) * np.exp(-x**2 / 3)) / self.dim
        chaos_perturb += 0.05 * np.sum(np.sin(30 * x) * np.cos(27 * x) * np.exp(-x**2 / 4)) / self.dim
        
        # New chaotic radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-np.sum((x - np.sin(i * np.pi / self.dim))**2) / 2)
        rbf_component /= self.dim
        
        # Combine all components with adjusted weights for better balance and increased complexity
        result = (poly_chaos * 1.5 + cross_coupling * 1.0 + 
                 multi_scale * 0.7 + nested * 1.1 + 
                 radial_component * 0.5 + chaos_perturb * 0.8 + 
                 rbf_component * 0.3)
        
        return float(result)