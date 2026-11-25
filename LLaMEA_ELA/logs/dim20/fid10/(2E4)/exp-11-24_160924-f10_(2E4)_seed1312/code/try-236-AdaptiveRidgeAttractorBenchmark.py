import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.attractor_centers = np.random.uniform(-3.0, 3.0, dim)
        self.attractor_strengths = np.random.uniform(1.0, 5.0, dim)
        self.ridge_parameters = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add periodic attractor contributions
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            ridge_param = self.ridge_parameters[i]
            
            # Attractor basin with periodic modulation and ridge structure
            distance = np.abs(xi - center)
            attractor_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.1 * xi**2))**2)
            
            # Add ridge-like gradient flow component
            ridge_component = ridge_param * np.sin(3.0 * xi) * np.cos(2.0 * xi)
            
            result += attractor_term + ridge_component
            
        # Add cross-dimensional coupling with adaptive noise
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Adaptive coupling strength based on dimension indices
                coupling_strength = 0.5 * (1.0 + np.sin(0.3 * (i - j)))
                
                # Cross-dimensional interaction with periodic modulation
                cross_term = coupling_strength * np.sin(xi * xj) * np.cos(0.5 * (xi + xj))
                result += cross_term
                
        # Add dimensionally adaptive noise
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i] * (1.0 + 0.2 * np.sin(0.7 * i))
            noise_component = noise_level * np.sin(10.0 * xi + 0.5 * i) * np.cos(5.0 * xi)
            result += noise_component
            
        # Add frequency-dependent modulation for enhanced complexity
        freq_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod += self.frequency_modulators[i] * np.sin(4.0 * xi + 0.3 * i)
        result += 0.1 * freq_mod**2
        
        # Add global scaling with non-linear transformation
        global_scale = 1.0 + 0.3 * np.tanh(np.sum(x) / self.dim)
        result *= global_scale
        
        return result