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
            freq = 2.0 + 5.0 * np.sin(0.9 * self.t + i * 0.6)
            amp = 1.5 + 0.8 * np.cos(0.8 * self.t + i * 0.5)
            result += amp * (xi**3) * np.sin(freq * xi) * np.cos(0.4 * xi**2)
            
        # Enhanced dynamic coupling with exponentially increasing interaction
        coupling_strength = 1.5 + 0.7 * np.sin(1.0 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially growing interaction terms with stronger coupling
                interaction = coupling_strength * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(1.5 * (x[i] + x[j]) + 0.6 * self.t)
                result += interaction * (x[i]**3 + x[j]**3)
                
        # Stronger adaptive noise with fractal-like characteristics
        noise_amp = 0.4 + 0.3 * np.sin(1.2 * self.t)
        noise_freq = 7.0 + 5.0 * np.cos(1.0 * self.t)
        noise = 0.0
        for i in range(self.dim):
            # Fractal-like noise pattern with multiple harmonics
            harmonic = np.sin(noise_freq * x[i] + self.t) + 0.6 * np.sin(2 * noise_freq * x[i] + 2 * self.t) + 0.3 * np.sin(3 * noise_freq * x[i] + 3 * self.t)
            noise += noise_amp * harmonic * np.random.normal(0, 1)
            
        # Multi-scale periodic modulations with chaotic phase shifts
        multi_scale = 0.0
        scales = [1.5, 2.5, 3.5, 4.5]
        for scale in scales:
            for i in range(self.dim):
                phase_shift = np.sin(0.9 * self.t + i * 0.7)
                multi_scale += np.sin(scale * x[i] + phase_shift) * np.cos(scale * x[i] + 0.8 * self.t) * (x[i]**4)
                
        # Adaptive weighting with chaotic coefficients
        w1 = 0.7 + 0.3 * np.sin(0.8 * self.t)
        w2 = 0.2 + 0.2 * np.cos(0.7 * self.t)
        w3 = 0.1 + 0.1 * np.sin(0.9 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result