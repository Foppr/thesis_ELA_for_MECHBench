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
            a = 3.8 * (1 + 0.25 * np.sin(0.7 * i))
            if x[i] < 0.5:
                tent_val = a * x[i]
            else:
                tent_val = a * (1 - x[i])
            tent += 0.45 * tent_val * np.sin(25 * x[i]) ** 2
        
        # Dynamic Gaussian radial basis functions with time-varying widths and amplitudes
        gaussian = 0
        for i in range(self.dim):
            center = 4.3 * np.sin(0.45 * i)
            width = 0.55 + 0.45 * np.cos(0.55 * i)
            amplitude = 0.45 + 0.35 * np.sin(0.35 * i)
            gaussian += amplitude * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric polynomial cross-dimensional interactions with dynamic coupling strengths
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.1 + 0.35 * np.sin(0.85 * (i + j))
                asym_factor = 1.05 + 0.25 * np.cos(0.65 * (i - j))
                if i < j:
                    poly_cross += coupling_strength * asym_factor * x[i]**3 * x[j]**2
                else:
                    poly_cross += coupling_strength * asym_factor * x[i]**2 * x[j]**3
        
        # Quaternion-inspired cross-dimensional interactions with complex phase modulation
        quat_coupling = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                phase = 0.45 * np.sin(i * 0.75)
                scale = 1.15 + 0.35 * np.cos(i * 0.45)
                quat_coupling += scale * (np.tanh(x[i]) * np.cos(phase) + np.tanh(x[i+1]) * np.sin(phase)) * (x[i]**2 + x[i+1]**2)
        
        # Hyperbolic tangent-based coupling with dynamic scaling and multi-scale modulation
        tanh_coupling = 0
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                scale = 1.05 + 0.65 * np.sin(i * 0.55)
                tanh_coupling += scale * np.tanh(x[i]) * np.tanh(x[i+1]) * np.tanh(x[i+2]) * (x[i]**2 + x[i+1]**2 + x[i+2]**2)
        
        # Logarithmic conditioning with exponential dimensionality dependence and oscillatory modulation
        cond_factor = 1.0 + 0.95 * np.log(self.dim + 1) + 0.35 * np.exp(0.16 * self.dim) + 0.12 * np.sin(0.22 * self.dim)
        
        # Fractal-like self-similar structure with recursive polynomial terms and multi-scale oscillations
        fractal = 0
        for i in range(self.dim):
            fractal += 0.35 * (x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2) * np.sin(13.5 * x[i]) * np.cos(7.5 * x[i])
        
        # Additional noise-like component with sinusoidal modulation and multi-frequency interference
        noise = 0
        for i in range(self.dim):
            noise += 0.16 * np.sin(32 * x[i]) * np.cos(18 * x[i]) * np.exp(-0.13 * x[i]**2) + 0.06 * np.sin(42 * x[i])
        
        # Combine all components with appropriate weights and scaling
        return sphere + cond_factor * (0.37 * tent + 0.32 * gaussian + 0.27 * poly_cross + 0.22 * quat_coupling + 0.16 * tanh_coupling) + fractal + noise