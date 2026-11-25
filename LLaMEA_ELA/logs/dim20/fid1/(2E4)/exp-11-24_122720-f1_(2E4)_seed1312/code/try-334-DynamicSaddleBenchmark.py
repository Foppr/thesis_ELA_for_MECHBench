import numpy as np

class DynamicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension with higher variability
        self.chaos_params = [np.random.uniform(0.3, 1.2) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(0.8, 3.0) for _ in range(dim)]
        self.fractal_dim = 1.2 + np.random.rand() * 0.8
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple sine harmonics and cubic terms
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Multi-harmonic chaotic behavior with cubic and quintic terms
            chaotic += param * x[i] * (1 - x[i]**2) + 0.2 * np.sin(2.0 * x[i] * np.pi) + \
                      0.15 * np.sin(3.0 * x[i] * np.pi) + 0.08 * x[i]**3 + 0.03 * x[i]**5
            
        # Enhanced fractal basin component with variable exponents and logarithmic scaling
        fractal = 0
        for i in range(self.dim):
            # Create more complex fractal behavior with log-periodic oscillations
            exponent = 1.0 + 0.6 * np.sin(i * np.pi / (self.dim + 1)) + 0.2 * np.cos(i * np.pi / (self.dim + 2))
            fractal += np.abs(x[i])**exponent + 0.1 * np.log(np.abs(x[i]) + 1)
            
        # Enhanced adaptive ridge structure with multi-scale sinusoidal components
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Multi-scale ridge with exponential and hyperbolic components
            ridge = strength * (np.exp(-x[i]**2) + 0.8 * np.sin(x[i]) + 0.4 * np.cos(2 * x[i]) + 
                               0.2 * np.tanh(x[i]) + 0.15 * np.sin(3 * x[i]) + 0.1 * np.exp(-x[i]**2))
            ridges += ridge
            
        # Complex cross-dimension interaction with multi-frequency terms and amplitude modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-frequency interaction with varying coupling strengths
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                interaction += scale_factor * np.sin(4.0 * x[i] * x[j]) * np.cos(3.0 * (x[i] + x[j])) * \
                              (1 + 0.4 * np.sin(i * j) + 0.3 * np.cos(i + j)) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Stronger hyperbolic saddle term with fractional powers for increased non-smoothness
        saddle = 0
        for i in range(self.dim):
            # Fractional hyperbolic term with variable exponents - slightly modified
            saddle += 0.8 * np.abs(x[i])**(1.35 + 0.15 * np.sin(i * np.pi / (self.dim + 1))) * np.tanh(x[i])
            
        # Add complex dimensionality-dependent modulation with multiple scaling factors
        dim_modulation = np.log(self.dim + 2) * 0.3 + np.sqrt(self.dim) * 0.05
        result = 2.5 * chaotic + 1.8 * fractal + 1.5 * ridges + 0.8 * interaction + 1.0 * saddle
        
        # Additional noise component for increased complexity
        noise = 0.05 * np.sum(np.sin(x * 10))
        result += noise
        
        return result