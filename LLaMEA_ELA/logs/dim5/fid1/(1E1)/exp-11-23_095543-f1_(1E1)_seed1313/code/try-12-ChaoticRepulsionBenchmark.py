import numpy as np

class ChaoticRepulsionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5] if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        if np.allclose(x, 0.0):
            return 0.0
            
        # Initialize result
        result = 0.0
        
        # Exponential repulsion fields centered at various points
        center_points = []
        for i in range(min(5, self.dim)):
            point = np.array([np.sin(i) * 2.0, np.cos(i) * 2.0] + [0.0] * (self.dim - 2)) if self.dim > 2 else np.array([np.sin(i) * 2.0, np.cos(i) * 2.0])
            center_points.append(point)
            
        # Calculate repulsion effect from multiple centers
        for center in center_points:
            dist = np.linalg.norm(x - center)
            if dist > 0:
                result += 10.0 * np.exp(-dist**2 / (2.0 * 0.5**2)) / (dist + 1e-8)
        
        # Add sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[(i + 1) % self.dim])
            
        # Add chaotic behavior using logistic map-like terms
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi / 2.0)
        result += 0.5 * chaotic_term**2
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.1 * x[i]**6 + 0.05 * x[i]**5
            
        # Add cross-term interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.3 * np.exp(-dist) * x[i] * x[j]
                
        # Add a final chaotic scaling factor
        scale_factor = 1.0 + 0.2 * np.sin(np.sum(x**2))
        result *= scale_factor
        
        return result