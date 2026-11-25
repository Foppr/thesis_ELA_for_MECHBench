import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave modulations with fractal-like behavior
        osc_component = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]**2)
            amp = 1.5 + 1.0 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[i]**2)
            osc_component += amp * np.sin(freq * x[i] + 0.7 * np.cos(1.2 * x[i]) * np.sin(0.8 * x[i]))
        
        # Adaptive parabolic valley with fractal curvature
        valley = 0.0
        for i in range(self.dim):
            curvature = 0.3 + 1.2 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]**2)
            valley += curvature * (x[i] - 1.5 * np.sin(0.6 * x[i]))**2
        
        # Multi-peak Gaussian with dynamic center, variance, and amplitude
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.0 + 2.5 * j
                variance = 1.0 + 0.8 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i]**2)
                amplitude = 2.5 + 1.0 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i]**2)
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional polynomial coupling with chaotic interaction strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coeff = 1.5 + 0.8 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[j])
                coupling += coeff * (x[i]**2 + x[j]**2) * np.cos(0.7 * (x[i] - x[j]))
        
        # Saddle-point structure with enhanced chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 1.0 + 0.6 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional high-frequency chaotic component with dynamic phase
        chaos = 0.0
        for i in range(self.dim):
            phase = 0.5 + 0.3 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]**2)
            chaos += 0.4 * np.cos(6.0 * x[i]) * np.sin(3.0 * x[i]) * np.cos(phase * x[i]**2)
        
        # Dimensionally adaptive weighting and normalization
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.22 * osc_component + 0.18 * valley + 0.28 * gaussian + 
                0.18 * coupling + 0.12 * saddle + 0.02 * chaos) * dim_factor