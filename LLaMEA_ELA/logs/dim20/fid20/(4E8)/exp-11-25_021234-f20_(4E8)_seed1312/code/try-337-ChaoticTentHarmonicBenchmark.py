import numpy as np

class ChaoticTentHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with radial harmonic interactions
        f1 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Tent map chaotic component
            tent = 1.0 - 2.0 * np.abs(0.5 - (x[i] / 5.0) % 1.0)
            # Radial harmonic interaction
            harmonic = np.sin(2.0 * np.pi * r + i * 0.5) * np.cos(2.0 * np.pi * r + i * 0.3)
            f1 += tent * harmonic * (x[i]**2 + 0.1)
            
        # Adaptive gradient conditioning with dynamic scaling
        f2 = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on position and radius
            scale = 1.0 + 0.5 * np.sin(0.3 * i + 0.2 * r) * np.cos(0.4 * i + 0.1 * r)
            f2 += scale * x[i]**3 * np.sin(0.5 * x[i] + 0.3 * r)
            
        # Cross-dimensional coupling with chaotic phase interactions
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase coupling
                phase_diff = np.sin(0.4 * (i - j) + 0.2 * r) * np.cos(0.3 * (i + j) + 0.1 * r)
                coupling = 1.0 + 0.3 * phase_diff
                f3 += coupling * x[i] * x[j] * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Multi-scale harmonic oscillations with chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            # Multiple frequency components
            freq1 = 2.0 + 1.5 * np.sin(0.2 * i + 0.1 * r)
            freq2 = 3.0 + 2.0 * np.cos(0.3 * i + 0.2 * r)
            f4 += (np.sin(freq1 * x[i]) + 0.5 * np.cos(freq2 * x[i])) * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like conditioning with self-similar structure
        f5 = 0.0
        for i in range(self.dim):
            # Self-similar scaling factor
            scale_factor = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * r) * np.cos(0.5 * i + 0.2 * r)
            f5 += scale_factor * x[i]**4
            
        # Boundary repulsion with chaotic penalty terms
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                # Chaotic penalty based on distance from boundary
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 1.5 * dist_from_boundary**2.5 * np.sin(0.7 * i + 0.4 * r)
                f6 += penalty
                
        # Adaptive radial conditioning with time-varying parameters
        f7 = 0.0
        for i in range(self.dim):
            # Time-varying radial parameter
            radial_param = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * r) * np.cos(0.2 * i + 0.1 * r)
            f7 += radial_param * x[i]**5
            
        # Cross-dimensional chaotic interactions with sinusoidal coupling
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sinusoidal coupling strength with chaotic modulation
                coupling = 0.8 + 0.4 * np.sin(0.5 * (i + j) + 0.3 * r) * np.cos(0.2 * (i - j) + 0.1 * r)
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f8 += coupling * interaction
                
        # Additional chaotic terms for increased complexity
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic modulation with tent map influence
            chaos_mod = np.sin(0.9 * i + 0.5 * r) * np.cos(0.4 * i + 0.3 * r)
            f9 += x[i]**3 * chaos_mod
            
        # Gradient-based interactions with chaotic weighting
        f10 = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic weight for gradient interaction
                    weight = 1.0 + 0.3 * np.sin(0.3 * (i + j) + 0.2 * r)
                    grad_sum += weight * (x[i] - x[j]) / (1.0 + (x[i] - x[j])**2)
            f10 += grad_sum**2
            
        # Mixed polynomial and chaotic terms with harmonic components
        f11 = 0.0
        for i in range(self.dim):
            # Polynomial and chaotic mixture
            poly_term = x[i]**6 + 0.5 * x[i]**4
            chaos_term = np.sin(0.8 * i + 0.4 * r) * np.cos(0.3 * i + 0.2 * r)
            f11 += poly_term * chaos_term
            
        # Global scaling with chaotic modulation
        total = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        return total * (1.0 + 0.2 * np.sin(0.2 * r))