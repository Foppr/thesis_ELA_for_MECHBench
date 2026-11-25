import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for dynamic behavior
        tent_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent_term += 2 * xi
            else:
                tent_term += 2 * (1 - xi)
        result = 0.5 * tent_term**2
        
        # Spherical harmonics component for rotational symmetry breaking
        sph_harm = 0.0
        for i in range(self.dim):
            sph_harm += np.sin(3 * x[i]) * np.cos(4 * x[i])
        result += 0.3 * sph_harm**2
        
        # Asymmetric Gaussian valleys with varying widths
        valley_term = 0.0
        for i in range(self.dim):
            # Different widths and positions for each dimension
            width = 1.0 + 0.5 * np.sin(i)
            center = 2.0 * np.cos(i)
            valley_term += np.exp(-0.5 * ((x[i] - center) / width)**2)
        result += 0.4 * valley_term
        
        # Cross-dimensional coupling with sine-wave interference
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(5 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        result += 0.2 * cross_term**2
        
        # Non-separable polynomial interactions with exponential decay
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        result += 0.3 * poly_term
        
        # Add a global minimum at origin with local perturbations
        result += 0.1 * np.sum(x**4) + 0.05 * np.sum(np.abs(x))
        
        return result