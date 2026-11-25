import numpy as np

class FractalChaoticPolynomialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial chaos expansion with fractal-like structure
        result = 0.0
        for i in range(self.dim):
            # Fractal-like polynomial terms with varying exponents
            poly_term = (x[i]**3 + 0.5*x[i]**2 + 0.3*x[i] + 0.1) * np.sin(i * 0.7)
            result += poly_term
            
        # Radial basis functions with fractal scaling and chaotic centers
        for i in range(self.dim):
            center = np.sin(i * 1.3) * 3.0
            width = 0.5 + 0.3 * np.cos(i * 0.9)
            radial = np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            result += 0.8 * radial * (1.0 + 0.2 * np.sin(i * 2.1))
            
        # Asymmetric harmonic oscillators with varying frequencies and damping
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.8)
            damping = 0.3 + 0.2 * np.cos(i * 1.2)
            harm_term = np.sin(freq * x[i]) * np.exp(-damping * abs(x[i]))
            result += 0.6 * harm_term
            
        # Cross-dimensional fractal coupling with recursive scaling
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, self.dim):
                scale_factor = 0.5 + 0.3 * np.sin((i+j) * 0.4)
                coupling = np.sin(x[i] * x[j]) * scale_factor
                coupling_sum += coupling / (1.0 + abs(x[i] - x[j])**1.5)
            result += 0.4 * coupling_sum
            
        # Multi-scale chaotic interaction with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.3 + 0.2 * np.sin(i * 0.6) * np.cos(j * 0.9)
                chaotic_coupling = np.sin(x[i] * x[j] * 1.7) * np.cos(x[i] + x[j] * 1.3)
                result += strength * chaotic_coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Fractal basin terms with varying depths and widths
        for i in range(self.dim):
            basin_depth = 1.0 + 0.5 * np.sin(i * 1.1)
            basin_width = 0.8 + 0.4 * np.cos(i * 0.7)
            basin_term = basin_depth * (x[i]**2 - basin_width)**2
            result += 0.3 * basin_term * np.exp(-0.1 * abs(x[i]))
            
        # High-frequency chaotic modulation with fractal-like behavior
        high_freq_mod = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(i * 0.3)
            mod_term = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.2)
            high_freq_mod += mod_term
        result += 0.5 * high_freq_mod
        
        # Global fractal scaling term
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x) * 0.5)
        result *= global_scale
        
        # Add structured noise with fractal characteristics
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 8.0) * np.cos(x[i] * 5.0) * (0.02 + 0.01 * np.abs(x[i]))
        result += 0.08 * noise
        
        return result