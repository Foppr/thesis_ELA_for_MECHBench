import numpy as np

class ChaoticTentHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic components with radial harmonic interactions
        f1 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Chaotic tent map dynamics
            tent_val = 1.0 - 2.0 * np.abs(0.5 - (x[i] / 5.0) % 1.0)
            # Radial harmonic modulation
            harmonic = np.sin(0.8 * i + 0.3 * r) * np.cos(0.4 * i + 0.2 * r)
            f1 += tent_val * harmonic * np.exp(-0.5 * ((x[i] - harmonic) / (1.0 + 0.3 * np.sin(0.6 * i)))**2)
            
        # Cross-dimensional gradient interactions with adaptive coupling
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on tent map values
                coupling = 1.2 + 0.6 * np.sin(0.4 * (i + j) + 0.3 * r) * tent_val
                dist = np.sqrt((x[i] - x[j])**2 + 0.05)
                f2 += coupling * (x[i]**2 + x[j]**2) / (dist + 0.1)
                
        # Chaotic harmonic oscillations with varying frequencies and amplitudes
        f3 = 0.0
        for i in range(self.dim):
            # Time-varying frequency and amplitude based on tent map
            freq = 2.5 + 1.8 * np.sin(0.5 * i + 0.4 * r) * tent_val
            amp = 1.5 + 0.9 * np.cos(0.3 * i + 0.2 * r) * tent_val
            f3 += amp * np.sin(freq * x[i] + 0.6 * r) * np.cos(freq * x[i])
            
        # Adaptive conditioning with fractal-like scaling based on tent map
        f4 = 0.0
        for i in range(self.dim):
            # Fractal-like scaling factor from tent map
            scale = 1.0 + 0.4 * np.sin(0.7 * i + 0.5 * r) * tent_val
            f4 += scale * x[i]**4
            
        # Boundary repulsion with non-uniform penalty based on tent dynamics
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 1.8 * dist_from_boundary**2.5
                f5 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale chaotic modulation with enhanced tent complexity
        f6 = 0.0
        for i in range(self.dim):
            # Complex chaotic modulation from tent map
            mod1 = 1.0 + 0.6 * np.sin(0.9 * i + 0.5 * r) * tent_val
            mod2 = 1.0 + 0.5 * np.sin(0.7 * i + 0.4 * r) * tent_val
            f6 += mod1 * mod2 * x[i]**5
            
        # Cross-dimensional coupling with sinusoidal interactions based on tent dynamics
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sinusoidal coupling strength from tent map
                coupling = 0.9 + 0.5 * np.sin(0.6 * (i + j) + 0.4 * r) * tent_val
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f7 += coupling * interaction
                
        # Adaptive radial conditioning with dynamic parameters from tent map
        f8 = 0.0
        for i in range(self.dim):
            # Dynamic amplitude and frequency from tent map
            amp = 1.8 + 0.8 * np.sin(0.5 * i + 0.3 * r) * tent_val
            freq = 3.5 + 2.5 * np.cos(0.4 * i + 0.2 * r) * tent_val
            f8 += amp * np.sin(freq * x[i] + 0.3 * r) * np.exp(-0.1 * r**2)
            
        # Additional chaotic terms for increased complexity from tent map
        f9 = 0.0
        for i in range(self.dim):
            chaos_term = np.sin(1.0 * i + 0.6 * r) * np.cos(0.5 * i + 0.4 * r) * tent_val
            f9 += x[i]**3 * chaos_term
            
        # Gradient-based cross-dimensional interactions with tent map influence
        f10 = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_sum += (x[i] - x[j]) / (1.0 + (x[i] - x[j])**2)
            f10 += grad_sum**2 * tent_val
            
        # Introduce additional complexity through mixed polynomial and trigonometric terms with tent influence
        f11 = 0.0
        for i in range(self.dim):
            # Mixed polynomial and trigonometric components with tent modulation
            poly_term = x[i]**6 + 0.6 * x[i]**4
            trig_term = np.sin(2.5 * x[i]) + 0.6 * np.cos(3.5 * x[i])
            f11 += poly_term * trig_term * tent_val
            
        # Add a global scaling factor to balance the contribution of different components
        total = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        return total * (1.0 + 0.15 * np.sin(0.12 * r) * tent_val)