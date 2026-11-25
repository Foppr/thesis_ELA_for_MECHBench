import numpy as np

class ExponentialTrigonometricFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors and trigonometric coupling coefficients
        self.fractal_factors = np.array([0.5 + 0.5 * np.sin(i * np.pi / dim) for i in range(dim)])
        self.trig_coeffs = np.array([1.0 + 0.3 * np.cos(i * np.pi / (dim + 1)) for i in range(dim)])
        # Precompute exponential basis centers and scales
        self.centers = np.random.uniform(-1, 1, dim)
        self.scales = np.random.uniform(0.3, 1.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential radial basis component with multi-scale influence
        exp_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            exp_sum += np.exp(-dist / (2 * self.scales[i]**2)) * np.cos(3 * x_norm[i])
        
        # Trigonometric coupling component with varying frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(i * np.pi / (dim + 1))
            trig_sum += self.trig_coeffs[i] * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Fractal-inspired self-similarity component with nested structures
        fractal_sum = 0.0
        for i in range(self.dim):
            scale_factor = self.fractal_factors[i]
            # Nested sinusoidal patterns at different scales
            pattern = 0.0
            for k in range(1, 6):
                pattern += np.sin(k * x_norm[i] * scale_factor) / k
            fractal_sum += pattern * np.exp(-0.5 * x_norm[i]**2)
        
        # Multi-modal harmonic component with frequency modulation
        harm_sum = 0.0
        for i in range(self.dim):
            mod_freq = 1 + 0.5 * np.sin(i * np.pi / self.dim)
            harm_sum += np.sin(mod_freq * x_norm[i]) * np.cos(2 * mod_freq * x_norm[i])
        
        # Nested basin structure with exponential potential wells
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (np.exp(-x_norm[i]**2) - 0.5 * np.exp(-0.5 * x_norm[i]**2)) * np.cos(2 * x_norm[i])
            else:
                basin_sum += (np.exp(-0.5 * x_norm[i]**2) - 0.3 * np.exp(-x_norm[i]**2)) * np.sin(1.5 * x_norm[i])
        
        # Combined landscape with adaptive scaling
        result = 0.2 * exp_sum + 0.25 * trig_sum + 0.2 * fractal_sum + 0.2 * harm_sum + 0.15 * basin_sum
        
        # Conditioning factor based on dimensionality and input magnitude
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x_norm[i]) + 0.1 * x_norm[i]**3 + 0.05 * np.cos(4 * x_norm[i]))
        
        # Final transformation with global scaling and noise modulation
        noise = 0.03 * np.sum(np.cos(x_norm * 5))
        return result * condition_factor + noise + 0.08 * np.sum(np.abs(x_norm)**7)