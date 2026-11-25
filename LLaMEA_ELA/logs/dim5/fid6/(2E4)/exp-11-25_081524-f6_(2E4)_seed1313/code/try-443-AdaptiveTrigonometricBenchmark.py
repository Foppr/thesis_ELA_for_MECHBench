import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial polynomial landscape with adaptive exponents
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            # Adaptive exponent based on radial distance
            adaptive_exp = 2.0 + 1.5 * np.sin(r / 3.0)
            result += (r**adaptive_exp) * np.exp(-r**2 / 20.0)
        
        # Cross-dimensional trigonometric coupling with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            trig_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    xj = x[j]
                    # Frequency modulation based on both variables
                    freq = 1.0 + 0.5 * np.sin(xi) * np.cos(xj)
                    trig_sum += np.sin(freq * xi + xj) * np.cos(freq * xj + xi)
            result += 0.3 * trig_sum * np.exp(-abs(xi) / 4.0)
        
        # Multi-scale sinusoidal modulation with adaptive amplitudes
        for scale in [1, 2, 3]:
            scale_factor = 1.0 / (scale ** 1.5)
            freq = scale * (1.0 + 0.3 * np.cos(r / 2.0))
            multi_scale_term = np.sin(freq * r) * np.cos(freq * r)
            result += scale_factor * multi_scale_term * np.exp(-r**2 / (15.0 * scale))
        
        # Polynomial perturbations with saddle-point characteristics
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Quintic polynomial with alternating signs to create multiple extrema
            poly_term = xi**5 - 15*xi**3 + 50*xi
            poly_sum += poly_term * np.exp(-abs(xi) / 2.0)
        result += 0.5 * poly_sum
        
        # Adaptive noise component with radial dependency
        noise_amp = 0.1 * (1.0 + 0.5 * np.sin(r))
        noise = np.random.normal(0, noise_amp, self.dim)
        noise_component = np.sum(noise**2) * np.exp(-r**2 / 30.0)
        result += noise_component
        
        # Angular coupling with exponential weighting
        angular_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            angular_term = np.sin(2.0 * xi) * np.cos(3.0 * xi) + 0.5 * np.sin(xi)
            angular_sum += angular_term * np.exp(-xi**2 / 10.0)
        result += 0.4 * angular_sum
        
        # Final normalization
        result = result / (1.0 + 0.05 * r**2)
        
        # Add improved fitness shaping component
        if r < 1.0:
            result *= (1.0 + 0.3 * np.sin(5.0 * r))
        
        return result