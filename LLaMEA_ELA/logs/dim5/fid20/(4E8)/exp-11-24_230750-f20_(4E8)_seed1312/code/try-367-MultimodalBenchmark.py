import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation with dynamic frequency and amplitude
        chaotic_component = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
            amp = 1.2 + 0.8 * np.sin(0.5 * x[i])
            chaotic_component += amp * np.sin(freq * x[i] + 0.2 * np.sin(3.0 * x[i]))
        
        # Asymmetric Gaussian peak structure with dynamic heights and widths
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                height = 2.5 + 1.8 * np.cos(0.6 * x[i])
                width = 0.5 + 0.3 * np.sin(0.4 * x[i])
                gaussian_peaks += height * np.exp(-0.5 * ((x[i] - j) / width)**2)
        
        # Cross-dimensional polynomial coupling with varying interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                strength = 1.0 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                coupling += strength * (x[i]**2 + x[j]**2) * np.sin(0.7 * (x[i] - x[j]))
        
        # Dynamic elliptic valley with multi-scale harmonics
        valley = 0.0
        for i in range(self.dim):
            a = 1.0 + 0.5 * np.cos(0.3 * x[i])
            b = 0.8 + 0.4 * np.sin(0.2 * x[i])
            c = 1.2 + 0.6 * np.tan(0.1 * x[i])
            valley += ((x[i] - a * np.sin(0.5 * x[i]))**2 / a + 
                      (x[i] - b * np.cos(0.4 * x[i]))**2 / b + 
                      (x[i] - c * np.exp(-0.1 * x[i]))**2 / c)
        
        # Multi-scale saddle-point structure with varying modulations
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                mod1 = 0.7 + 0.3 * np.sin(0.5 * x[i])
                mod2 = 0.6 + 0.4 * np.cos(0.3 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * mod1 + (x[i+1]**2 - x[i]**2) * mod2
        
        # High-frequency oscillatory component with exponential decay
        high_freq = 0.0
        for i in range(self.dim):
            amp = 0.9 + 0.6 * np.sin(1.2 * x[i])
            high_freq += amp * np.sin(15.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Dimensionally varying normalization factor
        norm_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return (0.15 * chaotic_component + 0.25 * gaussian_peaks + 
                0.20 * coupling + 0.18 * valley + 0.12 * saddle + 0.08 * high_freq) * norm_factor