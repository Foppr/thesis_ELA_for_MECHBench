import numpy as np

class HybridChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants for saddle point distribution
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        # Asymmetric saddle parameters
        self.saddle_centers = np.random.uniform(-3.0, 3.0, dim)
        self.saddle_heights = np.random.uniform(0.5, 2.0, dim)
        
    def _generate_chaotic_sequence(self):
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic widths
        result = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.5 * self.chaotic_sequence[i]
            result += np.exp(-0.5 * np.sum(((x - self.saddle_centers) / width)**2))
        
        # Sinusoidal oscillation component with varying frequencies
        for i in range(self.dim):
            freq = 2 * (1 + self.chaotic_sequence[i])
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Asymmetric saddle point component
        for i in range(self.dim):
            center = self.saddle_centers[i]
            height = self.saddle_heights[i]
            # Asymmetric quadratic term
            diff = x[i] - center
            if diff < 0:
                result += height * diff**2 * (1 + 0.1 * self.chaotic_sequence[i])
            else:
                result += height * diff**2 * (1 - 0.1 * self.chaotic_sequence[i])
        
        # Chaotic coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add a global minimum attractor with chaotic scaling
        scale = 0.02 + 0.03 * self.chaotic_sequence[0]
        result += scale * np.sum(x**2)
        
        # Add chaotic noise to increase landscape complexity
        noise = 0.01 * np.sum(np.sin(self.chaotic_sequence * x**3))
        result += noise
        
        return result