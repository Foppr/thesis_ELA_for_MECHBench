import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 1.0
        self.modulation_freq = 2.0 * np.pi
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add chaotic exponential decay components with adaptive scaling
        for i in range(self.dim):
            # Chaotic scaling factor based on dimension index
            chaos_scale = 1.0 + 0.5 * np.sin(3.14159 * i / self.dim)
            
            # Exponential decay term with chaotic scaling
            exp_term = np.exp(-chaos_scale * self.scale_factor * (x_norm[i]**2))
            
            # Fractal sinusoidal modulation with multiple harmonic frequencies
            sin_mod = np.sin(self.modulation_freq * x_norm[i]) + \
                     0.5 * np.sin(3 * self.modulation_freq * x_norm[i]) + \
                     0.3 * np.sin(7 * self.modulation_freq * x_norm[i]) + \
                     0.1 * np.sin(11 * self.modulation_freq * x_norm[i])
            
            # Combine exponential decay with fractal sinusoidal modulation
            fitness += exp_term * (1 + 0.5 * sin_mod)
        
        # Add chaotic cross-dimensional coupling with nonlinear interaction
        for i in range(self.dim - 1):
            # Nonlinear coupling strength based on chaotic sequence
            coupling_strength = 0.2 * np.sin(2.718 * i / self.dim) * (i + 1) / self.dim
            
            # Hyperbolic attraction potential between dimensions
            diff = x_norm[i] - x_norm[i+1]
            attr_term = np.tanh(diff**2) + 0.3 * np.tanh(diff**4)
            
            fitness += coupling_strength * attr_term
        
        # Add multi-modal structure through chaotic polynomial terms
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6) + 0.1 * np.sum(np.abs(x_norm)**8)
        
        # Add fractal noise for increased ruggedness and unpredictability
        noise = 0.005 * np.random.rand()
        for i in range(self.dim):
            noise += 0.001 * np.sin(13.0 * x_norm[i]) * np.cos(7.0 * x_norm[i])
        
        return fitness + poly_term + noise