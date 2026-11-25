import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with chaotic interactions
        fractal = 0
        for i in range(self.dim):
            # More chaotic behavior with increased frequency modulation
            freq1 = 2**(i % 5) * (1 + 0.3 * np.sin(i))
            freq2 = 3**(i % 4) * (1 + 0.2 * np.cos(i))
            term = np.sin(freq1 * np.pi * x_norm[i]) * np.cos(freq2 * np.pi * x_norm[i])
            fractal += term / (1.0 + i * 0.2)
        
        # Modified harmonic oscillator with dynamic coupling
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 3) * (1 + 0.1 * np.sin(i))
            damp = 1.0 / (1.0 + 0.2 * i + 0.05 * i**2)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Multi-scale interaction with exponential weights
        interaction = 0
        scales = [1, 2, 4, 8]  # Different scale values for complex interactions
        for scale in scales:
            if scale <= self.dim:
                # Exponential weighted grouped interactions
                group_sum = np.sum(x_norm[:scale]**2)
                weight = np.exp(-0.5 * scale)
                interaction += weight * np.sin(np.pi * group_sum) * np.cos(2 * np.pi * group_sum)
        
        # Enhanced asymmetric conditioning with modified exponential terms
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**4) * np.exp(-0.6 * x_norm[i]**2)  # Increased exponent
            else:
                conditioning += (x_norm[i]**6) * np.exp(-0.3 * x_norm[i]**2)  # Higher power and different decay
        
        # Improved boundary attraction with quadratic penalty
        boundary = 0
        for i in range(self.dim):
            dist = np.abs(x_norm[i]) - 1
            boundary += 12 * dist**4 + 8 * dist**6  # Enhanced boundary influence with higher-order terms
        
        # Combined result with refined scaling factors
        result = 2.0 * fractal + 1.3 * harmonic + 1.2 * interaction + 0.8 * conditioning + 0.6 * boundary
        
        return result