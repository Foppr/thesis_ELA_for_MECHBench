import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyper-chaotic parameters for each dimension
        self.chaos_params = [np.random.uniform(0.8, 1.2) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.fractal_dim = 2.0 + np.random.rand() * 0.5
        # Memory-based parameters for dynamic behavior
        self.memory = np.random.rand(dim)
        self.time_phase = np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic component with time-varying dynamics
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Hyper-chaotic logistic map with memory effect
            mem_factor = self.memory[i] * np.sin(self.time_phase + x[i])
            chaotic += param * x[i] * (1 - x[i]**3) * (1 + 0.2 * mem_factor) + 0.15 * np.sin(x[i] * np.pi * 2)
            
        # Multi-scale fractal basin component
        fractal = 0
        for i in range(self.dim):
            # Multi-fractal behavior with scale-dependent exponents
            scale = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 1))
            exponent = self.fractal_dim - 0.2 * np.sin(i)
            fractal += np.abs(x[i])**exponent * scale
            
        # Adaptive ridge structure with temporal variation
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Time-varying ridge with memory influence
            time_factor = np.cos(self.time_phase * 2 + i)
            ridge = strength * (np.exp(-x[i]**2) + 0.3 * np.sin(x[i]) * time_factor)
            ridges += ridge
            
        # Cross-dimension interaction with dynamic scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic interaction with memory-based scaling
                mem_scale = (self.memory[i] + self.memory[j]) / 2
                scale_factor = (i + 1) * (j + 1) / (self.dim**2) * (1 + 0.1 * mem_scale)
                interaction += scale_factor * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j] + self.time_phase)
                
        # Memory-dependent modulation component
        memory_mod = 0
        for i in range(self.dim):
            memory_mod += self.memory[i] * np.cos(x[i] * np.pi / 2)
            
        # Combine all components with dynamic weighting
        result = 2.0 * chaotic + 1.5 * fractal + 1.2 * ridges + 0.5 * interaction + 0.2 * memory_mod
        
        # Add dimensionality-dependent modulation with time effect
        dim_modulation = np.log(self.dim + 1) * 0.15 * (1 + 0.1 * np.sin(self.time_phase))
        result *= (1.0 + dim_modulation)
        
        return result