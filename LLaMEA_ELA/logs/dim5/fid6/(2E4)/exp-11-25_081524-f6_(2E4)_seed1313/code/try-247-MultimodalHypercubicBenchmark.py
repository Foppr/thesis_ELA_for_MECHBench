import numpy as np

class MultimodalHypercubicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base hypercubic structure with enhanced chaotic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic oscillations with dynamic frequencies and amplitudes
            freq = 3.5 + 1.5 * np.sin(0.7 * self.t + i * 0.5)
            amp = 1.2 + 0.2 * np.cos(0.6 * self.t + i * 0.4)
            result += amp * (xi**4) * np.sin(freq * xi) + 0.6 * (xi**2) * np.cos(freq * xi)
            
        # Stronger dynamic coupling with modified interaction strengths
        coupling_strength = 0.8 + 0.2 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling with sine and cosine interaction terms
                interaction = coupling_strength * (np.sin(1.3 * (x[i] + x[j]) + 0.4 * self.t) + 
                                                   np.cos(1.6 * (x[i] - x[j]) + 0.3 * self.t))
                result += interaction * (x[i]**2 + x[j]**2)
                
        # Modified noise with increased variability and temporal correlation
        noise_amp = 0.4 + 0.15 * np.sin(1.0 * self.t)
        noise_freq = 4.5 + 2.5 * np.cos(0.9 * self.t)
        noise = 0.0
        for i in range(self.dim):
            # Add temporal correlation to noise
            noise += noise_amp * np.sin(noise_freq * x[i] + self.t) * np.random.normal(0, 1)
            
        # Multi-scale periodic modulations with additional nonlinear terms
        multi_scale = 0.0
        scales = [1.2, 2.8, 3.2]
        for scale in scales:
            for i in range(self.dim):
                multi_scale += np.sin(scale * x[i] + self.t) * np.cos(scale * x[i] + 0.6 * self.t) * (x[i]**4)
                
        # Adaptive weighting of components with modified coefficients
        w1 = 0.8 + 0.1 * np.sin(0.7 * self.t)
        w2 = 0.25 + 0.1 * np.cos(0.6 * self.t)
        w3 = 0.15 + 0.05 * np.sin(0.8 * self.t)
        
        result = w1 * result + w2 * noise + w3 * multi_scale
        return result