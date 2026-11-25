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
            # Spherical harmonics on the unit sphere
            for i in range(1, min(4, self.dim + 1)):
                for j in range(-i, i+1):
                    # Simplified spherical harmonic approximation
                    theta = np.arctan2(x[0], x[1]) if self.dim >= 2 else 0.0
                    phi = np.arccos(x[2] / r) if self.dim >= 3 else 0.0
                    result += (0.5 + 0.3 * np.sin(i * theta + j * phi)) * np.exp(-r/4.0)
        
        # Polynomial modulation with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 3*xi**4 + 3*xi**2 - 1
            scale_factor = 1.0 + 0.5 * np.sin(xi / 2.0)
            result += scale_factor * poly_term * np.exp(-abs(xi)/3.0)
        
        # Cross-dimensional coupling with adaptive weights based on angular distance
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                angle_diff = np.arccos(np.clip((xi * xj) / (np.sqrt(xi**2 + 1e-8) * np.sqrt(xj**2 + 1e-8)), -1.0, 1.0))
                weight = 0.7 + 0.3 * np.cos(angle_diff)
                coupling = np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/5.0)
                result += weight * coupling
        
        # Multi-scale radial sinusoidal terms with polynomial modulation
        for i in range(1, 6):
            freq = i * (1.0 + 0.2 * np.cos(r / 3.0))
            amp = 0.8 * (1.0 + 0.2 * np.sin(i * r / 4.0))
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        # Adaptive polynomial terms with angular modulation
        for i in range(self.dim):
            xi = x[i]
            angle_mod = 1.0 + 0.3 * np.sin(xi / 2.0)
            poly_mod = xi**5 - 2*xi**3 + xi
            result += angle_mod * poly_mod * np.exp(-abs(xi)/4.0)
        
        # Dynamic scaling based on radial distance
        dynamic_factor = 1.0 + 0.4 * np.cos(r / 2.0)
        result *= dynamic_factor
        
        # Cross-dimensional exponential coupling with harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-(xi**2 + xj**2)/6.0)
                harmonic_coupling = np.sin(2.0 * (xi + xj)) * np.cos(3.0 * (xi - xj))
                result += 0.5 * exp_coupling * harmonic_coupling
        
        # Spherical polynomial with radial modulation
        for i in range(self.dim):
            xi = x[i]
            poly = xi**4 - 2*xi**2 + 1
            result += 0.6 * poly * np.sin(xi) * np.exp(-abs(xi)/5.0)
            
        return result