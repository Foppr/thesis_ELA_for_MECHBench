import numpy as np

class QuaternionSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential radial potentials with adaptive scaling and quaternion-like structure
        r = np.sqrt(np.sum(x**2))
        f1 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
            f1 += scale * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * r))**2) * (1.0 + 0.4 * np.cos(0.3 * i + 0.1 * r))
            
        # Quaternion-inspired cross-dimensional coupling with imaginary unit emulation
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Emulate quaternion multiplication structure
                coupling = 0.6 + 0.4 * np.sin(0.4 * (i - j) + 0.3 * r)
                f2 += coupling * (x[i] * x[j] + x[i]**2 * x[j]**2) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                
        # Dynamic spherical harmonics with multi-scale angular modulation
        f3 = 0.0
        for i in range(self.dim):
            theta = np.arctan2(x[i], x[(i+1) % self.dim]) if self.dim > 1 else 0.0
            phi = np.arccos(x[i] / (r + 1e-8)) if r > 0 else 0.0
            freq_theta = 2.0 + 3.0 * np.sin(0.3 * i)
            freq_phi = 1.5 + 2.0 * np.cos(0.2 * i)
            f3 += np.sin(freq_theta * theta) * np.cos(freq_phi * phi) * np.exp(-0.03 * x[i]**2)
            
        # Adaptive boundary conditioning with logarithmic penalty and exponential scaling
        f4 = 0.0
        for i in range(self.dim):
            dist_to_bound = min(5.0 - x[i], 5.0 + x[i])
            if dist_to_bound < 1.0:
                penalty = 3.0 * np.exp(-dist_to_bound**2 / 0.5) + 0.8 * np.log(1.0 + dist_to_bound)
            else:
                penalty = 0.0
            f4 += penalty
            
        # Stochastic coupling with dynamic phase shifts and chaotic interaction strengths
        f5 = 0.0
        for i in range(self.dim):
            phase_shift = 0.2 * np.sin(0.3 * i + 0.1 * r) + np.random.uniform(-0.1, 0.1)
            for j in range(i+1, self.dim):
                strength = 0.7 + 0.3 * np.cos(0.5 * (i + j) + 0.2 * r)
                f5 += strength * np.sin(x[i] + phase_shift) * np.cos(x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Polynomial chaos with fractional exponents and dynamic coefficients
        f6 = 0.0
        for i in range(self.dim):
            coeff1 = 0.5 + 0.5 * np.sin(0.4 * i)
            coeff2 = 0.3 + 0.7 * np.cos(0.3 * i)
            coeff3 = 0.8 + 0.2 * np.sin(0.5 * i)
            f6 += coeff1 * x[i]**(1.5) + coeff2 * x[i]**(2.5) + coeff3 * x[i]**(3.5)
            
        # Spherical symmetry breaking with cosine modulation and dynamic radius coupling
        f7 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.6 * np.cos(0.2 * i + 0.1 * r)
            f7 += mod * np.cos(x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Multi-scale fractal-like cross-terms with recursive structure
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 0.5 + 0.5 * np.sin(0.3 * (i + j) + 0.2 * r)
                f8 += scale * np.cos(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Combined chaotic oscillations with time-varying amplitude and frequency
        f9 = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.8 * np.sin(0.2 * i + 0.3 * r)
            freq = 1.0 + 2.0 * np.cos(0.4 * i)
            f9 += amp * np.sin(freq * x[i] + 0.2 * r) * np.exp(-0.05 * np.abs(x[i]))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9