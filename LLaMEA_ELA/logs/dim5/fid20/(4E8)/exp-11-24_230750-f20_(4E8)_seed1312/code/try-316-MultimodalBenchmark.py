import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hybrid sine-cosine oscillatory component with adaptive frequency
        osc_component = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * x[i])
            amp = 1.0 + 0.7 * np.cos(0.3 * x[i]**2)
            osc_component += amp * np.sin(freq * x[i] + 0.5 * np.cos(1.5 * x[i]))
        
        # Adaptive parabolic valley structure with dynamic curvature
        valley = 0.0
        for i in range(self.dim):
            curvature = 0.5 + 0.8 * np.sin(0.6 * x[i])
            valley += curvature * (x[i] - 2.0 * np.sin(0.5 * x[i]))**2
        
        # Multi-peak Gaussian with dynamic center, variance, and amplitude
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(4):
                center = -3.5 + 1.8 * j
                variance = 0.8 + 0.6 * np.cos(0.4 * x[i])
                amplitude = 2.0 + 0.5 * np.sin(0.7 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with varying interaction strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coeff = 1.0 + 0.5 * np.cos(0.5 * x[i]) * np.sin(0.3 * x[j])
                coupling += coeff * (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] - x[j]))
        
        # Saddle-point structure with enhanced chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.4 * np.cos(0.7 * x[i]) * np.sin(0.5 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional high-frequency chaotic component
        chaos = 0.0
        for i in range(self.dim):
            chaos += 0.3 * np.cos(5.0 * x[i]) * np.sin(2.0 * x[i]) * np.cos(0.8 * x[i]**2)
        
        # Dimensionally adaptive weighting and normalization
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        return (0.25 * osc_component + 0.20 * valley + 0.25 * gaussian + 
                0.15 * coupling + 0.10 * saddle + 0.05 * chaos) * dim_factor