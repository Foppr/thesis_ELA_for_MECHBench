import numpy as np

class FractalChaoticPolynomialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial chaos expansion with enhanced fractal structure
        result = 0.0
        for i in range(self.dim):
            # Higher-order polynomial terms with dynamic coefficients
            poly_term = (x[i]**7 + 0.8*x[i]**6 + 0.65*x[i]**5 + 0.45*x[i]**4 + 0.3*x[i]**3 + 0.15*x[i]**2 + 0.05*x[i] + 0.02) * np.sin(i * 1.1)
            result += poly_term
            
        # Enhanced radial basis functions with multi-scale fractal centers and chaotic widths
        for i in range(self.dim):
            center = np.sin(i * 1.9) * 4.5 + 0.6 * np.cos(i * 1.3)
            width = 0.25 + 0.5 * np.cos(i * 1.4) + 0.15 * np.sin(i * 0.9)
            radial = np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            result += 1.5 * radial * (1.0 + 0.4 * np.sin(i * 2.8) * np.cos(i * 2.1))
            
        # Enhanced asymmetric harmonic oscillators with time-varying parameters
        for i in range(self.dim):
            freq = 4.0 + 0.9 * np.sin(i * 1.2)
            damping = 0.5 + 0.35 * np.cos(i * 1.7)
            harm_term = np.sin(freq * x[i]) * np.exp(-damping * abs(x[i])) * (1.0 + 0.25 * np.sin(i * 0.8))
            result += 1.0 * harm_term
            
        # Cross-dimensional fractal coupling with recursive scaling and dynamic weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, self.dim):
                scale_factor = 0.7 + 0.3 * np.sin((i+j) * 0.6)
                coupling = np.sin(x[i] * x[j]) * scale_factor * np.cos(i * 0.4 + j * 0.8)
                coupling_sum += coupling / (1.0 + abs(x[i] - x[j])**2.5)
            result += 0.7 * coupling_sum
            
        # Multi-scale chaotic interaction with variable coupling strengths and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.35 * np.sin(i * 0.8) * np.cos(j * 1.2)
                phase_shift = 0.6 * np.sin(i * 1.0 + j * 0.5)
                chaotic_coupling = np.sin(x[i] * x[j] * 2.3 + phase_shift) * np.cos(x[i] + x[j] * 1.9)
                result += strength * chaotic_coupling * np.exp(-0.4 * (x[i]**2 + x[j]**2))
                
        # Enhanced fractal basin terms with variable depths, widths, and rotation
        for i in range(self.dim):
            basin_depth = 1.8 + 0.9 * np.sin(i * 1.5)
            basin_width = 1.2 + 0.7 * np.cos(i * 1.1)
            rotation_angle = 0.3 * np.sin(i * 0.6)
            rotated_x = x[i] * np.cos(rotation_angle) - 0.6 * np.sin(rotation_angle)
            basin_term = basin_depth * (rotated_x**2 - basin_width)**2
            result += 0.5 * basin_term * np.exp(-0.2 * abs(x[i]))
            
        # High-frequency chaotic modulation with fractal-like behavior and amplitude variation
        high_freq_mod = 0.0
        for i in range(self.dim):
            freq = 8.0 + 6.0 * np.sin(i * 0.5)
            amp_mod = 1.1 + 0.35 * np.cos(i * 0.9)
            mod_term = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4) * amp_mod
            high_freq_mod += mod_term
        result += 0.8 * high_freq_mod
        
        # Global fractal scaling term with dynamic multiplicative factors
        global_scale = 1.3 + 0.5 * np.sin(np.sum(x) * 0.7)
        result *= global_scale
        
        # Add structured noise with enhanced fractal characteristics and dynamic variance
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 14.0) * np.cos(x[i] * 8.0) * (0.04 + 0.025 * np.abs(x[i]) + 0.015 * np.sin(i * 0.6))
        result += 0.15 * noise
        
        # Add dynamic coupling between all dimensions with variable weights and phase
        full_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = 0.25 + 0.15 * np.sin(i * 0.4 + j * 0.8)
                    phase = 0.9 * np.cos(i * 0.7 - j * 0.5)
                    coupling = np.sin(x[i] * x[j] * 1.7 + phase) * weight
                    full_coupling += coupling
        result += 0.35 * full_coupling
        
        # Add a global harmonic term to increase the number of local minima
        global_harmonic = np.sum(np.sin(2.5 * x) * np.cos(1.8 * x))
        result += 0.6 * global_harmonic
        
        return result