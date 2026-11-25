import numpy as np

class QuaternionSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-based rotational dynamics with spectral filtering
        f1 = 0.0
        for i in range(self.dim):
            # Quaternion-like rotation with adaptive angle
            angle = 0.6 * x[i] + 0.3 * np.sin(0.4 * i)  # Slight change in coefficient
            rot_factor = np.cos(angle)**2 + np.sin(angle)**2
            f1 += rot_factor * np.sin(2.0 * x[i])**2 * np.exp(-0.1 * x[i]**2)
            
        # Adaptive spectral filtering with frequency modulation
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Frequency modulation based on radial distance and dimension
            freq_mod = 1.0 + 0.6 * np.sin(0.5 * i + 0.4 * r)  # Slight change in coefficient
            f2 += (x[i]**2 / (1.0 + 0.1 * r**2)) * np.cos(freq_mod * x[i])**2
            
        # Saddle-point harmonic interactions with multi-scale coupling
        f3 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Saddle-point coupling with harmonic interaction
                    coupling_strength = 1.0 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * r)  # Slight change in coefficient
                    saddle_interaction = coupling_strength * np.cos(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f3 += saddle_sum
            
        # Multi-scale harmonic resonances with complex phase relationships
        f4 = 0.0
        for i in range(self.dim):
            # Complex phase modulation based on position and dimension
            phase_mod = np.sin(0.6 * x[i] + 0.3 * i) + 0.4 * np.cos(0.5 * r)  # Slight change in coefficients
            f4 += np.sin(3.0 * x[i] + phase_mod)**2 * np.cos(2.0 * x[i] + phase_mod)**2
            
        # Boundary-sensitive potential with multi-exponential decay
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.5 * np.sin(0.7 * i)  # Slight change in coefficient
                f5 += boundary_factor * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.6 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with quaternion-based coefficients
        f6 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Quaternion-like coefficient based on position and dimension
                coeff = 1.0 + 0.5 * np.sin(0.4 * (i + j) + 0.3 * r)  # Slight change in coefficient
                interaction = x[i]**3 * x[j]**3
                poly_sum += coeff * interaction * np.exp(-0.04 * (x[i]**2 + x[j]**2))
            f6 += poly_sum
            
        # Fractal-like rotational structure with quaternion symmetry
        f7 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.8 * i + 0.5 * r)  # Slight change in coefficient
            f7 += scale_factor * np.cos(np.pi * x[i] / (1.0 + 0.3 * r))**3
            
        # Phase-shifted harmonic components with quaternion modulation
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.7 * i + 0.3 * r) + 0.2 * np.cos(0.5 * r)  # Slight change in coefficients
            freq_mod = 2.5 + 0.9 * np.sin(0.6 * i)  # Slight change in base frequency
            f8 += np.sin(freq_mod * x[i] + phase_shift)**4
            
        # Exponential radial conditioning with quaternion-based parameters
        f9 = 0.0
        for i in range(self.dim):
            # Quaternion-like parameter based on position and dimension
            adapt_param = 1.0 + 0.7 * np.sin(0.6 * i + 0.4 * r)  # Slight change in coefficient
            f9 += adapt_param * np.exp(-0.2 * x[i]**2) * np.sin(1.5 * x[i])**2  # Slight change in exponent
            
        # Enhanced rotational complexity with multi-dimensional coupling
        f10 = 0.0
        for i in range(self.dim):
            # Multi-scale rotational difficulty factor
            difficulty_factor = 1.0 + 0.8 * np.sin(0.9 * i + 0.6 * r)  # Slight change in coefficient
            f10 += difficulty_factor * np.cos(2.0 * x[i])**3
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10