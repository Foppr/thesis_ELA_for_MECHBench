import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # High-order polynomial radial term with trigonometric modulation
            poly_radial = r**6 - 5*r**4 + 10*r**2 - 1
            trig_mod = np.sin(3.0 * r) * np.cos(2.0 * r)
            result += poly_radial * trig_mod * np.exp(-r/4.0)
        
        # Cross-dimensional trigonometric coupling with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                # Angular distance based weighting
                angle_dist = np.arccos(np.clip((xi * xj) / (np.sqrt(xi**2 + 1e-8) * np.sqrt(xj**2 + 1e-8)), -1.0, 1.0))
                coupling = np.sin(xi + xj) * np.cos(xi - xj)
                weight = 1.0 + 0.3 * np.sin(angle_dist)
                result += weight * coupling
        
        # Adaptive polynomial modulation with exponential decay
        for i in range(self.dim):
            xi = x[i]
            poly_mod = xi**5 - 2*xi**3 + xi
            exp_decay = np.exp(-abs(xi)/3.0)
            adaptive_factor = 1.0 + 0.4 * np.sin(xi / 2.0) * np.cos(xi / 3.0)
            result += adaptive_factor * poly_mod * exp_decay
        
        # Multi-scale sinusoidal terms with radial dependence
        for i in range(1, 6):
            freq = i * (2.0 + 0.5 * np.sin(r / 3.0))
            amp = 1.0 + 0.5 * np.cos(i * r / 4.0)
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0)
        
        # Enhanced cross-dimensional exponential coupling with angular modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_coupling = np.exp(-((xi - xj)**2)/6.0)
                angle_mod = np.sin(xi + xj) * np.cos(xi - xj)
                result += 0.8 * exp_coupling * angle_mod
        
        # Spherical harmonic approximation with dynamic scaling
        if self.dim >= 2:
            theta = np.arctan2(x[1], x[0])
            phi = np.arccos(x[2] / (r + 1e-8)) if self.dim >= 3 else 0.0
            sph_harm = np.sin(2 * theta) * np.cos(2 * phi) + np.cos(3 * theta) * np.sin(3 * phi)
            result += 0.6 * sph_harm * np.exp(-r/2.0)
        
        # Sharp fitness transition regions with piecewise polynomial
        for i in range(self.dim):
            xi = x[i]
            if abs(xi) < 1.0:
                result += 0.5 * (xi**4 - 2*xi**2 + 1) * np.exp(-abs(xi)/2.0)
            else:
                result += 0.3 * (xi**3 - xi) * np.exp(-abs(xi)/3.0)
        
        # Dynamic scaling factor based on radial distance
        dynamic_scale = 1.0 + 0.7 * np.sin(r / 4.0) * np.cos(r / 6.0)
        result *= dynamic_scale
        
        return result