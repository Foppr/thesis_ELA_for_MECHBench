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
            # Periodic cubic terms with adaptive frequencies
            freq = 1.0 + 2.0 * np.sin(0.5 * self.t + i * 0.3)
            amp = 0.5 + 0.5 * np.cos(0.4 * self.t + i * 0.2)
            result += amp * (xi**3) * np.sin(freq * xi)
            
        # Nested periodic hypercubes with dynamic coupling
        coupling_strength = 0.3 + 0.2 * np.sin(0.6 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic interaction between dimensions
                interaction = coupling_strength * np.sin(0.5 * (x[i] + x[j]) + 0.3 * self.t)
                result += interaction * (x[i]**2 + x[j]**2)
                
        # Adaptive noise with time-varying amplitude and frequency
        noise_amp = 0.1 + 0.15 * np.sin(0.8 * self.t)
        noise_freq = 3.0 + 2.0 * np.cos(0.7 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_amp * np.sin(noise_freq * x[i] + self.t) * np.random.normal(0, 1)
            
        # Multi-scale periodic modulations with varying amplitudes
        multi_scale = 0.0
        scales = [1.0, 2.0, 3.0]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(scale * x[i] + self.t) * np.cos(scale * x[i] + 0.5 * self.t)
                
        # Adaptive weighting of components
        w1 = 0.6 + 0.1 * np.sin(0.5 * self.t)
        w2 = 0.3 + 0.1 * np.cos(0.4 * self.t)
        w3 = 0.1 + 0.05 * np.sin(0.6 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result