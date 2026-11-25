import numpy as np

class HyperChaoticLegendreBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Legendre polynomial coefficients
        self.legendre_coeffs = np.random.uniform(-1.0, 1.0, (dim, 7))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic tent map dynamics with multiple parameters
        f1 = 0.0
        for i in range(self.dim):
            # Multiple chaotic maps combined
            a1 = 1.7 + 0.2 * np.sin(0.3 * i)
            a2 = 1.3 + 0.4 * np.cos(0.2 * i)
            xi = x[i] if x[i] < 0.5 else 1.0 - x[i]
            f1 += (a1 * xi + a2 * (1.0 - xi)) * np.exp(-0.1 * x[i]**2)
            
        # Legendre polynomial terms with adaptive degrees
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            degree = 3 + int(4 * np.sin(0.4 * i + r) * np.cos(0.3 * i))
            coeff = self.legendre_coeffs[i, degree % 7]
            # Legendre polynomial approximation
            f2 += coeff * np.polynomial.legendre.legval(x[i], [0]*degree + [1]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional spectral coupling with adaptive weights
        f3 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.6 * np.sin(0.5 * i + r)
            spectral_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    spectral_mod += (x[i] - x[j]) / (1.0 + np.abs(x[i] - x[j]))
            f3 += weight * spectral_mod**2
            
        # Dynamic conditioning with multi-scale scaling factors
        f4 = 0.0
        t = 0.15 * np.sum(x**2)
        for i in range(self.dim):
            scale1 = 1.0 + 0.8 * np.sin(t + 0.4 * i)
            scale2 = 1.0 + 0.6 * np.cos(t + 0.3 * i)
            f4 += scale1 * scale2 * x[i]**4 * np.exp(-0.1 * x[i]**2)
            
        # Fractal-like self-similarity with recursive hyperchaotic mappings
        f5 = 0.0
        for i in range(self.dim):
            # Recursive application of hyperchaotic map
            xi = x[i]
            for _ in range(4):
                if xi < 0.25:
                    xi = 4.0 * xi
                elif xi < 0.5:
                    xi = 4.0 * (0.5 - xi)
                elif xi < 0.75:
                    xi = 4.0 * (xi - 0.5)
                else:
                    xi = 4.0 * (1.0 - xi)
            f5 += np.sin(xi) * np.exp(-0.1 * x[i]**2)
            
        # Boundary repulsion with exponential penalty
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.7:
                dist = np.abs(x[i]) - 4.7
                f6 += 5.0 * np.exp(dist) * np.exp(-0.2 * dist)
                
        # Multi-scale chaotic oscillations with spectral filtering
        f7 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.8 * np.cos(0.4 * i)
            f7 += amp * np.sin(freq * x[i]) * np.exp(-0.25 * x[i]**2)
            
        # Adaptive coupling with phase shifts and spectral weights
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.4 * i + r)
            for j in range(i+1, self.dim):
                strength = 1.0 + 0.5 * np.cos(0.3 * (i + j) + r)
                interaction = np.sin(x[i] + x[j] + phase_shift)
                f8 += strength * interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8