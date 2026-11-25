import numpy as np

class ExponentialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay factors and ridge parameters
        self.decay_factors = [np.exp(-0.15 * i) for i in range(dim)]
        self.ridge_params = [(np.sin(0.6 * i), np.cos(0.4 * i)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced exponential decay sinusoidal components with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            amp = 2.5 * self.decay_factors[i]
            freq = 1.2 + 0.3 * np.sin(0.8 * i)
            phase = 0.4 * np.cos(0.5 * i) + 0.1 * np.sin(2.0 * i)
            result += amp * np.exp(-0.3 * (xi - phase)**2) * np.sin(freq * xi + 0.2 * np.cos(3.0 * xi))
            
        # Add adaptive ridge structures with enhanced variability
        for i in range(self.dim):
            xi = x[i]
            height = 1.8 + 0.6 * np.sin(0.7 * i)
            width = 0.2 + 0.8 * np.cos(0.6 * i)
            center = -4.5 + 9.0 * np.random.random() * self.decay_factors[i]
            result += height * np.exp(-0.4 * ((xi - center) / width)**2)
            
        # Add multi-scale ridge interactions with enhanced chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction scope
                coupling = 0.5 * self.decay_factors[i] * self.decay_factors[j] * np.sin(0.9 * (i + j) + 0.3 * np.cos(i*j))
                result += coupling * np.sin(0.6 * x[i]) * np.cos(0.4 * x[j] + 0.1 * np.sin(x[i]))
                
        # Add enhanced exponentially decaying noise with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            noise_amp = 0.25 * self.decay_factors[i] * np.sin(11.0 * xi + 0.6)
            result += noise_amp * np.cos(13.0 * xi) * np.sin(9.0 * xi + 0.2 * np.cos(xi))
            
        # Add enhanced chaotic ridge peaks with nested structures
        for i in range(self.dim):
            xi = x[i]
            # Nested ridges at different scales with enhanced complexity
            result += 1.5 * np.exp(-0.4 * ((xi - 1.2) / 0.25)**2) * np.sin(3.5 * xi + 0.3 * np.cos(xi))
            result += 1.1 * np.exp(-0.3 * ((xi + 1.8) / 0.4)**2) * np.cos(2.8 * xi + 0.2 * np.sin(xi))
            result += 0.8 * np.exp(-0.5 * ((xi - 2.8) / 0.6)**2) * np.sin(2.3 * xi + 0.1 * np.cos(2*xi))
            
        # Add enhanced dynamic coupling terms with varying interaction strengths
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                strength = 0.6 * self.decay_factors[i] * self.decay_factors[i+1]
                result += strength * np.sin(x[i] + x[i+1] + 0.2 * np.cos(x[i]*x[i+1])) * np.cos(0.7 * (x[i] - x[i+1]) + 0.1 * np.sin(x[i]))
                
        # Add enhanced global scaling with exponential decay
        global_scale = 1.2 + 0.4 * np.exp(-0.07 * self.dim)
        result *= global_scale
        
        return result