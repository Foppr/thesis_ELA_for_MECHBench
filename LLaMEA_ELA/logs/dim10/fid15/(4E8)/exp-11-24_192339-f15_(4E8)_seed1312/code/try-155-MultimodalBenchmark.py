import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced chaotic tent map with dynamic parameter modulation and frequency scaling
        tent = 0
        for i in range(self.dim):
            a = 3.9 * (1 + 0.3 * np.sin(0.6 * i))
            if x[i] < 0.5:
                tent_val = a * x[i]
            else:
                tent_val = a * (1 - x[i])
            tent += 0.4 * tent_val * np.sin(23 * x[i]) ** 2
        
        # Dynamic Gaussian radial basis functions with time-varying widths and amplitudes
        gaussian = 0
        for i in range(self.dim):
            center = 4.5 * np.sin(0.4 * i)
            width = 0.6 + 0.4 * np.cos(0.5 * i)
            amplitude = 0.5 + 0.3 * np.sin(0.3 * i)
            gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric polynomial cross-dimensional interactions with dynamic coupling strengths
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 + 0.4 * np.sin(0.8 * (i + j))
                asym_factor = 1.0 + 0.2 * np.cos(0.6 * (i - j))
                if i < j:
                    poly_cross += coupling_strength * asym_factor * x[i]**3 * x[j]**2
                else:
                    poly_cross += coupling_strength * asym_factor * x[i]**2 * x[j]**3
        
        # Quaternion-inspired cross-dimensional interactions with complex phase modulation
        quat_coupling = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                phase = 0.5 * np.sin(i * 0.7)
                scale = 1.2 + 0.3 * np.cos(i * 0.4)
                quat_coupling += scale * (np.tanh(x[i]) * np.cos(phase) + np.tanh(x[i+1]) * np.sin(phase)) * (x[i]**2 + x[i+1]**2)
        
        # Hyperbolic tangent-based coupling with dynamic scaling and multi-scale modulation
        tanh_coupling = 0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                scale = 1.0 + 0.6 * np.sin(i * 0.5)
                tanh_coupling += scale * np.tanh(x[i]) * np.tanh(x[i+1]) * np.tanh(x[i+2]) * (x[i]**2 + x[i+1]**2 + x[i+2]**2)
        
        # Logarithmic conditioning with exponential dimensionality dependence and oscillatory modulation
        cond_factor = 1.0 + 0.9 * np.log(self.dim + 1) + 0.3 * np.exp(0.15 * self.dim) + 0.1 * np.sin(0.2 * self.dim)
        
        # Fractal-like self-similar structure with recursive polynomial terms and multi-scale oscillations
        fractal = 0
        for i in range(self.dim):
            fractal += 0.3 * (x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.sin(13 * x[i]) * np.cos(7 * x[i])
        
        # Additional noise-like component with sinusoidal modulation and multi-frequency interference
        noise = 0
        for i in range(self.dim):
            noise += 0.15 * np.sin(31 * x[i]) * np.cos(17 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.05 * np.sin(41 * x[i])
        
        # Combine all components with appropriate weights and scaling
        return sphere + cond_factor * (0.35 * tent + 0.3 * gaussian + 0.25 * poly_cross + 0.2 * quat_coupling + 0.15 * tanh_coupling) + fractal + noise