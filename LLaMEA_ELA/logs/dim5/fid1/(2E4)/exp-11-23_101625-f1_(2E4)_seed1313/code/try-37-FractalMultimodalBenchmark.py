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
            # Modified frequencies with more irregular spacing
            freq = 3 ** (i % 5 + 1) * (1 + 0.3 * np.sin(i * 0.7))
            result += 2.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
            
        # Multi-resolution interference patterns with altered coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                # Increased interaction strength
                strength = 2.0 / (1 + np.log(1 + abs(i-j) * 0.5))
                result += strength * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j]))
                
        # Modified nested valley structure with different decay
        for i in range(self.dim):
            result += 1.0 * np.exp(-0.15 * abs(x[i])) * np.sin(2.5 * x[i])
            
        # Multi-scale sinusoidal modulation with modified amplitudes
        scales = [1, 2, 3, 6]
        for scale in scales:
            if self.dim >= scale:
                sub_x = x[:scale]
                result += 0.7 * np.sin(np.sum(sub_x**3) / scale) * np.cos(np.sum(sub_x**2) / (scale * 1.5))
                
        # Modified asymmetric fractal penalty with increased complexity
        if self.dim >= 4:
            for i in range(4):
                if i < self.dim:
                    # Increased penalty complexity
                    result += 0.4 * (x[i]**5 + x[i]**3) * np.exp(-0.25 * abs(x[i]))
                    
        # Adjusted global scaling factor
        result *= 1.0 + 0.15 * np.sin(np.sum(x**2) * 0.06)
        
        return result