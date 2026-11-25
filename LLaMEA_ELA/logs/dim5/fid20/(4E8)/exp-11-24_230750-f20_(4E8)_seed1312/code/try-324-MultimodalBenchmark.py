import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillatory component with modified modulation
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.6 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]) + 0.4 * np.sin(0.4 * x[i]**2)
            amp_mod = 1.0 + 0.5 * np.cos(0.6 * x[i]) * np.sin(0.8 * x[i])
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.6 * np.sin(2.5 * x[i]))
        
        # Adaptive fractal coupling with altered rotation and scaling
        fractal_coupling = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.9 * x[i]) * np.cos(0.7 * x[i])
            rot_angle = 0.6 * np.sin(0.5 * x[i])
            fractal_coupling += scale_factor * (np.sin(2.5 * x[i] + rot_angle) + np.cos(1.8 * x[i] - rot_angle))
        
        # Multi-peak Gaussian with altered variance and cross-dimensional interaction
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -2.5 + 2.5 * j
                variance = 0.9 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
                amplitude = 1.7 + 0.2 * np.sin(0.7 * x[i]**2) * np.cos(0.5 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional nonlinear coupling with modified weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    weight = 0.6 + 0.4 * np.sin(0.4 * (x[i] + x[j]))
                    coupling += weight * (x[i]**3 + x[j]**3) * np.cos(0.5 * (x[i] - x[j]))
        
        # Saddle-point structure with modified chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.2 * np.sin(1.0 * x[i]) * np.cos(0.6 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional high-frequency chaotic component for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.5 * np.sin(4.5 * x[i]) * np.cos(3.5 * x[i]) * np.sin(0.9 * x[i]**2)
        
        # Combined function with adjusted dimensionally adaptive weights and scaling
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return (0.24 * chaotic_osc + 0.25 * fractal_coupling + 0.23 * gaussian + 
                0.17 * coupling + 0.11 * saddle + 0.06 * high_freq) * dim_factor