import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyper-chaotic parameters for each dimension
        self.chaos_params = [np.random.uniform(0.8, 1.2) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(1.0, 3.0) for _ in range(dim)]
        self.fractal_dim = 1.8 + np.random.rand() * 0.4
        # Time-varying components
        self.time_factor = np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic component with time-varying dynamics
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Enhanced chaotic behavior with exponential modulation
            chaotic += param * x[i] * np.sin(x[i]**2) + 0.2 * np.cos(x[i] * np.pi)
            
        # Multi-fractal basin component with varying scaling
        fractal = 0
        for i in range(self.dim):
            # Multi-scale fractal behavior with dynamic exponents
            exponent = 1.2 + 0.8 * np.sin(i * np.pi / (self.dim + 1)) + 0.3 * np.cos(self.time_factor * i)
            fractal += np.abs(x[i])**exponent
            
        # Adaptive ridge structure with time-varying non-linearity
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Time-varying ridge with periodic modulation
            ridge = strength * (np.exp(-x[i]**2) + 0.3 * np.sin(x[i] * self.time_factor))
            ridges += ridge
            
        # Cross-dimension interaction with multi-scale coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale interaction terms with dynamic weights
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                interaction += scale_factor * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j] * self.time_factor)
                
        # Add multi-scale noise injection for robustness testing
        noise = 0
        for i in range(self.dim):
            # Inject noise at multiple scales
            noise += 0.1 * np.sin(x[i] * (i + 1) * self.time_factor) * np.cos(x[i] * self.fractal_dim)
            
        # Combine all components with dynamic weighting
        result = 2.0 * chaotic + 1.5 * fractal + 1.2 * ridges + 0.5 * interaction + 0.3 * noise
        
        # Add dimensionality-dependent modulation and time factor
        dim_modulation = np.log(self.dim + 1) * 0.15
        result *= (1.0 + dim_modulation) * (1.0 + 0.2 * self.time_factor)
        
        return result