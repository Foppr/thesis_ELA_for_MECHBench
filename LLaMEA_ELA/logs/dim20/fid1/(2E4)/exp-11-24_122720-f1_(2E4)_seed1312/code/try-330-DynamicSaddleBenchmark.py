import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with fractional chaos and dynamic scaling
        self.chaos_params = [np.random.uniform(0.5, 1.5) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(1.2, 3.5) for _ in range(dim)]
        self.fractal_dim = 1.7 + np.random.rand() * 0.8
        # Add multi-scale coupling with fractal dimensionality
        self.coupling_strength = np.random.uniform(0.3, 3.0, (dim, dim))
        # Additional chaotic modulation factors for each dimension
        self.modulation_factors = [np.random.uniform(0.8, 2.0) for _ in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with fractional harmonics and exponential terms
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Add fractional-order sine components and exponential modulations
            chaotic += param * x[i] * (1 - x[i]**2) + 0.3 * np.sin(2.5 * x[i] * np.pi) + \
                       0.2 * np.sin(4.0 * x[i] * np.pi) + 0.1 * np.exp(-x[i]**2) * np.sinh(x[i]) + \
                       0.05 * np.abs(x[i])**1.7
            
        # Fractal basin component with multi-scale logarithmic exponents
        fractal = 0
        for i in range(self.dim):
            # Use variable log-scale exponents and add fractional dimensionality
            exponent = 1.0 + 2.0 * np.log(i + 3) / np.log(self.dim + 2)
            fractal += np.abs(x[i])**exponent
            
        # Enhanced ridge structure with multi-scale piecewise and hyperbolic components
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Add discontinuous functions with hyperbolic and fractional components
            ridge = strength * (np.exp(-x[i]**2) + 0.7 * np.sin(x[i]) + 0.5 * np.cos(2 * x[i]) + 
                               0.2 * np.tanh(x[i]) + 0.15 * np.sign(x[i]) * np.log(np.abs(x[i]) + 1) + 
                               0.08 * np.abs(x[i])**1.3)
            ridges += ridge
            
        # Cross-dimension interaction with multi-scale coupling and chaotic modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add multi-scale chaotic modulation and higher-order coupling terms
                coupling = self.coupling_strength[i][j] * (1 + 0.3 * np.sin(x[i] * x[j]))
                interaction += coupling * np.sin(5.0 * x[i] * x[j]) * np.cos(4.0 * (x[i] + x[j])) * \
                              np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1 + 0.3 * np.sin(i * j * np.pi / self.dim)) * \
                              np.log(np.abs(x[i] - x[j]) + 1)
                
        # Hyperbolic saddle term with multi-asymptotic behaviors and fractional scaling
        saddle = 0
        for i in range(self.dim):
            # Add multi-scale exponential and hyperbolic components
            saddle += 0.5 * np.abs(x[i]) * np.tanh(x[i]) + 0.2 * np.exp(-x[i]**2) * np.sinh(x[i]) + \
                      0.1 * np.abs(x[i])**1.8
            
        # Add global scaling factor with multi-dimensional chaotic modulation
        global_factor = 2.0 + 0.8 * np.sin(self.dim * np.pi / 5)
        
        # Combine all components with adaptive weights and enhanced chaotic scaling
        result = global_factor * (3.0 * chaotic + 2.0 * fractal + 1.8 * ridges + 1.0 * interaction + 1.2 * saddle)
        
        # Add dimensionality-dependent modulation with multi-scale fractal scaling
        dim_modulation = np.log(self.dim + 3) * 0.4
        result *= (1.0 + dim_modulation)
        
        return result