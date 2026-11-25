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
            freq = 2.0 + 3.0 * np.sin(0.6 * self.t + i * 0.4)
            amp = 0.7 + 0.3 * np.cos(0.5 * self.t + i * 0.3)
            result += amp * (xi**3) * np.sin(freq * xi)
            
        # Enhanced dynamic coupling with modified interaction terms
        coupling_strength = 0.5 + 0.3 * np.sin(0.7 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger interaction between dimensions
                interaction = coupling_strength * np.sin(0.8 * (x[i] + x[j]) + 0.4 * self.t)
                result += interaction * (x[i]**3 + x[j]**3)
                
        # Modified noise with increased variability
        noise_amp = 0.15 + 0.2 * np.sin(0.9 * self.t)
        noise_freq = 4.0 + 3.0 * np.cos(0.8 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_amp * np.sin(noise_freq * x[i] + self.t) * np.random.normal(0, 1)
            
        # Modified multi-scale periodic modulations with additional nonlinear terms
        multi_scale = 0.0
        scales = [1.5, 2.5, 3.5]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(scale * x[i] + self.t) * np.cos(scale * x[i] + 0.6 * self.t) * (x[i]**2)
                
        # Adaptive weighting of components with modified coefficients
        w1 = 0.7 + 0.15 * np.sin(0.6 * self.t)
        w2 = 0.2 + 0.1 * np.cos(0.5 * self.t)
        w3 = 0.1 + 0.08 * np.sin(0.7 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result