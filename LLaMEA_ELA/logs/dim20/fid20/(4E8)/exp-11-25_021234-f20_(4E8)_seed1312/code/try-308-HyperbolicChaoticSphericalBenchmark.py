import numpy as np

class HyperbolicChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.sph_coeffs = np.random.uniform(-1.0, 1.0, (dim, 7))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent chaotic dynamics component
        f1 = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent with parameter modulation
            a = 2.0 + 0.5 * np.sin(0.3 * i)
            xi = np.tanh(x[i])
            f1 += a * xi * np.exp(-0.1 * x[i]**2)
            
        # Modified spherical harmonic terms with radial coupling
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            degree = 3 + int(4 * np.sin(0.4 * i + r))
            coeff = self.sph_coeffs[i, degree % 7]
            # Modified spherical harmonic approximation with radial coupling
            f2 += coeff * np.tanh(degree * np.arctan2(x[i], r)) * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional gradient modulation with adaptive weights
        f3 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.7 * np.sin(0.5 * i + r)
            grad_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_mod += (x[i] - x[j]) / (1.0 + np.abs(x[i] - x[j]))
            f3 += weight * grad_mod**2
            
        # Dynamic conditioning with time-varying scaling
        f4 = 0.0
        t = 0.15 * np.sum(x**2)
        for i in range(self.dim):
            scale = 1.0 + 0.8 * np.sin(t + 0.4 * i)
            f4 += scale * x[i]**4 * np.exp(-0.1 * x[i]**2)
            
        # Fractal-like self-similarity with recursive hyperbolic tangent mappings
        f5 = 0.0
        for i in range(self.dim):
            # Recursive application of hyperbolic tangent map
            xi = x[i]
            for _ in range(4):
                xi = np.tanh(2.0 * xi)
            f5 += np.sinh(xi) * np.exp(-0.1 * x[i]**2)
            
        # Boundary repulsion with logarithmic penalty
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                dist = np.abs(x[i]) - 4.5
                f6 += 4.0 * np.log(1.0 + dist) * np.exp(-0.2 * dist)
                
        # Multi-scale chaotic oscillations with hyperbolic modulation
        f7 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.8 * np.cos(0.4 * i)
            f7 += amp * np.tanh(freq * x[i]) * np.exp(-0.25 * x[i]**2)
            
        # Adaptive coupling with phase shifts and hyperbolic interaction
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.4 * i + r)
            for j in range(i+1, self.dim):
                strength = 1.0 + 0.5 * np.cos(0.3 * (i + j) + r)
                interaction = np.tanh(x[i] + x[j] + phase_shift)
                f8 += strength * interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8