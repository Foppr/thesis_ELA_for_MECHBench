import numpy as np

class ChaoticAngularBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial with chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Chaotic sine-wave radial component
            for i in range(1, min(5, self.dim + 1)):
                freq = 2.0 * i + 0.5 * np.sin(r / 3.0)
                result += np.sin(freq * r) * np.cos(freq * r) * np.exp(-r/4.0) * (1.0 + 0.3 * np.sin(7.0 * r))
        
        # Dynamic angular coupling with chaotic scaling
        for i in range(self.dim):
            xi = x[i]
            angle_sum = 0.0
            for j in range(i+1, self.dim):
                xj = x[j]
                angle_diff = np.arctan2(xj, xi)
                # Chaotic angular coupling with dynamic scaling
                scale = 1.0 + 0.4 * np.sin(3.0 * angle_diff) * np.cos(5.0 * angle_diff)
                coupling = np.exp(-((xi - xj)**2)/2.0) * np.sin(xi + xj) * np.cos(xi - xj)
                angle_sum += scale * coupling
            result += angle_sum
        
        # Fractal-like radial polynomial with chaotic modulation
        for i in range(1, 6):
            poly = x[0]**(2*i) if self.dim > 0 else 0.0
            for j in range(1, min(i+1, self.dim)):
                poly *= (x[j]**2 + 0.5 * np.sin(x[j]))
            result += 0.5 * poly * np.exp(-r/3.0) * (1.0 + 0.2 * np.cos(11.0 * r))
        
        # Multi-scale chaotic sine terms with angular modulation
        for i in range(1, 8):
            freq = i * (1.0 + 0.3 * np.sin(r / 2.0))
            amp = 1.0 + 0.5 * np.cos(i * r / 4.0)
            phase = 0.5 * np.sin(i * r / 3.0)
            result += amp * np.sin(freq * r + phase) * np.cos(freq * r + phase) * np.exp(-r/5.0)
        
        # Chaotic cross-dimensional exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                exp_term = np.exp(-(xi**2 + xj**2)/3.0)
                chaotic_mod = 1.0 + 0.3 * np.sin(4.0 * (xi + xj)) * np.cos(6.0 * (xi - xj))
                result += exp_term * chaotic_mod
        
        # Angular harmonic with dynamic frequency
        for i in range(self.dim):
            xi = x[i]
            freq = 2.0 + 0.7 * np.sin(xi / 2.0)
            result += np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-abs(xi)/3.0)
        
        # Fractal scaling with chaotic sine coupling
        for i in range(self.dim):
            xi = x[i]
            fractal_scale = 1.0 + 0.2 * np.sin(9.0 * xi) * np.cos(11.0 * xi)
            result += fractal_scale * xi**5 * np.exp(-abs(xi)/4.0)
        
        # High-order chaotic polynomial with radial coupling
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_sum += xi**8 - 4*xi**6 + 6*xi**4 - 4*xi**2 + 1
        result += 0.7 * poly_sum * np.exp(-r/5.0) * (1.0 + 0.3 * np.sin(8.0 * r))
        
        # Additional chaotic angular terms with exponential weighting
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    xj = x[j]
                    chaotic_term = np.sin(5.0 * (xi + xj)) * np.cos(7.0 * (xi - xj))
                    result += 0.4 * chaotic_term * np.exp(-abs(xi-xj)/2.5)
        
        return result