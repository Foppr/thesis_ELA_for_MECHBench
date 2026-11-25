import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic oscillatory component with quaternion-inspired modulation
        chaotic_osc = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i]) + 0.3 * np.sin(0.3 * x[i]**2)
            amp_mod = 1.0 + 0.4 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i])
            chaotic_osc += amp_mod * np.sin(freq_mod * x[i] + 0.5 * np.sin(2.0 * x[i]))
        
        # Adaptive fractal coupling with dynamic rotation and scaling
        fractal_coupling = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
            rot_angle = 0.5 * np.sin(0.4 * x[i])
            fractal_coupling += scale_factor * (np.sin(2.0 * x[i] + rot_angle) + np.cos(1.5 * x[i] - rot_angle))
        
        # Multi-peak Gaussian with dynamic variance and cross-dimensional interaction
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -3.0 + 2.0 * j
                variance = 0.8 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
                amplitude = 1.5 + 0.3 * np.sin(0.6 * x[i]**2) * np.cos(0.4 * x[i])
                gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional nonlinear coupling with dynamic weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+3, self.dim)):
                if i != j:
                    weight = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                    coupling += weight * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i] - x[j]))
        
        # Saddle-point structure with enhanced chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.7 + 0.3 * np.sin(0.9 * x[i]) * np.cos(0.5 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Additional high-frequency chaotic component for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.4 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(0.8 * x[i]**2)
        
        # Combined function with improved dimensionally adaptive weights and scaling
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.22 * chaotic_osc + 0.23 * fractal_coupling + 0.25 * gaussian + 
                0.18 * coupling + 0.12 * saddle + 0.07 * high_freq) * dim_factor