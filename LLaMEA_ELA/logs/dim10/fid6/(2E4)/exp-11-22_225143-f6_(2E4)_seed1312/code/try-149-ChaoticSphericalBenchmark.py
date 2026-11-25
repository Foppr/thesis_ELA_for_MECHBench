import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters
        self.logistic_r = np.random.uniform(3.57, 4.0, dim)
        self.logistic_x0 = np.random.uniform(0.1, 0.9, dim)
        # Spherical harmonics coefficients
        self.sph_harm_l = np.random.randint(1, 6, dim)
        self.sph_harm_m = np.random.randint(-5, 6, dim)
        # Adaptive conditioning exponents
        self.conditioning_exponents = np.random.uniform(1.0, 8.0, dim)
        # Multi-scale noise parameters
        self.noise_scales = np.logspace(-3, 0, 10)
        self.noise_amplitudes = np.random.uniform(0.5, 2.0, 10)
        # Basin interaction centers
        self.basin_centers = np.random.uniform(-4.0, 4.0, (15, dim))
        self.basin_strengths = np.random.uniform(0.5, 3.0, 15)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic logistic map components
        for i in range(self.dim):
            x_log = self.logistic_x0[i]
            for _ in range(20):  # Iterate to reach chaotic regime
                x_log = self.logistic_r[i] * x_log * (1 - x_log)
            f_val += np.sin(x_log * np.pi) * np.cos(x_log * np.pi) * \
                     np.exp(-x_norm[i]**2 / 2.0) * (1.0 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Spherical harmonics components
        for i in range(self.dim):
            theta = np.arccos(x_norm[i])
            phi = np.arctan2(x_norm[(i+1)%self.dim], x_norm[i])
            f_val += (self.sph_harm_l[i] * self.sph_harm_m[i]) * \
                     np.sin(self.sph_harm_l[i] * theta) * np.cos(self.sph_harm_m[i] * phi) * \
                     np.exp(-x_norm[i]**2)
        
        # Adaptive conditioning
        for i in range(self.dim):
            f_val += self.conditioning_exponents[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.cos(3 * x_norm[i]))
        
        # Basin interaction terms
        for i in range(15):
            dist = np.sum((x_norm - self.basin_centers[i])**2)
            f_val += self.basin_strengths[i] * np.exp(-dist / (2 * 0.5**2)) * \
                     np.sin(dist) * np.cos(dist) * \
                     (1.0 + 0.1 * np.sin(4 * dist))
        
        # Multi-scale noise perturbations
        for i, (scale, amp) in enumerate(zip(self.noise_scales, self.noise_amplitudes)):
            noise = np.sum(np.sin(x_norm / scale) * np.cos(x_norm / scale)) * amp
            f_val += noise
        
        # Global scaling and non-linearity
        f_val *= (1.0 + 0.5 * np.sum(np.sin(x_norm)**3))
        
        return f_val