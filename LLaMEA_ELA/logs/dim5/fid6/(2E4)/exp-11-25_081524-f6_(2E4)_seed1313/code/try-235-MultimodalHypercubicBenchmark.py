import numpy as np

class MultimodalHypercubicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base hypercubic structure with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic cubic terms with time-varying frequencies
            freq = 1.0 + 3.0 * np.sin(0.5 * self.t + i * 0.4)
            amp = 0.7 + 0.3 * np.cos(0.3 * self.t + i * 0.25)
            result += amp * (xi**3) * np.sin(freq * xi + 0.1 * np.sin(2.0 * self.t))
            
        # Enhanced nested periodic hypercubes with dynamic coupling
        coupling_strength = 0.4 + 0.3 * np.sin(0.7 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction between dimensions with chaotic modulation
                interaction = coupling_strength * np.sin(0.5 * (x[i] + x[j]) + 0.4 * np.cos(0.8 * self.t))
                result += interaction * (x[i]**2 + x[j]**2) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Chaotic noise with time-varying amplitude and frequency
        noise_amp = 0.15 + 0.2 * np.sin(0.9 * self.t)
        noise_freq = 4.0 + 3.0 * np.cos(0.6 * self.t)
        noise = 0.0
        for i in range(self.dim):
            noise += noise_amp * np.sin(noise_freq * x[i] + 0.5 * np.sin(1.2 * self.t)) * np.random.normal(0, 1)
            
        # Multi-scale chaotic modulations with varying amplitudes and frequencies
        multi_scale = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(scale * x[i] + 0.2 * np.sin(1.5 * self.t)) * np.cos(scale * x[i] + 0.6 * np.cos(1.3 * self.t))
                
        # Adaptive weighting of components with chaotic modulation
        w1 = 0.5 + 0.2 * np.sin(0.6 * self.t)
        w2 = 0.3 + 0.15 * np.cos(0.5 * self.t)
        w3 = 0.2 + 0.1 * np.sin(0.7 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result