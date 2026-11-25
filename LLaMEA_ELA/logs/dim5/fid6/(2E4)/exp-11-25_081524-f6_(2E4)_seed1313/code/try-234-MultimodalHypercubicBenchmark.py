import numpy as np

class MultimodalHypercubicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Base hypercubic structure with highly chaotic oscillations
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Extremely chaotic frequencies and amplitudes
            freq = 3.0 + 4.0 * np.sin(0.8 * self.t + i * 0.5)
            amp = 1.0 + 0.5 * np.cos(0.7 * self.t + i * 0.4)
            result += amp * (xi**4) * np.sin(freq * xi) * np.cos(0.3 * xi**2)
            
        # Enhanced dynamic coupling with exponentially increasing interaction
        coupling_strength = 1.0 + 0.5 * np.sin(0.9 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially growing interaction terms
                interaction = coupling_strength * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(1.2 * (x[i] + x[j]) + 0.5 * self.t)
                result += interaction * (x[i]**4 + x[j]**4)
                
        # Stronger adaptive noise with fractal-like characteristics
        noise_amp = 0.3 + 0.25 * np.sin(1.1 * self.t)
        noise_freq = 6.0 + 4.0 * np.cos(0.9 * self.t)
        noise = 0.0
        for i in range(self.dim):
            # Fractal-like noise pattern with multiple harmonics
            harmonic = np.sin(noise_freq * x[i] + self.t) + 0.5 * np.sin(2 * noise_freq * x[i] + 2 * self.t)
            noise += noise_amp * harmonic * np.random.normal(0, 1)
            
        # Multi-scale periodic modulations with chaotic phase shifts
        multi_scale = 0.0
        scales = [2.0, 3.0, 4.0, 5.0]
        for scale in scales:
            for i in range(self.dim):
                phase_shift = np.sin(0.8 * self.t + i * 0.6)
                multi_scale += np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] + 0.7 * self.t) * (x[i]**3)
                
        # Adaptive weighting with chaotic coefficients
        w1 = 0.8 + 0.2 * np.sin(0.7 * self.t)
        w2 = 0.15 + 0.15 * np.cos(0.6 * self.t)
        w3 = 0.05 + 0.05 * np.sin(0.8 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result