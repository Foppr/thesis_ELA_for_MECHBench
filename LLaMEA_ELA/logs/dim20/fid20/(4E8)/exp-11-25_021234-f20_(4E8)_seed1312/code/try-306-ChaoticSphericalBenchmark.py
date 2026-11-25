import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.sph_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics component
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with parameter modulation
            a = 1.5 + 0.3 * np.sin(0.2 * i)
            xi = x[i] if x[i] < 0.5 else 1.0 - x[i]
            f1 += a * xi * np.exp(-0.1 * x[i]**2)
            
        # Spherical harmonic terms with adaptive degrees
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            degree = 2 + int(3 * np.sin(0.3 * i + r))
            coeff = self.sph_coeffs[i, degree % 5]
            # Simple spherical harmonic approximation
            f2 += coeff * np.sin(degree * np.arctan2(x[i], r)) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional gradient modulation with adaptive weights
        f3 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.4 * i + r)
            grad_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_mod += (x[i] - x[j]) / (1.0 + np.abs(x[i] - x[j]))
            f3 += weight * grad_mod**2
            
        # Dynamic conditioning with time-varying scaling
        f4 = 0.0
        t = 0.1 * np.sum(x**2)
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.sin(t + 0.3 * i)
            f4 += scale * x[i]**3 * np.exp(-0.08 * x[i]**2)
            
        # Fractal-like self-similarity with recursive tent mappings
        f5 = 0.0
        for i in range(self.dim):
            # Recursive application of tent map
            xi = x[i]
            for _ in range(3):
                xi = 2.0 * xi if xi < 0.5 else 2.0 * (1.0 - xi)
            f5 += np.sin(xi) * np.exp(-0.1 * x[i]**2)
            
        # Boundary repulsion with logarithmic penalty
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                dist = np.abs(x[i]) - 4.5
                f6 += 3.0 * np.log(1.0 + dist) * np.exp(-0.15 * dist)
                
        # Multi-scale chaotic oscillations
        f7 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f7 += amp * np.sin(freq * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Adaptive coupling with phase shifts
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.3 * i + r)
            for j in range(i+1, self.dim):
                strength = 0.8 + 0.4 * np.cos(0.2 * (i + j) + r)
                interaction = np.sin(x[i] + x[j] + phase_shift)
                f8 += strength * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8