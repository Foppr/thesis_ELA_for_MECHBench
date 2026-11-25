import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.5 * np.sum(x**2)
        
        # Chaotic harmonic oscillations with exponential decay
        for i in range(self.dim):
            freq = 3 * np.exp(0.1 * i) + 2 * np.sin(i * 0.7)
            amp = 2 * np.exp(-0.05 * i**2) * (1 + 0.2 * np.cos(i * 0.5))
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.log(1 + abs(x[i]))
            
        # Exponential penalty landscape with chaotic scaling
        for i in range(self.dim):
            penalty = np.exp(2 * abs(x[i]) / 5.0) * (1 + 0.1 * np.sin(i * 0.8))
            result += penalty * (1 + 0.3 * np.cos(x[i] * 4))
            
        # Nested gradient valleys with varying steepness
        for i in range(self.dim):
            valley_depth = 1.5 * (1 + 0.2 * np.sin(i * 0.6)) * np.exp(-0.1 * abs(x[i]))
            result += valley_depth * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Cross-dimensional chaotic coupling with time-varying weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(min(i+3, self.dim)):
                weight = 0.5 * (1 + np.sin(i * j * 0.4)) * np.exp(-0.02 * (i-j)**2)
                coupling_sum += weight * np.sin(2**j * x[j]) * np.cos(2**i * x[i])
            result += 0.3 * coupling_sum
            
        # Asymmetric exponential barriers with chaotic positioning
        for i in range(self.dim):
            barrier_pos = 2 * np.sin(i * 0.5) + 1.5
            barrier_height = 1.2 * (1 + 0.1 * np.cos(i * 0.3))
            result += barrier_height * np.exp(-0.5 * (x[i] - barrier_pos)**2) * (1 + 0.2 * np.sin(x[i]))
            
        # Multi-scale fractal ridge patterns with chaotic amplitude modulation
        for i in range(self.dim):
            scale = 4 ** (i % 4 + 1)
            amp_mod = 0.8 * (1 + 0.15 * np.sin(i * 0.7))
            result += amp_mod * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.2) * np.log(1 + abs(x[i]))
            
        # Chaotic noise component with frequency modulation
        noise_freq = 8 + 3 * np.sin(self.dim * 0.3)
        result += 0.25 * np.sum(np.sin(noise_freq * x) * np.cos(noise_freq * x * 0.4)) * (1 + 0.1 * np.mean(x))
        
        return result