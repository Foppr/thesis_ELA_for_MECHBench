import numpy as np

class SphericalHarmonicCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Spherical harmonic components with radial dependency
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Enhanced spherical harmonic approximation
            for i in range(1, min(5, self.dim + 1)):
                for j in range(-i, i+1):
                    theta = np.arctan2(x[0], x[1]) if self.dim >= 2 else 0.0
                    phi = np.arccos(x[2] / r) if self.dim >= 3 else 0.0
                    # Add angular frequency modulation and enhanced amplitude
                    freq_mod = 1.0 + 0.3 * np.sin(i * 0.5)
                    amp_mod = 0.6 + 0.4 * np.cos(j * 0.7)
                    result += amp_mod * np.sin(freq_mod * (i * theta + j * phi)) * np.exp(-r/3.0)
        
        # Enhanced polynomial modulation with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 3*xi**4 + 3*xi**2 - 1
            scale_factor = 1.0 + 0.6 * np.sin(xi / 2.0)
            result += scale_factor * poly_term * np.exp(-abs(xi)/2.5)
        
        # Improved cross-dimensional coupling with enhanced weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                angle_diff = np.arccos(np.clip((xi * xj) / (np.sqrt(xi**2 + 1e-8) * np.sqrt(xj**2 + 1e-8)), -1.0, 1.0))
                # Enhanced weight with dynamic angular modulation
                weight = 0.8 + 0.4 * np.cos(angle_diff * 1.5)
                coupling = np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/4.0)
                result += weight * coupling
        
        # Multi-scale radial sinusoidal terms with enhanced modulation
        for i in range(1, 7):
            freq = i * (1.2 + 0.3 * np.cos(r / 2.0))
            amp = 0.9 * (1.0 + 0.3 * np.sin(i * r / 3.0))
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/4.0)
        
        # Enhanced adaptive polynomial terms with angular modulation
        for i in range(self.dim):
            xi = x[i]
            angle_mod = 1.0 + 0.4 * np.sin(xi / 1.5)
            poly_mod = xi**5 - 2*xi**3 + xi
            result += angle_mod * poly_mod * np.exp(-abs(xi)/3.5)
        
        # Improved dynamic scaling based on radial distance
        dynamic_factor = 1.0 + 0.5 * np.cos(r / 1.5)
        result *= dynamic_factor
        
        # Enhanced cross-dimensional exponential coupling with harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-(xi**2 + xj**2)/5.0)
                harmonic_coupling = np.sin(3.0 * (xi + xj)) * np.cos(2.0 * (xi - xj))
                result += 0.6 * exp_coupling * harmonic_coupling
        
        # Enhanced spherical polynomial with radial modulation
        for i in range(self.dim):
            xi = x[i]
            poly = xi**4 - 2*xi**2 + 1
            result += 0.7 * poly * np.sin(xi) * np.exp(-abs(xi)/4.0)
            
        # Additional high-frequency oscillatory component for increased multimodality
        freq_factor = 10.0
        result += 0.3 * np.sin(freq_factor * r) * np.cos(freq_factor * r) * np.exp(-r/6.0)
        
        return result