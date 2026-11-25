import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.1
        
        # Fractal-like multimodal structure with self-similarity
        for i in range(self.dim):
            # Logarithmic scaling of frequencies with fractal dimension
            freq = 2 ** (i % 4 + 1) * (1 + 0.5 * np.sin(i))
            result += 2.0 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Multi-resolution interference patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for scalability
                # Logarithmic interaction strength
                strength = 1.5 / (1 + np.log(1 + abs(i-j)))
                result += strength * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Nested valley structure with exponential decay
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.1 * abs(x[i])) * np.sin(3 * x[i])
            
        # Multi-scale sinusoidal modulation with varying amplitudes
        scales = [1, 2, 4, 8]
        for scale in scales:
            if self.dim >= scale:
                # Apply to first 'scale' dimensions
                sub_x = x[:scale]
                result += 0.5 * np.sin(np.sum(sub_x**3) / scale) * np.cos(np.sum(sub_x**2) / scale)
                
        # Asymmetric fractal penalty with multi-scale critical points
        if self.dim >= 4:
            for i in range(4):
                if i < self.dim:
                    # Fractal-like penalty with increasing complexity
                    result += 0.3 * (x[i]**6 + x[i]**4) * np.exp(-0.2 * abs(x[i]))
                    
        # Global scaling factor to maintain balance
        result *= 1.0 + 0.1 * np.sin(np.sum(x**2) * 0.05)
        
        return result