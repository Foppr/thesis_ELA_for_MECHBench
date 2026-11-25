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
        
        # Additional high-frequency trigonometric coupling terms
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    xj = x[j]
                    freq_term = np.sin(5.0 * (xi + xj)) * np.cos(7.0 * (xi - xj))
                    result += 0.3 * freq_term * np.exp(-abs(xi-xj)/3.0)
        
        # Novel angular harmonic components with higher-order modulation
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                angle = np.arctan2(xj, xi)
                angular_mod = 0.6 + 0.4 * np.cos(5*angle) * np.sin(3*angle)
                result += angular_mod * np.exp(-((xi-xj)**2)/6.0) * np.sin(4*(xi+xj))
        
        # Enhanced multi-scale radial terms with complex modulation
        for i in range(1, 10):
            freq = i * (2.0 + 0.5 * np.sin(r / 3.0))
            amp = 1.2 + 0.3 * np.cos(i * r / 4.0) * np.sin(i * r / 5.0)
            result += amp * np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/5.0) * (1.0 + 0.2 * np.sin(r))
        
        # Additional cross-dimensional coupling with fractal-like behavior - Modified parameters
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                fractal_factor = 1.0 + 0.4 * np.sin(15 * (xi**2 + xj**2))  # Increased frequency
                result += fractal_factor * np.exp(-abs(xi-xj)/3.5) * np.cos(8*(xi+xj)) * np.sin(10*(xi-xj))  # Modified frequencies
        
        # High-order polynomial with exponential weighting and angular coupling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += xi**9 - 5*xi**7 + 10*xi**5 - 10*xi**3 + 5*xi
        result += 0.9 * poly_sum * np.exp(-r/6.0)
        
        # Final angular coupling with dynamic scaling
        angle_sum = 0.0
        for i in range(self.dim):
            angle_sum += np.sin(x[i] / 2.0) * np.cos(x[i] / 3.0)
        result += 0.5 * angle_sum * np.exp(-r/7.0)
        
        # Additional fractal-like coupling with increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                # Increased frequency and amplitude for more complex fractal behavior
                fractal_term = np.sin(25 * (xi**2 + xj**2)) * np.cos(20 * (xi - xj))
                result += 0.6 * fractal_term * np.exp(-abs(xi-xj)/4.0) * (1.0 + 0.3 * np.sin(xi+xj))
        
        # Enhanced radial exponential with multiple harmonic components
        for i in range(1, 12):
            freq = i * (2.5 + 0.4 * np.cos(r / 4.0))
            amp = 1.5 + 0.5 * np.sin(i * r / 5.0) * np.cos(i * r / 6.0)
            result += amp * np.exp(-r/8.0) * np.sin(freq * r) * np.cos(freq * r)
        
        # Additional high-order trigonometric coupling with angular dependence
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                if j < self.dim:
                    xj = x[j]
                    # Increased complexity in coupling terms
                    coupling = np.sin(7*(xi+xj)) * np.cos(9*(xi-xj)) * np.exp(-((xi-xj)**2)/7.0)
                    result += 0.4 * coupling * (1.0 + 0.25 * np.sin(xi) * np.cos(xj))
        
        # Multi-scale exponential terms with adaptive modulation
        for i in range(1, 15):
            scale = 1.0 + 0.3 * np.sin(i * r / 3.0)
            result += scale * np.exp(-i * r / 10.0) * np.sin(i * r) * np.cos(i * r / 2.0)
        
        # Additional cross-dimensional interaction with complex angular modulation
        for i in range(self.dim):
            xi = x[i]
            angle_mod = 1.0 + 0.4 * np.sin(xi / 3.0) * np.cos(xi / 5.0)
            result += angle_mod * (xi**5 - 2*xi**3 + xi) * np.exp(-abs(xi)/5.0)
        
        # Final enhanced dynamic scaling with multi-dimensional angular dependence
        total_angle = 0.0
        for i in range(self.dim):
            total_angle += np.arctan2(x[i], 1.0)
        final_scale = 1.0 + 0.3 * np.sin(total_angle) * np.cos(total_angle / 2.0)
        result *= final_scale
        
        return result