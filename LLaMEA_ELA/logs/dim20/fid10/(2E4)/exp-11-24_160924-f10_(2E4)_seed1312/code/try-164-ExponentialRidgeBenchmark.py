import numpy as np

class ExponentialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay factors and ridge parameters
        self.decay_factors = [np.exp(-0.1 * i) for i in range(dim)]
        self.ridge_params = [(np.sin(0.5 * i), np.cos(0.3 * i)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add exponential decay sinusoidal components
        for i in range(self.dim):
            xi = x[i]
            amp = 2.0 * self.decay_factors[i]
            freq = 1.0 + 0.5 * np.sin(0.7 * i)
            phase = 0.3 * np.cos(0.4 * i)
            result += amp * np.exp(-0.5 * (xi - phase)**2) * np.sin(freq * xi)
            
        # Add adaptive ridge structures with varying heights and widths
        for i in range(self.dim):
            xi = x[i]
            height = 1.5 + 0.8 * np.sin(0.6 * i)
            width = 0.3 + 0.7 * np.cos(0.5 * i)
            center = -4.0 + 8.0 * np.random.random() * self.decay_factors[i]
            result += height * np.exp(-0.5 * ((xi - center) / width)**2)
            
        # Add multi-scale ridge interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction scope
                coupling = 0.4 * self.decay_factors[i] * self.decay_factors[j] * np.sin(0.8 * (i + j))
                result += coupling * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                
        # Add exponentially decaying noise with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            noise_amp = 0.2 * self.decay_factors[i] * np.sin(10.0 * xi + 0.5)
            result += noise_amp * np.cos(12.0 * xi) * np.sin(8.0 * xi)
            
        # Add chaotic ridge peaks with nested structures
        for i in range(self.dim):
            xi = x[i]
            # Nested ridges at different scales
            result += 1.2 * np.exp(-0.5 * ((xi - 1.0) / 0.3)**2) * np.sin(3.0 * xi)
            result += 0.9 * np.exp(-0.5 * ((xi + 1.5) / 0.5)**2) * np.cos(2.5 * xi)
            result += 0.6 * np.exp(-0.5 * ((xi - 2.5) / 0.7)**2) * np.sin(2.0 * xi)
            
        # Add dynamic coupling terms with varying interaction strengths
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                strength = 0.5 * self.decay_factors[i] * self.decay_factors[i+1]
                result += strength * np.sin(x[i] + x[i+1]) * np.cos(0.6 * (x[i] - x[i+1]))
                
        # Add global scaling with exponential decay
        global_scale = 1.0 + 0.5 * np.exp(-0.05 * self.dim)
        result *= global_scale
        
        return result