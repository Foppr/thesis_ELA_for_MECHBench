import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with modified scaling
        result = np.sum(x**2) * 0.12
        
        # Fractal-like multimodal structure with enhanced self-similarity
        for i in range(self.dim):
            # Increased frequency variation and added phase modulation
            freq = 5 ** (i % 7 + 1) * (1 + 0.5 * np.sin(i * 0.9))
            phase = 0.6 * np.cos(i * 0.4)
            result += 3.5 * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.8 + phase)
            
        # Enhanced multi-resolution interference patterns
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling range
                # Increased interaction strength with distance-dependent scaling
                dist = abs(i - j)
                strength = 3.0 / (1 + np.log(1 + dist * 0.8))
                result += strength * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Enhanced nested valley structure with modified decay
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.25 * abs(x[i])) * np.sin(3.5 * x[i])
            
        # Multi-scale sinusoidal modulation with increased complexity
        scales = [1, 2, 3, 4, 6, 8]
        for scale in scales:
            if self.dim >= scale:
                sub_x = x[:scale]
                result += 1.1 * np.sin(np.sum(sub_x**4) / scale) * np.cos(np.sum(sub_x**3) / (scale * 2.5))
                
        # Enhanced asymmetric fractal penalty with higher-order terms
        if self.dim >= 6:
            for i in range(6):
                if i < self.dim:
                    # Increased penalty complexity with cubic and quintic terms
                    result += 0.7 * (x[i]**7 + x[i]**5 + x[i]**3) * np.exp(-0.35 * abs(x[i]))
                    
        # Enhanced global scaling factor with additional modulation
        result *= 1.0 + 0.25 * np.sin(np.sum(x**2) * 0.1) * np.cos(np.sum(x) * 0.06)
        
        return result