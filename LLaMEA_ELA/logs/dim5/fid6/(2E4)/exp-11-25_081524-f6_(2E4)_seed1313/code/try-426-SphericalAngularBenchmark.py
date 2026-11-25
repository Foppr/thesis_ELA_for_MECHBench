import numpy as np

class SphericalAngularBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Spherical harmonic components with variable degree
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            for l in range(1, min(6, self.dim + 1)):
                m = l // 2
                theta = np.arctan2(np.sqrt(np.sum(x[:l]**2)), x[l-1]) if l < self.dim else np.arctan2(x[0], x[1])
                phi = np.arctan2(x[1], x[0]) if l == 2 else 0.0
                sph_harm = np.sin(l * theta) * np.cos(m * phi) * np.exp(-r**2 / 20.0)
                result += sph_harm * (l + 1.0) * np.sin(r / (l + 1.0))
        
        # Fractional polynomial scaling with oscillatory behavior
        for i in range(self.dim):
            xi = x[i]
            frac_poly = xi**(1.5 + 0.5 * np.sin(xi)) - 2*xi**(0.7 + 0.3 * np.cos(xi))
            result += frac_poly * np.exp(-abs(xi) / 8.0)
        
        # Complex angular coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                xi = x[i]
                xj = x[j]
                angle_coupling = np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj) / 5.0)
                adaptive_weight = 1.0 + 0.4 * np.sin(2*xi) * np.cos(3*xj) * np.sin(4*(xi+xj))
                result += adaptive_weight * angle_coupling
        
        # Multi-scale radial oscillations with varying amplitudes
        for k in range(1, 5):
            scale = 2.0**k
            freq = 0.5 + 0.3 * np.sin(r / (k+2.0))
            amp = 1.0 + 0.5 * np.cos(r / (k+1.0)) * np.sin(r / (k+3.0))
            result += amp * np.sin(freq * r / scale) * np.cos(freq * r / scale) * np.exp(-r**2 / (scale * 10.0))
        
        # Adaptive Gaussian peaks with varying widths and heights
        for i in range(1, min(8, self.dim + 1)):
            center = np.sin(i) * 3.0
            width = 0.5 + 0.3 * np.cos(i)
            height = 1.0 + 0.7 * np.sin(i)
            gaussian_peak = height * np.exp(-((x[0] - center)**2) / (2 * width**2))
            result += gaussian_peak
        
        # Fractional harmonic polynomial with radial modulation
        frac_harmonic = 0.0
        for i in range(self.dim):
            xi = x[i]
            frac_harmonic += (xi**(1.7 + 0.3 * np.sin(xi)) - 2*xi**(1.3 + 0.2 * np.cos(xi)))**2
        result += 0.5 * frac_harmonic * np.exp(-r / 15.0)
        
        # Cross-dimensional coupling with hyperbolic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                hyperbolic_coupling = np.sinh(xi + xj) * np.cosh(xi - xj)
                result += hyperbolic_coupling / (1.0 + abs(xi) + abs(xj))
        
        # Modified angular frequency components with exponential decay
        for i in range(self.dim):
            xi = x[i]
            freq_mod = 2.0 + 1.5 * np.sin(xi)
            result += np.sin(freq_mod * xi) * np.cos(freq_mod * xi) * np.exp(-abs(xi) / 6.0)
        
        # Additional high-frequency oscillatory term
        high_freq_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            high_freq_term += np.sin(10*xi) * np.cos(12*xi) * np.exp(-abs(xi) / 4.0)
        result += 0.3 * high_freq_term
        
        return result