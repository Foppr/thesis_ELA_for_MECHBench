import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with temporal variation
        self.chaos_params = [np.random.uniform(0.8, 1.2) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.fractal_dim = 1.8 + np.random.rand() * 0.4
        # Time-varying chaotic modulation
        self.time_factor = np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with time-varying dynamics
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Highly chaotic behavior with higher frequency sinusoidal terms
            chaotic += param * x[i] * (1 - x[i]**2) + 0.3 * np.sin(3.0 * x[i] * np.pi) + 0.2 * np.cos(5.0 * x[i])
            
        # Fractal basin with enhanced multi-fractal scaling
        fractal = 0
        for i in range(self.dim):
            # Multi-fractal exponent with dynamic variation
            exponent = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 2)) + 0.3 * np.cos(2 * i * np.pi / (self.dim + 1))
            fractal += np.abs(x[i])**exponent
            
        # Enhanced adaptive ridge structure with multi-modal peaks
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Multi-modal ridge with enhanced peak complexity
            ridge = strength * (np.exp(-x[i]**2) + 0.8 * np.sin(x[i]) + 0.4 * np.cos(3 * x[i]) + 0.3 * np.sin(2 * x[i]))
            ridges += ridge
            
        # Cross-dimension interaction with enhanced coupling and time modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger interaction with frequency modulation based on dimension indices
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                freq_mod = 1.0 + 0.5 * np.sin(self.time_factor * i * j)
                interaction += scale_factor * np.sin(3.0 * x[i] * x[j]) * np.cos(2.0 * (x[i] + x[j])) * freq_mod * (1 + 0.3 * np.sin(i * j))
                
        # Additional chaotic modulation term with time-varying influence
        time_mod = 1.0 + 0.4 * np.sin(self.time_factor * np.sum(x**2))
        
        # Combine all components with adjusted weights and time modulation
        result = 3.0 * chaotic + 2.0 * fractal + 1.5 * ridges + 0.8 * interaction
        
        # Dimensionality-dependent modulation with enhanced scaling
        dim_modulation = np.log(self.dim + 2) * 0.3
        result *= (time_mod * (1.0 + dim_modulation))
        
        return result