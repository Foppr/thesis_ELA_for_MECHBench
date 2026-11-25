import numpy as np

class MultimodalHypercubicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base hypercubic structure with periodic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic oscillations with modified frequencies
            freq = 2.5 + 2.5 * np.sin(0.6 * self.t + i * 0.4)
            amp = 0.8 + 0.2 * np.cos(0.5 * self.t + i * 0.3)
            result += amp * (xi**3) * np.sin(freq * xi)
            
        # Enhanced dynamic coupling with modified interaction terms
        coupling_strength = 0.6 + 0.25 * np.sin(0.7 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger interaction between dimensions
                interaction = coupling_strength * np.sin(0.9 * (x[i] + x[j]) + 0.3 * self.t)
                result += interaction * (x[i]**2 + x[j]**2)
                
        # Modified noise with increased variability
        noise_amp = 0.2 + 0.15 * np.sin(0.9 * self.t)
        noise_freq = 3.5 + 2.5 * np.cos(0.8 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_amp * np.sin(noise_freq * x[i] + self.t) * np.random.normal(0, 1)
            
        # Modified multi-scale periodic modulations with additional nonlinear terms
        multi_scale = 0.0
        scales = [1.2, 2.2, 3.2]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(scale * x[i] + self.t) * np.cos(scale * x[i] + 0.5 * self.t) * (x[i]**3)
                
        # Adaptive weighting of components with modified coefficients
        w1 = 0.65 + 0.18 * np.sin(0.6 * self.t)
        w2 = 0.25 + 0.12 * np.cos(0.5 * self.t)
        w3 = 0.15 + 0.07 * np.sin(0.7 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result