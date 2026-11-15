import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.3  # Fractal dimension parameter
        self.scale_factors = np.array([2**(i/3) for i in range(dim)])
        self.rotation_matrices = [self._generate_rotation_matrix(i) for i in range(dim)]
        
    def _generate_rotation_matrix(self, seed):
        np.random.seed(seed)
        theta = np.random.uniform(0, 2*np.pi)
        return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    
    def _fractal_basis(self, x, scale):
        # Generate fractal-like basis functions
        result = 0.0
        for i in range(1, 6):
            freq = 2**i * scale
            result += np.sin(freq * x) / (freq**self.fractal_dim)
        return result
    
    def _hierarchical_correlation(self, x):
        # Create hierarchical correlations between dimensions
        corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-dependent correlation strength
                scale_factor = self.scale_factors[i] * self.scale_factors[j]
                corr += scale_factor * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        return corr
    
    def _self_similar_structure(self, x):
        # Create self-similar structure using recursive scaling
        result = 0.0
        for i in range(self.dim):
            # Apply different scales to each dimension
            scaled_x = x[i] / self.scale_factors[i]
            # Fractal-like contribution
            result += self._fractal_basis(scaled_x, self.scale_factors[i])
        return result
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Global fractal component
        result += self._self_similar_structure(x)
        
        # Add hierarchical correlation terms
        result += 0.5 * self._hierarchical_correlation(x)
        
        # Add multi-scale sinusoidal components
        for i in range(self.dim):
            scale = self.scale_factors[i]
            result += 0.3 * np.sin(scale * x[i]) * np.cos(scale * x[i]**2)
        
        # Add fractal-based interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-invariant interaction
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
                result += 0.2 * interaction / (1 + np.abs(x[i] - x[j]))
        
        # Add self-similar polynomial terms
        for i in range(self.dim):
            result += 0.1 * x[i]**3 * np.sin(x[i]**2)
        
        # Add multi-fractal penalty
        penalty = 0.0
        for i in range(self.dim):
            penalty += np.abs(x[i])**self.fractal_dim
        result += 0.4 * penalty
        
        # Add scale-invariant noise
        noise = 0.05 * np.sum(np.sin(self.scale_factors * x))
        result += noise
        
        # Add fractal dimension modulation
        mod = 1.0 + 0.3 * np.sin(np.sum(x) / self.dim)
        result *= mod
        
        # Add boundary effect
        boundary = 0.0
        for i in range(self.dim):
            boundary += 10 * (np.abs(x[i]) - 5.0)**2
        result += boundary
        
        return result