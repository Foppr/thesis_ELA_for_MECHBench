import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        radius = np.sqrt(np.sum(x**2))
        radial_component = np.sin(4 * radius) * np.cos(6 * radius) * np.exp(-radius / 4)
        
        # Enhanced polynomial chaos with higher order terms and mixed coefficients
        poly_chaos = (np.sum(x**9) / (9 * self.dim) + 
                     np.sum(x**7) / (7 * self.dim) + 
                     np.sum(x**5) / (5 * self.dim) + 
                     np.sum(x**4) / (4 * self.dim) + 
                     0.3 * np.sum(x**2) / self.dim)
        
        # Improved cross-dimensional coupling with exponential decay and chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += np.sin(1.5 * x[i]) * np.cos(2.5 * x[i+1]) * np.exp(-0.5 * abs(x[i] - x[i+1]))
        cross_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with increased frequency diversity
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(3 * x[i]) * np.cos(7 * x[i]) * 
                           np.sin(5 * x[i]) * np.cos(9 * x[i]))
        multi_scale /= self.dim
        
        # Nested structure with enhanced local minima using combined trigonometric functions
        nested = 0.0
        for i in range(self.dim):
            nested += (np.sin(12 * x[i]) * np.cos(10 * x[i]) + 
                      0.4 * np.sin(8 * x[i]) + 
                      0.2 * np.sin(15 * x[i]))
        nested /= self.dim
        
        # Additional chaotic perturbation with modified parameters
        chaos_perturb = 0.15 * np.sum(np.sin(15 * x) * np.cos(11 * x) * np.exp(-x**2 / 2)) / self.dim
        chaos_perturb += 0.05 * np.sum(np.sin(20 * x) * np.cos(18 * x) * np.exp(-x**2 / 3)) / self.dim
        
        # Combine all components with adjusted weights for better balance
        result = (poly_chaos * 1.2 + cross_coupling * 0.8 + 
                 multi_scale * 0.6 + nested * 0.9 + 
                 radial_component * 0.4 + chaos_perturb)
        
        return float(result)