import numpy as np

class FractalRidgeGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 1.7
        self.ridge_strength = 2.0
        self.gaussian_scale = 0.5
        self.ruggedness = 3.0
        self.coherence_factor = 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal ridge component with chaotic scaling
        ridge_term = 0.0
        for i in range(self.dim):
            # Chaotic ridge interaction with fractal scaling
            scale_factor = np.sin(i * np.pi / self.dim) ** self.fractal_dimension
            ridge_term += scale_factor * (x[i] ** 2 + self.ridge_strength * np.sin(x[i] * 10.0))
        
        # Multi-scale Gaussian perturbations
        gaussian_term = 0.0
        for level in range(1, min(6, self.dim + 1)):
            level_scale = self.gaussian_scale / (level ** 1.2)
            level_sum = 0.0
            for i in range(self.dim):
                # Gaussian perturbation with multi-scale frequency
                freq = 2.0 ** level
                level_sum += np.exp(-0.5 * ((x[i] - np.sin(freq * x[i])) / level_scale) ** 2)
            gaussian_term += level_sum
        
        # Ruggedness modulation through fractional powers
        rugged_term = 0.0
        for i in range(self.dim):
            rugged_term += (np.abs(x[i]) ** self.ruggedness) * np.cos(x[i] * 5.0)
        
        # Cross-dimensional coupling with coherence factor
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_term += (1.0 / dist) * np.sin(x[i] * x[j] * self.coherence_factor)
        
        # Combine all terms with adaptive weights
        total = (ridge_term * 0.3 + 
                gaussian_term * 0.4 + 
                rugged_term * 0.2 + 
                cross_term * 0.1)
        
        return total