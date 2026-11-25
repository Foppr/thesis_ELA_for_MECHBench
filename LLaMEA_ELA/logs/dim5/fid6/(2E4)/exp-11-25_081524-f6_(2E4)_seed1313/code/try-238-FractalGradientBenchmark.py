import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like base landscape with self-similar structure
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal scaling with chaotic exponents
            scale = 1.0 + 0.5 * np.sin(0.6 * self.t + i * 0.3)
            exponent = 2.0 + 1.5 * np.cos(0.4 * self.t + i * 0.7)
            result += scale * (xi**exponent) * np.sin(xi * (1.0 + 0.3 * np.cos(0.5 * self.t + i * 0.2)))
            
        # Dynamic gradient modulation with time-varying coefficients
        grad_mod = 1.0 + 0.4 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Enhanced gradient effects with periodic modulation
            result += grad_mod * xi * np.cos(xi * (0.5 + 0.2 * np.sin(0.7 * self.t + i * 0.4)))
            
        # Time-varying periodic interference patterns
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling to maintain separability
                # Interference with dynamic phase shifts and amplitudes
                amp = 0.5 + 0.3 * np.sin(0.9 * self.t + i * 0.2 + j * 0.1)
                phase = 0.3 * self.t + i * 0.4 + j * 0.3
                interference += amp * np.sin((x[i] - x[j]) * (1.0 + 0.2 * np.cos(phase))) * \
                               np.cos((x[i] + x[j]) * (0.8 + 0.1 * np.sin(phase)))
                
        # Fractal-like periodicity with chaotic frequency ratios
        fractal_period = 0.0
        freq_ratios = [1.0, 1.618, 2.718, 3.142]
        for k, ratio in enumerate(freq_ratios):
            for i in range(self.dim):
                # Multi-scale periodic components with varying frequencies
                freq = ratio * (1.0 + 0.2 * np.sin(0.5 * self.t + i * 0.3))
                fractal_period += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * \
                                 np.sin(0.7 * self.t + k * 0.8 + i * 0.2)
                
        # Adaptive weighting and combination of components
        w1 = 0.6 + 0.2 * np.sin(0.6 * self.t)
        w2 = 0.3 + 0.15 * np.cos(0.5 * self.t)
        w3 = 0.1 + 0.05 * np.sin(0.8 * self.t)
        
        result = w1 * result + w2 * interference + w3 * fractal_period
        return result