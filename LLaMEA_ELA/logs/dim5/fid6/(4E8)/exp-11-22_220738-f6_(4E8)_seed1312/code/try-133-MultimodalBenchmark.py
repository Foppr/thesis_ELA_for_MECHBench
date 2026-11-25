import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaotic_factor = 3.8 + np.random.rand() * 0.2
        self.rbf_width = 0.5 + np.random.rand() * 0.5
        self.polynomial_degree = 3 + np.random.randint(2)
        self.saddle_strength = 2.0 + np.random.rand() * 1.5
        self.tent_scaling = 1.2 + np.random.rand() * 0.8
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(self.chaotic_factor * x[i]) * np.cos(self.chaotic_factor * x[i])
            
        # Dynamic radial basis functions with time-varying parameters
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    rbf_sum += np.exp(-dist**2 / (2 * self.rbf_width**2))
            rbf_component += rbf_sum
        
        # Cross-dimensional polynomial couplings
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i] * x[j])**self.polynomial_degree
                
        # Asymmetric exponential saddle points
        saddle_component = 0.0
        for i in range(self.dim):
            saddle_component += self.saddle_strength * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(2.0 * x[i])
            
        # Hyperchaotic tent map component
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = x[i]
            for _ in range(5):  # Tent map iterations
                if tent_val < 0.5:
                    tent_val = self.tent_scaling * tent_val
                else:
                    tent_val = self.tent_scaling * (1.0 - tent_val)
            tent_component += tent_val
            
        # Modified curvature effects and noise sensitivity
        curvature_effect = 0.0
        for i in range(self.dim):
            curvature_effect += x[i]**4 + 0.3 * np.sin(5.0 * x[i]) + 0.1 * np.random.randn()
            
        # Combine all components with adaptive weights
        result = (0.25 * chaotic_component + 
                 0.35 * rbf_component + 
                 0.15 * poly_coupling + 
                 0.12 * saddle_component + 
                 0.10 * tent_component + 
                 0.03 * curvature_effect)
        
        # Add dimensionality scaling
        result *= (1.0 + 0.05 * self.dim)
        
        return result