import numpy as np

class TrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic trigonometric potentials with dynamic phase shifts
        f1 = 0.0
        for i in range(self.dim):
            phase = 0.2 * i + 0.1 * np.sum(x**2)
            f1 += np.sin(x[i] * (1.0 + 0.5 * np.sin(phase))) * np.exp(-0.05 * x[i]**2)
            
        # Adaptive radial conditioning with fractal-like scaling
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.3 * i + 0.1 * r)
            f2 += scale * np.cos(x[i] * (1.0 + 0.4 * np.cos(0.2 * x[i]))) * np.exp(-0.03 * x[i]**2)
            
        # Fractal cross-dimensional couplings with time-varying coefficients
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.7 + 0.3 * np.sin(0.25 * (i + j) + 0.1 * r)
                f3 += coeff * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Dynamic phase shifts with stochastic harmonic modulations
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.3 * i + 0.2 * r)
            phase_shift = 0.5 * np.sin(0.1 * i + 0.3 * np.random.uniform(-1, 1))
            f4 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.06 * x[i]**2)
            
        # Novel quartic cross-terms with time-varying coefficients
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.5 * np.cos(0.2 * (i - j) + 0.1 * r)
                f5 += coeff * x[i]**2 * x[j]**2 * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Modified interaction weights with chaotic modulation
        f6 = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.8 * np.sin(0.4 * i + 0.2 * r + np.pi/3)
            f6 += weight * x[i]**3 * np.exp(-0.05 * x[i]**2)
            
        # Increased algorithmic challenge through refined nonlinear interactions
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                f7 += interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Additional stochastic harmonic modulations
        f8 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * r)
            f8 += amp * np.sin(x[i] * (1.0 + 0.3 * np.cos(0.1 * x[i]))) * np.exp(-0.07 * x[i]**2)
            
        # Enhanced boundary attraction with fractal scaling
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                scale = 1.0 + 0.2 * np.sin(0.5 * i + 0.1 * r)
                f9 += scale * dist**3 * np.exp(-0.1 * dist)
                
        # Multi-scale fractal-like harmonic coupling
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 0.8 + 0.4 * np.sin(0.2 * (i - j) + 0.15 * r)
                f10 += scale * np.cos(x[i] * x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Hybrid coupling with sine and cosine components
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f11 += hybrid_term * x[i]**2 * x[j]**2 * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with enhanced chaotic modulation
        f12 = 0.0
        for i in range(self.dim):
            coeff = 2.0 + 1.0 * np.sin(0.2 * i + 0.1 * r)
            f12 += coeff * x[i]**4 * np.exp(-0.02 * r**2)
            
        # Cross-dimensional fractal interactions with dynamic coupling
        f13 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.9 + 0.3 * np.sin(0.4 * (i - j) + 0.15 * r)
                f13 += dynamic_weight * x[i]**3 * x[j]**3 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation for increased complexity
        f14 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.4 * np.sin(0.6 * i + 0.15 * r + np.pi/6)
            f14 += x[i]**2 * np.exp(-0.01 * x[i]**2) * chaos_factor
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14