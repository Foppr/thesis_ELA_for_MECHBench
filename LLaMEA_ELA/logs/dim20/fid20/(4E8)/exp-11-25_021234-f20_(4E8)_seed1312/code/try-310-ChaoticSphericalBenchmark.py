import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.sph_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics component with enhanced nonlinearity
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with parameter modulation and higher sensitivity
            a = 1.8 + 0.4 * np.sin(0.25 * i)
            xi = x[i] if x[i] < 0.5 else 1.0 - x[i]
            f1 += a * xi * np.exp(-0.12 * x[i]**2) + 0.1 * np.sin(5 * x[i])
            
        # Spherical harmonic terms with adaptive degrees and improved conditioning
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            degree = 3 + int(2 * np.sin(0.3 * i + r))
            coeff = self.sph_coeffs[i, degree % 5]
            # Improved spherical harmonic approximation with better distribution
            f2 += coeff * np.cos(degree * np.arctan2(x[i], r)) * np.exp(-0.07 * x[i]**2)
            
        # Cross-dimensional gradient modulation with enhanced coupling
        f3 = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.3 * np.sin(0.4 * i + r)
            grad_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = x[i] - x[j]
                    grad_mod += diff / (1.0 + np.abs(diff) + 0.1 * diff**2)
            f3 += weight * grad_mod**2
            
        # Dynamic conditioning with time-varying scaling and improved convergence
        f4 = 0.0
        t = 0.15 * np.sum(x**2)
        for i in range(self.dim):
            scale = 1.0 + 0.6 * np.sin(t + 0.3 * i)
            f4 += scale * x[i]**4 * np.exp(-0.1 * x[i]**2)
            
        # Fractal-like self-similarity with recursive tent mappings and improved structure
        f5 = 0.0
        for i in range(self.dim):
            # Recursive application of tent map with modified parameters
            xi = x[i]
            for _ in range(4):
                xi = 2.0 * xi if xi < 0.5 else 2.0 * (1.0 - xi)
            f5 += np.cos(xi) * np.exp(-0.12 * x[i]**2)
            
        # Boundary repulsion with logarithmic penalty and improved scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.4:
                dist = np.abs(x[i]) - 4.4
                f6 += 2.5 * np.log(1.0 + dist) * np.exp(-0.18 * dist)
                
        # Multi-scale chaotic oscillations with better frequency distribution
        f7 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.5 * np.sin(0.35 * i)
            amp = 1.2 + 0.3 * np.cos(0.25 * i)
            f7 += amp * np.cos(freq * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Adaptive coupling with phase shifts and improved interaction strength
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.3 * i + r)
            for j in range(i+1, self.dim):
                strength = 0.9 + 0.3 * np.cos(0.25 * (i + j) + r)
                interaction = np.cos(x[i] + x[j] + phase_shift)
                f8 += strength * interaction * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8