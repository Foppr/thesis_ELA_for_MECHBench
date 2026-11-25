import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial exponential decay with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Spherical harmonics approximation with exponential weighting
            for i in range(1, min(6, self.dim + 1)):
                for j in range(-i, i+1):
                    theta = np.arctan2(x[0], x[1]) if self.dim >= 2 else 0.0
                    phi = np.arccos(x[2] / r) if self.dim >= 3 else 0.0
                    # Enhanced spherical harmonic with exponential decay
                    result += (0.8 + 0.2 * np.sin(i * theta + j * phi)) * np.exp(-r/3.0) * np.cos(i * r)
        
        # High-order polynomial modulation with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**8 - 4*xi**6 + 6*xi**4 - 4*xi**2 + 1
            scale_factor = 1.0 + 0.6 * np.sin(xi / 3.0) * np.cos(xi / 2.0)
            result += scale_factor * poly_term * np.exp(-abs(xi)/2.5)
        
        # Cross-dimensional exponential coupling with angular distance weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                angle_diff = np.arccos(np.clip((xi * xj) / (np.sqrt(xi**2 + 1e-8) * np.sqrt(xj**2 + 1e-8)), -1.0, 1.0))
                weight = 0.9 + 0.1 * np.cos(angle_diff)
                coupling = np.exp(-((xi - xj)**2)/4.0) * np.sin(xi + xj) * np.cos(xi - xj)
                result += weight * coupling
        
        # Multi-scale radial sinusoidal terms with enhanced polynomial modulation
        for i in range(1, 8):
            freq = i * (1.5 + 0.3 * np.sin(r / 2.0))
            amp = 1.0 + 0.4 * np.cos(i * r / 3.0)
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/4.0)
        
        # Adaptive polynomial terms with angular modulation and exponential weighting
        for i in range(self.dim):
            xi = x[i]
            angle_mod = 1.0 + 0.5 * np.sin(xi / 2.0) * np.cos(xi / 3.0)
            poly_mod = xi**7 - 3*xi**5 + 3*xi**3 - xi
            result += angle_mod * poly_mod * np.exp(-abs(xi)/3.5)
        
        # Dynamic scaling based on radial distance with trigonometric modulation
        dynamic_factor = 1.0 + 0.5 * np.cos(r / 2.0) * np.sin(r / 4.0)
        result *= dynamic_factor
        
        # Enhanced cross-dimensional exponential coupling with harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-(xi**2 + xj**2)/5.0) * np.sin(xi + xj)
                harmonic_coupling = np.cos(3.0 * (xi - xj)) * np.sin(2.0 * (xi + xj))
                result += 0.7 * exp_coupling * harmonic_coupling
        
        # Spherical polynomial with enhanced radial modulation and exponential weighting
        for i in range(self.dim):
            xi = x[i]
            poly = xi**6 - 3*xi**4 + 3*xi**2 - 1
            result += 0.8 * poly * np.sin(xi) * np.exp(-abs(xi)/4.0)
        
        # Additional high-frequency trigonometric coupling terms with modified weights
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    xj = x[j]
                    freq_term = np.sin(5.0 * (xi + xj)) * np.cos(7.0 * (xi - xj))
                    result += 0.4 * freq_term * np.exp(-abs(xi-xj)/3.0)
        
        # New: Additional harmonic component with modified frequency and amplitude
        for i in range(1, 6):
            freq = i * (2.0 + 0.2 * np.cos(r / 3.0))
            amp = 0.7 + 0.3 * np.sin(i * r / 4.0)
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        return result