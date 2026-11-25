import numpy as np

class FractalGradientHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Fractal noise parameters
        self.fractal_octaves = 4
        self.fractal_gain = 0.5
        self.fractal_scale = 1.0
        
        # Adaptive gradient steepness parameters
        self.steepness_factors = np.random.uniform(1.0, 5.0, dim)
        
        # Spherical harmonic coefficients for angular complexity
        self.sph_harm_coeffs = np.random.randn(dim, 6, 6)
        
        # Multiple overlapping local minima with varying depths
        self.minima_centers = np.random.uniform(-5.0, 5.0, (12, dim))
        self.minima_depths = np.random.uniform(0.5, 2.0, 12)
        
        # Periodic modulation for increased complexity
        self.modulation_freqs = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Normalize to [-1, 1] range for internal computations
        x_norm = x / 5.0
        
        # Generate fractal noise component
        fractal_noise = 0.0
        for i in range(self.dim):
            pos = x_norm[i]
            octave_sum = 0.0
            for octave in range(self.fractal_octaves):
                freq = 2 ** octave
                amp = self.fractal_gain ** octave
                octave_sum += amp * np.sin(freq * pos * np.pi)
            fractal_noise += octave_sum
        
        # Adaptive gradient steepness component
        grad_steepness = 0.0
        for i in range(self.dim):
            grad_steepness += self.steepness_factors[i] * (x_norm[i] ** 3)
        
        # Spherical harmonics component
        sph_harm = 0.0
        for i in range(self.dim):
            theta = np.arctan2(x_norm[i], 1.0) if i < self.dim - 1 else 0.0
            phi = np.arctan2(np.sqrt(x_norm[i]**2 + x_norm[i+1]**2), x_norm[i]) if i < self.dim - 1 else 0.0
            
            for l in range(6):
                for m in range(-l, l+1):
                    sph_harm += self.sph_harm_coeffs[i, l, abs(m)] * np.sin(l * theta) * np.cos(m * phi)
        
        # Multiple local minima attraction
        minima_attraction = 0.0
        for j in range(12):
            dist = np.linalg.norm(x_norm - self.minima_centers[j] / 5.0)
            minima_attraction += self.minima_depths[j] * np.exp(-dist**2 / 0.5)
        
        # Periodic modulation component
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += np.sin(self.modulation_freqs[i] * x_norm[i] * np.pi) * np.cos(self.modulation_freqs[i] * x_norm[i] * np.pi)
        
        # Combine all components with dynamic weights
        result = 0.3 * fractal_noise + 0.25 * grad_steepness + 0.2 * sph_harm + 0.15 * minima_attraction + 0.1 * periodic_mod
        
        # Apply sigmoid transformation to create non-convexity and plateaus
        result = 1.0 / (1.0 + np.exp(-result)) - 0.5
        
        # Add final chaotic scaling based on all dimensions
        chaos_scale = 1.0 + 0.2 * np.sin(np.sum(x_norm) * np.pi)
        
        return result * chaos_scale