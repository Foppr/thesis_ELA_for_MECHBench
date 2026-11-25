import numpy as np

class ChaoticRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with chaotic modulation
        f1 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Chaotic phase modulation for each dimension
            phase = np.sin(0.7 * i + 0.3 * r) * np.cos(0.4 * i + 0.2 * r)
            # Radial basis with adaptive width
            width = 1.0 + 0.5 * np.sin(0.5 * i + 0.1 * r)
            f1 += np.exp(-0.5 * ((x[i] - phase) / width)**2)
            
        # Cross-dimensional gradient interactions with time-varying coefficients
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on distance
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling = 1.5 + 0.8 * np.sin(0.3 * (i + j) + 0.2 * r)
                f2 += coupling * (x[i]**2 + x[j]**2) / dist
                
        # Chaotic harmonic oscillations with varying frequencies and amplitudes
        f3 = 0.0
        for i in range(self.dim):
            # Time-varying frequency and amplitude
            freq = 2.0 + 1.5 * np.sin(0.4 * i + 0.3 * r)
            amp = 1.2 + 0.8 * np.cos(0.3 * i + 0.2 * r)
            f3 += amp * np.sin(freq * x[i] + 0.5 * r) * np.cos(freq * x[i])
            
        # Adaptive conditioning with fractal-like scaling
        f4 = 0.0
        for i in range(self.dim):
            # Fractal-like scaling factor
            scale = 1.0 + 0.3 * np.sin(0.6 * i + 0.4 * r) * np.cos(0.3 * i + 0.2 * r)
            f4 += scale * x[i]**4
            
        # Boundary repulsion with non-uniform penalty
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                # Non-uniform penalty based on distance from boundary
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 2.0 * dist_from_boundary**3.0
                f5 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale chaotic modulation with enhanced complexity
        f6 = 0.0
        for i in range(self.dim):
            # Complex chaotic modulation
            mod1 = 1.0 + 0.5 * np.sin(0.8 * i + 0.4 * r) * np.cos(0.3 * i + 0.2 * r)
            mod2 = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * r) * np.cos(0.5 * i + 0.1 * r)
            f6 += mod1 * mod2 * x[i]**5
            
        # Cross-dimensional coupling with sinusoidal interactions
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Sinusoidal coupling strength
                coupling = 0.8 + 0.4 * np.sin(0.5 * (i + j) + 0.3 * r)
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f7 += coupling * interaction
                
        # Adaptive radial conditioning with dynamic parameters
        f8 = 0.0
        for i in range(self.dim):
            # Dynamic amplitude and frequency
            amp = 1.5 + 0.7 * np.sin(0.4 * i + 0.2 * r)
            freq = 3.0 + 2.0 * np.cos(0.3 * i + 0.1 * r)
            f8 += amp * np.sin(freq * x[i] + 0.2 * r) * np.exp(-0.1 * r**2)
            
        # Additional chaotic terms for increased complexity
        f9 = 0.0
        for i in range(self.dim):
            chaos_term = np.sin(0.9 * i + 0.5 * r) * np.cos(0.4 * i + 0.3 * r)
            f9 += x[i]**3 * chaos_term
            
        # Gradient-based cross-dimensional interactions
        f10 = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_sum += (x[i] - x[j]) / (1.0 + (x[i] - x[j])**2)
            f10 += grad_sum**2
            
        # Introduce additional complexity through mixed polynomial and trigonometric terms
        f11 = 0.0
        for i in range(self.dim):
            # Mixed polynomial and trigonometric components
            poly_term = x[i]**6 + 0.5 * x[i]**4
            trig_term = np.sin(2.0 * x[i]) + 0.5 * np.cos(3.0 * x[i])
            f11 += poly_term * trig_term
            
        # Add a global scaling factor to balance the contribution of different components
        total = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        return total * (1.0 + 0.1 * np.sin(0.1 * r))