import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with nested exponential decay and chaotic modulation
        radius = np.sqrt(np.sum(x**2))
        radial_component = (np.sin(5 * radius) * np.cos(7 * radius) * 
                          np.exp(-radius / 3) * np.sin(2 * radius**1.5))
        
        # Increased polynomial chaos with higher order terms and mixed coefficients
        poly_chaos = (np.sum(x**10) / (10 * self.dim) + 
                     np.sum(x**8) / (8 * self.dim) + 
                     np.sum(x**6) / (6 * self.dim) + 
                     np.sum(x**5) / (5 * self.dim) + 
                     0.4 * np.sum(x**3) / self.dim + 
                     0.2 * np.sum(x**2) / self.dim)
        
        # Enhanced cross-dimensional coupling with exponential decay and chaotic interaction
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            cross_coupling += (np.sin(2.0 * x[i]) * np.cos(3.0 * x[i+1]) * 
                              np.exp(-0.7 * abs(x[i] - x[i+1])) * 
                              np.sin(1.5 * (x[i] + x[i+1])))
        cross_coupling /= (self.dim - 1)
        
        # Multi-scale chaotic modulation with increased frequency diversity and nested structure
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
        
        # Additional chaotic perturbation with modified parameters and increased complexity
        chaos_perturb = 0.2 * np.sum(np.sin(18 * x) * np.cos(14 * x) * np.exp(-x**2 / 2.5)) / self.dim
        chaos_perturb += 0.1 * np.sum(np.sin(25 * x) * np.cos(22 * x) * np.exp(-x**2 / 3.5)) / self.dim
        chaos_perturb += 0.05 * np.sum(np.sin(30 * x) * np.cos(27 * x) * np.exp(-x**2 / 4.0)) / self.dim
        
        # New chaotic radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_component += np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(8 * x[i])
        rbf_component /= self.dim
        
        # Combine all components with adjusted weights for better balance
        result = (poly_chaos * 1.5 + cross_coupling * 1.0 + 
                 multi_scale * 0.7 + nested * 1.1 + 
                 radial_component * 0.5 + chaos_perturb * 0.8 + 
                 rbf_component * 0.3)
        
        return float(result)