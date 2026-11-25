import numpy as np

class ChaoticTentPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.tent_map = lambda x: 2 * x if x < 0.5 else 2 * (1 - x)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with dynamic scaling
        f1 = 0.0
        for i in range(self.dim):
            # Apply tent map to each dimension with dynamic scaling factor
            scale = 1.0 + 0.5 * np.sin(0.2 * i)
            chaotic_val = self.tent_map(x[i] / scale)
            f1 += chaotic_val**2
            
        # Radial polynomial potential with varying exponents
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            exp_factor = 2 + int(2 * np.cos(0.3 * i + 0.1 * r))
            f2 += x[i]**exp_factor
            
        # Dynamic sine-cosine coupling with time-varying phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.5 * np.sin(0.2 * (i + j) + 0.1 * r)
                coupling = np.sin(x[i] + x[j] + phase_shift) * np.cos(x[i] - x[j] + phase_shift)
                f3 += coupling * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary repulsion with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                f4 += dist**3 * np.exp(-0.2 * dist)
                
        # Multi-scale chaotic polynomial interactions
        f5 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.8 * np.sin(0.4 * i + 0.1 * r + np.pi/3)
            f5 += chaos_factor * x[i]**5 * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional tent map coupling
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                tent_coupling = self.tent_map(x[i]) * self.tent_map(x[j])
                f6 += tent_coupling * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Adaptive radial harmonic terms
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.5 * np.cos(0.2 * i + 0.1 * r)
            f7 += np.sin(freq * x[i]) * np.exp(-0.1 * r**2)
            
        # Hybrid chaotic polynomial with boundary influence
        f8 = 0.0
        for i in range(self.dim):
            boundary_factor = 1.0 + 0.3 * np.tanh(5.0 - np.abs(x[i]))
            f8 += boundary_factor * x[i]**4 * np.exp(-0.01 * x[i]**2)
            
        # Dynamic cross-dimensional coupling with chaotic weights
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.3 * (i - j) + 0.2 * r)
                chaotic_weight = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * j + 0.1 * r)
                f9 += weight * chaotic_weight * x[i] * x[j] * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Fractional polynomial with chaotic modulation
        f10 = 0.0
        for i in range(self.dim):
            frac_exp = 1.5 + 0.5 * np.sin(0.2 * i + 0.1 * r)
            f10 += x[i]**frac_exp * np.exp(-0.03 * x[i]**2)
            
        # Combined chaotic and harmonic terms
        f11 = 0.0
        for i in range(self.dim):
            chaos_harmonic = self.tent_map(x[i]) * np.sin(x[i])
            f11 += chaos_harmonic * np.exp(-0.05 * x[i]**2)
            
        # Dynamic radial coupling with chaotic scaling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                radial_weight = 1.0 + 0.6 * np.sin(0.3 * (i + j) + 0.1 * r)
                chaotic_scale = 1.0 + 0.5 * np.cos(0.2 * i + 0.3 * j + 0.1 * r)
                f12 += radial_weight * chaotic_scale * x[i]**2 * x[j]**2 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Multi-modal sine-cosine with tent map modulation
        f13 = 0.0
        for i in range(self.dim):
            modulator = self.tent_map(np.sin(x[i]))
            f13 += np.sin(modulator * x[i]) * np.cos(modulator * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Boundary-constrained chaotic polynomial
        f14 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**2
                f14 += penalty * np.exp(-0.1 * x[i]**2)
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14