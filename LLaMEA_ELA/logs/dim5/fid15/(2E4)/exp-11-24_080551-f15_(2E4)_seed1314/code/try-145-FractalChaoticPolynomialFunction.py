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
            poly_term = (x[i]**5 + 0.7*x[i]**4 + 0.6*x[i]**3 + 0.4*x[i]**2 + 0.2*x[i] + 0.1) * np.sin(i * 0.9)
            result += poly_term
            
        # Enhanced radial basis functions with multi-scale fractal centers and chaotic widths
        for i in range(self.dim):
            center = np.sin(i * 1.7) * 4.0 + 0.5 * np.cos(i * 1.1)
            width = 0.3 + 0.4 * np.cos(i * 1.2) + 0.1 * np.sin(i * 0.8)
            radial = np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            result += 1.2 * radial * (1.0 + 0.3 * np.sin(i * 2.5) * np.cos(i * 1.8))
            
        # Enhanced asymmetric harmonic oscillators with time-varying parameters
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(i * 1.0)
            damping = 0.4 + 0.3 * np.cos(i * 1.5)
            harm_term = np.sin(freq * x[i]) * np.exp(-damping * abs(x[i])) * (1.0 + 0.2 * np.sin(i * 0.6))
            result += 0.8 * harm_term
            
        # Cross-dimensional fractal coupling with recursive scaling and dynamic weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, self.dim):
                scale_factor = 0.6 + 0.4 * np.sin((i+j) * 0.5)
                coupling = np.sin(x[i] * x[j]) * scale_factor * np.cos(i * 0.3 + j * 0.7)
                coupling_sum += coupling / (1.0 + abs(x[i] - x[j])**2.0)
            result += 0.6 * coupling_sum
            
        # Multi-scale chaotic interaction with variable coupling strengths and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.4 + 0.3 * np.sin(i * 0.7) * np.cos(j * 1.1)
                phase_shift = 0.5 * np.sin(i * 0.9 + j * 0.4)
                chaotic_coupling = np.sin(x[i] * x[j] * 2.1 + phase_shift) * np.cos(x[i] + x[j] * 1.7)
                result += strength * chaotic_coupling * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                
        # Enhanced fractal basin terms with variable depths, widths, and rotation
        for i in range(self.dim):
            basin_depth = 1.5 + 0.8 * np.sin(i * 1.3)
            basin_width = 1.0 + 0.6 * np.cos(i * 0.9)
            rotation_angle = 0.2 * np.sin(i * 0.5)
            rotated_x = x[i] * np.cos(rotation_angle) - 0.5 * np.sin(rotation_angle)
            basin_term = basin_depth * (rotated_x**2 - basin_width)**2
            result += 0.4 * basin_term * np.exp(-0.15 * abs(x[i]))
            
        # High-frequency chaotic modulation with fractal-like behavior and amplitude variation
        high_freq_mod = 0.0
        for i in range(self.dim):
            freq = 7.0 + 5.0 * np.sin(i * 0.4)
            amp_mod = 1.0 + 0.3 * np.cos(i * 0.8)
            mod_term = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * amp_mod
            high_freq_mod += mod_term
        result += 0.7 * high_freq_mod
        
        # Global fractal scaling term with dynamic multiplicative factors
        global_scale = 1.2 + 0.4 * np.sin(np.sum(x) * 0.6)
        result *= global_scale
        
        # Add structured noise with enhanced fractal characteristics and dynamic variance
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * 12.0) * np.cos(x[i] * 7.0) * (0.03 + 0.02 * np.abs(x[i]) + 0.01 * np.sin(i * 0.5))
        result += 0.12 * noise
        
        # Add dynamic coupling between all dimensions with variable weights and phase
        full_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = 0.2 + 0.1 * np.sin(i * 0.3 + j * 0.7)
                    phase = 0.8 * np.cos(i * 0.6 - j * 0.4)
                    coupling = np.sin(x[i] * x[j] * 1.5 + phase) * weight
                    full_coupling += coupling
        result += 0.3 * full_coupling
        
        # Add a global harmonic term to increase the number of local minima
        global_harmonic = np.sum(np.sin(2.0 * x) * np.cos(1.5 * x))
        result += 0.5 * global_harmonic
        
        return result